from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional, TypedDict, Union

from botocore.client import BaseClient


class UsageClass(Enum):
    SPOT = "spot"
    ON_DEMAND = "on-demand"


class Architecture(Enum):
    I386 = "i386"
    X86_64 = "x86_64"
    ARM64 = "arm64"
    X86_64_MAC = "x86_64_mac"


class ProductDescription(Enum):
    LINUX_UNIX = "Linux/UNIX"
    RED_HAT_ENTERPRISE_LINUX = "Red Hat Enterprise Linux"
    SUSE_LINUX = "SUSE Linux"
    WINDOWS = "Windows"
    LINUX_UNIX_VPC = "Linux/UNIX (Amazon VPC)"
    RED_HAT_ENTERPRISE_LINUX_VPC = "Red Hat Enterprise Linux (Amazon VPC)"
    SUSE_LINUX_VPC = "SUSE Linux (Amazon VPC)"
    WINDOWS_VPC = "Windows (Amazon VPC)"


class FinalSpotPriceStrategy(Enum):
    MIN = "min"
    MAX = "max"
    AVERAGE = "average"


class InterruptionFrequencyInfo(TypedDict):
    min: int
    max: int
    rate: str


class DiskInfo(TypedDict):
    SizeInGB: int
    Count: int
    Type: str


class InstanceStorageInfo(TypedDict):
    Disks: List[DiskInfo]


class GpuInfo(TypedDict):
    total_gpu_memory: int


class _InstanceTypeRequired(TypedDict):
    price: float
    instance_type: str
    vcpu: int
    memory_gb: int
    network_performance: str
    storage: Union[str, List[DiskInfo]]


# Define the optional fields in a separate class that extends the required one
class InstanceType(_InstanceTypeRequired, total=False):
    az_price: Optional[Dict[str, float]]
    interruption_frequency: Optional[InterruptionFrequencyInfo]
    gpu_memory_gb: Optional[int]


InstanceTypeResponse = List[InstanceType]


class ClientsDict(TypedDict, total=False):
    ec2: Optional[BaseClient]
    pricing: Optional[BaseClient]


class BestEc2Options(TypedDict, total=False):
    region: Optional[str]
    describe_spot_price_history_concurrency: Optional[int]
    describe_on_demand_price_concurrency: Optional[int]
    clients: Optional[ClientsDict]
    cache_ttl_in_minutes: Optional[int]


class NetworkInfo(TypedDict):
    NetworkPerformance: str


class VCpuInfo(TypedDict):
    DefaultVCpus: int


class InstanceTypeInfo(TypedDict):  # total=False makes all keys optional
    InstanceType: str
    CurrentGeneration: bool
    FreeTierEligible: bool
    SupportedUsageClasses: List[str]
    SupportedRootDeviceTypes: List[str]
    SupportedVirtualizationTypes: List[str]
    BareMetal: bool
    Hypervisor: str
    ProcessorInfo: Dict[str, Union[List[str], float, List[str]]]
    VCpuInfo: VCpuInfo
    MemoryInfo: Dict[str, int]
    InstanceStorageSupported: bool
    InstanceStorageInfo: Optional[InstanceStorageInfo]
    EbsInfo: Dict[str, Union[str, Dict[str, Union[int, float]]]]
    NetworkInfo: NetworkInfo
    PlacementGroupInfo: Dict[str, List[str]]
    HibernationSupported: bool
    BurstablePerformanceSupported: bool
    DedicatedHostsSupported: bool
    AutoRecoverySupported: bool
    SupportedBootModes: List[str]
    NitroEnclavesSupport: str
    NitroTpmSupport: str
    NitroTpmInfo: Dict[str, List[str]]
    InterruptionFrequency: Optional[InterruptionFrequencyInfo]
    GpuInfo: Optional[GpuInfo]


class _InstanceTypeRequestRequired(TypedDict):
    vcpu: float
    memory_gb: float


class InstanceTypeRequest(_InstanceTypeRequestRequired, total=False):
    usage_class: Optional[UsageClass]
    burstable: Optional[bool]
    architecture: Optional[Architecture]
    product_description: Optional[ProductDescription]
    is_current_generation: Optional[bool]
    has_gpu: Optional[bool]
    gpu_memory: Optional[int]
    is_instance_storage_supported: Optional[bool]
    max_interruption_frequency: Optional[int]
    availability_zones: Optional[List[str]]
    final_spot_price_strategy: Optional[FinalSpotPriceStrategy]


class ExtendedInstanceTypeRequest(InstanceTypeRequest):
    region: str


class CacheEntry(TypedDict):
    result: InstanceTypeResponse
    datetime: datetime


CacheDict = Dict[str, CacheEntry]


class DescribeInstanceTypeRequest(TypedDict, total=False):
    is_current_generation: Optional[bool]
    is_instance_storage_supported: Optional[bool]


class _PriceDetails(TypedDict):
    price: float


class PriceDetails(_PriceDetails, total=False):
    az_price: Optional[Dict[str, float]]


class TypePriceDetails(TypedDict):
    instance_type: str
    price_details: PriceDetails
