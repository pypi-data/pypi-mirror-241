import json
from typing import Dict, List, Optional, Tuple

from ..constants import OS_PRODUCT_DESCRIPTION_MAP, REGIONS
from ..types import (
    FinalSpotPriceStrategy,
    InstanceTypeInfo,
    ProductDescription,
    PriceDetails,
)
from .abstract_sort_strategy import AbstractSortStrategy


class SortOnDemandStrategy(AbstractSortStrategy):
    """Sort strategy for On-Demand EC2 instances."""

    def _get_price(
        self,
        filtered_instances: List[InstanceTypeInfo],
        product_description: ProductDescription,
        availability_zones: Optional[List[str]],
        final_spot_price_strategy: FinalSpotPriceStrategy,
    ) -> Dict[str, PriceDetails]:
        operating_system = self._map_product_description_to_os(product_description)
        return self._get_on_demand_instance_price(operating_system)

    @staticmethod
    def _map_product_description_to_os(product_description: ProductDescription) -> str:
        return OS_PRODUCT_DESCRIPTION_MAP[product_description]

    def _get_on_demand_instance_price(
        self, operating_system: str
    ) -> Dict[str, PriceDetails]:
        filters = self._build_ec2_filter_criteria(operating_system)
        return self._retrieve_pricing_records(filters)

    def _build_ec2_filter_criteria(self, operating_system: str) -> List[Dict[str, str]]:
        return [
            {"Type": "TERM_MATCH", "Field": "preInstalledSw", "Value": "NA"},
            {
                "Type": "TERM_MATCH",
                "Field": "productFamily",
                "Value": "Compute Instance",
            },
            {"Type": "TERM_MATCH", "Field": "termType", "Value": "OnDemand"},
            {"Type": "TERM_MATCH", "Field": "location", "Value": REGIONS[self._region]},
            {
                "Type": "TERM_MATCH",
                "Field": "licenseModel",
                "Value": "No License required",
            },
            {"Type": "TERM_MATCH", "Field": "tenancy", "Value": "Shared"},
            {"Type": "TERM_MATCH", "Field": "capacitystatus", "Value": "Used"},
            {
                "Type": "TERM_MATCH",
                "Field": "operatingSystem",
                "Value": operating_system,
            },
        ]

    def _retrieve_pricing_records(
        self, filters: List[Dict[str, str]]
    ) -> Dict[str, PriceDetails]:
        records = {}
        next_token = None

        while True:
            response = self._query_pricing_api(filters, next_token)
            price_list = response.get("PriceList", [])

            if not price_list:
                break

            for price in price_list:
                instance_type, instance_price = self._parse_price_details(price)
                if instance_price > 0:
                    records[instance_type] = {"price": instance_price}

            next_token = response.get("NextToken")
            if not next_token:
                break

        return records

    def _query_pricing_api(
        self, filters: List[Dict[str, str]], next_token: Optional[str]
    ) -> dict:
        request_parameters = {
            "ServiceCode": "AmazonEC2",
            "Filters": filters,
        }

        if next_token:
            request_parameters["NextToken"] = next_token

        return self._pricing_client.get_products(**request_parameters)

    @staticmethod
    def _parse_price_details(price: str) -> Tuple[str, float]:
        details = json.loads(price)
        price_dimensions = next(iter(details["terms"]["OnDemand"].values()))[
            "priceDimensions"
        ]
        pricing_details = next(iter(price_dimensions.values()))
        instance_price = float(pricing_details["pricePerUnit"]["USD"])
        instance_type = details["product"]["attributes"]["instanceType"]

        return instance_type, instance_price
