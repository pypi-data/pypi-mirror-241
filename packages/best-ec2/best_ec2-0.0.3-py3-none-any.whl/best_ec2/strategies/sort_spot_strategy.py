import os
from logging import Logger
from multiprocessing.pool import ThreadPool
from typing import Dict, List, Type, Optional

from botocore.client import BaseClient
from lambda_thread_pool import LambdaThreadPool

from ..types import (
    FinalSpotPriceStrategy,
    InstanceTypeInfo,
    ProductDescription,
    PriceDetails,
    TypePriceDetails,
)
from ..aws_utils import AwsUtils
from ..exceptions import InvalidStrategyError
from .abstract_sort_strategy import AbstractSortStrategy


class SortSpotStrategy(AbstractSortStrategy):
    def __init__(
        self,
        region: str,
        pricing_client: BaseClient,
        ec2_client: BaseClient,
        logger: Logger,
        spot_price_history_concurrency: int,
    ):
        super().__init__(
            region, pricing_client, ec2_client, logger, spot_price_history_concurrency
        )
        self._pool: Type[ThreadPool] = (
            LambdaThreadPool
            if os.environ.get("AWS_LAMBDA_FUNCTION_NAME")
            else ThreadPool
        )
        self._aws_utils = AwsUtils(ec2_client)

    def _get_price(
        self,
        filtered_instances: List[InstanceTypeInfo],
        product_description: ProductDescription,
        availability_zones: Optional[List[str]],
        final_spot_price_strategy: FinalSpotPriceStrategy,
    ) -> Dict[str, PriceDetails]:
        availability_zones = (
            availability_zones
            or self._aws_utils.get_all_availability_zones_for_region()
        )

        with self._pool() as executor:
            futures = [
                executor.apply_async(
                    self._get_spot_instance_price,
                    (
                        ec2_instance,
                        product_description,
                        availability_zones,
                        final_spot_price_strategy,
                    ),
                )
                for ec2_instance in filtered_instances
            ]

            ec2_prices = {
                f.get()["instance_type"]: f.get()["price_details"]
                for f in futures
                if f.get()
            }

        return ec2_prices

    def _get_spot_instance_price(
        self,
        ec2_instance: InstanceTypeInfo,
        product_description: ProductDescription,
        availability_zones: List[str],
        strategy: FinalSpotPriceStrategy,
    ) -> Optional[TypePriceDetails]:
        instance_type = ec2_instance["InstanceType"]
        filters = [{"Name": "product-description", "Values": [product_description]}]

        if availability_zones:
            filters.append({"Name": "availability-zone", "Values": availability_zones})

        response = self._ec2_client.describe_spot_price_history(
            InstanceTypes=[instance_type], Filters=filters
        )

        history_events = response["SpotPriceHistory"]
        az_price: Dict[str, float] = {
            event["AvailabilityZone"]: float(event["SpotPrice"])
            for event in history_events
            if event["AvailabilityZone"] in availability_zones
        }

        spot_price = self._calculate_spot_price(list(az_price.values()), strategy)

        return {
            "instance_type": instance_type,
            "price_details": {"price": spot_price, "az_price": az_price},
        }

    @staticmethod
    def _calculate_spot_price(
        prices: List[float], strategy: FinalSpotPriceStrategy
    ) -> float:
        if strategy == "average":
            return sum(prices) / len(prices)
        elif strategy == "max":
            return max(prices)
        elif strategy == "min":
            return min(prices)
        else:
            raise InvalidStrategyError(strategy)
