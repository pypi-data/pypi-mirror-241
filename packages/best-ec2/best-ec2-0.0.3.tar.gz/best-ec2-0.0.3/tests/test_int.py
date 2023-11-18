from best_ec2 import (
    BestEc2,
    InstanceTypeRequest,
    InstanceTypeResponse,
    UsageClass,
    BestEc2Options,
    Architecture,
    ProductDescription,
    FinalSpotPriceStrategy,
)


def test_on_demand_instance_types_lack_az_price():
    ec2 = BestEc2()

    request: InstanceTypeRequest = {"vcpu": 1, "memory_gb": 1}

    response: InstanceTypeResponse = ec2.get_types(request)

    assert response is not None, "Response should not be None"

    for instance_type in response:
        assert (
            "az_price" not in instance_type
        ), f"Instance type {instance_type.get('instance_type', 'unknown')} should not have 'az_price' key."


def test_spot_instance_types_have_az_price():
    ec2 = BestEc2()

    request: InstanceTypeRequest = {
        "vcpu": 1,
        "memory_gb": 1,
        "usage_class": UsageClass.SPOT.value,
    }

    response: InstanceTypeResponse = ec2.get_types(request)

    assert response is not None, "Response should not be None"

    for instance_type in response:
        assert (
            "az_price" in instance_type
        ), f"Instance type {instance_type.get('instance_type', 'unknown')} must have 'az_price' key."


def test_on_demand_gpu():
    ec2 = BestEc2()

    request: InstanceTypeRequest = {
        "vcpu": 1,
        "memory_gb": 1,
        "usage_class": UsageClass.ON_DEMAND.value,
        "has_gpu": True,
    }

    response: InstanceTypeResponse = ec2.get_types(request)

    for instance_type in response:
        assert "gpu_memory_gb" in instance_type

    assert response is not None, "Response should not be None"


def test_advanced():
    from botocore.config import Config
    import logging
    import boto3

    ec2_client_config = Config(retries={"max_attempts": 20, "mode": "adaptive"})

    pricing_client_config = Config(retries={"max_attempts": 10, "mode": "standard"})

    ec2_client = boto3.Session().client(
        "ec2", config=ec2_client_config, region_name="eu-central-1"
    )
    pricing_client = boto3.Session().client(
        "pricing", config=pricing_client_config, region_name="us-east-1"
    )

    options: BestEc2Options = {
        "region": "eu-central-1",
        "describe_spot_price_history_concurrency": 20,
        "describe_on_demand_price_concurrency": 20,
        "clients": {"ec2": ec2_client, "pricing": pricing_client},
        "cache_ttl_in_minutes": 60,
    }

    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s: %(levelname)s: %(message)s"
    )
    logger = logging.getLogger()

    ec2 = BestEc2(options, logger)

    request: InstanceTypeRequest = {
        "vcpu": 1,
        "memory_gb": 2,
        "usage_class": UsageClass.SPOT.value,
        "burstable": False,
        "architecture": Architecture.X86_64.value,
        "product_description": ProductDescription.LINUX_UNIX.value,
        "is_current_generation": True,
        "is_instance_storage_supported": True,
        "max_interruption_frequency": 10,
        "availability_zones": [
            "eu-central-1a",
            "eu-central-1b",
        ],
        "final_spot_price_strategy": FinalSpotPriceStrategy.MIN.value,
    }

    response: InstanceTypeResponse = ec2.get_types(request)

    assert response is not None, "Response should not be None"
