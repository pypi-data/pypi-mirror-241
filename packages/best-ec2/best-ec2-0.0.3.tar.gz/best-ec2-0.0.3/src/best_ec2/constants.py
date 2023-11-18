DEFAULT_CACHE_TTL_IN_MINUTES = 120  # Default time to live for cache entries, in minutes
DEFAULT_SPOT_CONCURRENCY = 10
DEFAULT_ON_DEMAND_CONCURRENCY = 10

# Default AWS region for operations
DEFAULT_REGION = "us-east-1"

REGIONS = {
    "us-east-2": "US East (Ohio)",
    "us-east-1": "US East (N. Virginia)",
    "us-west-1": "US West (N. California)",
    "us-west-2": "US West (Oregon)",
    "ap-east-1": "Asia Pacific (Hong Kong)",
    "ap-south-1": "Asia Pacific (Mumbai)",
    "ap-northeast-3": "Asia Pacific (Osaka-Local)",
    "ap-northeast-2": "Asia Pacific (Seoul)",
    "ap-southeast-1": "Asia Pacific (Singapore)",
    "ap-southeast-2": "Asia Pacific (Sydney)",
    "ap-northeast-1": "Asia Pacific (Tokyo)",
    "ca-central-1": "Canada (Central)",
    "cn-north-1": "China (Beijing)",
    "cn-northwest-1": "China (Ningxia)",
    "eu-central-1": "EU (Frankfurt)",
    "eu-west-1": "EU (Ireland)",
    "eu-west-2": "EU (London)",
    "eu-west-3": "EU (Paris)",
    "eu-north-1": "EU (Stockholm)",
    "me-south-1": "Middle East (Bahrain)",
    "sa-east-1": "South America (Sao Paulo)",
}

# Short names for EC2 operating system product descriptions
OS_PRODUCT_DESCRIPTION_MAP = {
    "Linux/UNIX": "Linux",
    "Red Hat Enterprise Linux": "RHEL",
    "SUSE Linux": "SUSE",
    "Windows": "Windows",
    "Linux/UNIX (Amazon VPC)": "Linux",
    "Red Hat Enterprise Linux (Amazon VPC)": "RHEL",
    "SUSE Linux (Amazon VPC)": "SUSE",
    "Windows (Amazon VPC)": "Windows",
}
