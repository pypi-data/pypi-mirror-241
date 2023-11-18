from logging import Logger, getLogger, StreamHandler
from typing import Optional, List

import boto3
from botocore.client import BaseClient

from .types import (
    BestEc2Options,
    DescribeInstanceTypeRequest,
    InstanceTypeRequest,
    InstanceTypeResponse,
    ProductDescription,
    UsageClass,
    Architecture,
    InstanceTypeInfo,
)
from .constants import (
    DEFAULT_CACHE_TTL_IN_MINUTES,
    DEFAULT_SPOT_CONCURRENCY,
    DEFAULT_REGION,
)
from .strategies.sort_strategy_factory import SortStrategyFactory
from .cache import Cache
from .validators import Validator
from .filters import FilterChain


class BestEc2Impl:
    def __init__(
        self, options: Optional[BestEc2Options] = None, logger: Optional[Logger] = None
    ):
        options = options if options is not None else {}
        self._region = options.get("region", DEFAULT_REGION)
        cache_ttl = options.get("cache_ttl_in_minutes", DEFAULT_CACHE_TTL_IN_MINUTES)
        self._cache = Cache(cache_ttl, self._region)
        self._ec2_client = self._get_client(options, "ec2", self._region)
        self._pricing_client = self._get_client(options, "pricing", "us-east-1")
        self._logger = logger or self._setup_default_logger()
        self._spot_price_history_concurrency = options.get(
            "describe_spot_price_history_concurrency", DEFAULT_SPOT_CONCURRENCY
        )

    @staticmethod
    def _setup_default_logger() -> Logger:
        logger = getLogger(__name__)
        console_handler = StreamHandler()
        logger.addHandler(console_handler)
        return logger

    def get_types(
        self, request: Optional[InstanceTypeRequest] = None
    ) -> InstanceTypeResponse:
        request = self._prepare_request_with_defaults(request)

        Validator.instance_type_request(request)

        if cached_result := self._cache.get(request):
            self._logger.info("Cache hit")
            return cached_result

        self._logger.info("Cache miss")

        instances = self._fetch_and_describe_instance_types(request)

        filtered_instances = self._apply_filters_to_instances(instances, request)
        sorted_instances = self._sort_instances_by_strategy(filtered_instances, request)

        self._cache_result(request, sorted_instances)
        return sorted_instances

    @staticmethod
    def _prepare_request_with_defaults(
        request: Optional[InstanceTypeRequest],
    ) -> InstanceTypeRequest:
        if request is None:
            request = {}
        request.setdefault("usage_class", UsageClass.ON_DEMAND.value)
        request.setdefault("architecture", Architecture.X86_64.value)
        request.setdefault("product_description", ProductDescription.LINUX_UNIX.value)
        return request

    def _fetch_and_describe_instance_types(
        self, request: InstanceTypeRequest
    ) -> List[InstanceTypeInfo]:
        filter_params = self._extract_filter_params(request)
        return self._describe_instance_types(filter_params)

    def _apply_filters_to_instances(
        self, instances: List[InstanceTypeInfo], request: InstanceTypeRequest
    ) -> List[InstanceTypeInfo]:
        self._logger.debug(
            f"Number of instance types before filtering: {len(instances)}"
        )
        filtered_instances = FilterChain(self._region).execute(instances, request)
        self._logger.debug(
            f"Number of instance types after filtering: {len(filtered_instances)}"
        )
        return filtered_instances

    def _sort_instances_by_strategy(
        self, instances: List[InstanceTypeInfo], request: InstanceTypeRequest
    ) -> InstanceTypeResponse:
        strategy = SortStrategyFactory.create(
            request["usage_class"],
            self._region,
            self._pricing_client,
            self._ec2_client,
            self._logger,
            self._spot_price_history_concurrency,
        )
        return strategy.sort(
            instances,
            request["product_description"],
            request.get("availability_zones"),
            request.get("final_spot_price_strategy", "min"),
        )

    def _cache_result(
        self, request: InstanceTypeRequest, result: InstanceTypeResponse
    ) -> None:
        self._cache.set(request, result)

    @staticmethod
    def _extract_filter_params(
        request: InstanceTypeRequest,
    ) -> DescribeInstanceTypeRequest:
        return {
            "is_current_generation": request.get("is_current_generation"),
            "is_instance_storage_supported": request.get(
                "is_instance_storage_supported"
            ),
        }

    @staticmethod
    def _get_client(options: BestEc2Options, service: str, region: str) -> BaseClient:
        if (
            options.get("clients") is not None
            and options["clients"].get(service) is not None
        ):
            return options["clients"][service]
        else:
            return boto3.session.Session().client(service, region_name=region)

    def _describe_instance_types(
        self, options: Optional[DescribeInstanceTypeRequest] = None
    ) -> List[InstanceTypeInfo]:
        filters = []
        if options.get("is_current_generation") is not None:
            is_current_generation = (
                "true" if options.get("is_current_generation") else "false"
            )
            filters.append(
                {
                    "Name": "current-generation",
                    "Values": [is_current_generation],
                }
            )
        if options.get("is_instance_storage_supported") is not None:
            filters.append(
                {
                    "Name": "instance-storage-supported",
                    "Values": [
                        "true" if options["is_instance_storage_supported"] else "false"
                    ],
                }
            )

        instances = []
        paginator = self._ec2_client.get_paginator("describe_instance_types")
        for page in paginator.paginate(Filters=filters):
            instances.extend(page["InstanceTypes"])

        return instances
