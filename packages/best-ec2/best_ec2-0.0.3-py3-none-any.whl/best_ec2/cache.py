import hashlib
import json
from datetime import datetime, timedelta
from typing import Optional

from .types import (
    CacheDict,
    ExtendedInstanceTypeRequest,
    InstanceTypeRequest,
    InstanceTypeResponse,
)


class Cache:
    def __init__(self, ttl_minutes: int, region: str):
        self._region = region
        self._ttl_minutes = ttl_minutes
        self._cache: CacheDict = {}

    def get(self, request: InstanceTypeRequest) -> Optional[InstanceTypeResponse]:
        hash_digest = self._get_hash(request)

        cached = self._cache.get(hash_digest)
        if cached and self._is_valid(cached["datetime"]):
            return cached["result"]
        return None

    def set(self, request: InstanceTypeRequest, result: InstanceTypeResponse) -> None:
        hash_digest = self._get_hash(request)
        self._cache[hash_digest] = {"result": result, "datetime": datetime.now()}

    def _get_hash(self, request: InstanceTypeRequest) -> str:
        cached_request: ExtendedInstanceTypeRequest = dict(request)
        cached_request["region"] = self._region
        hash_object = hashlib.md5(json.dumps(cached_request, sort_keys=True).encode())
        return hash_object.hexdigest()

    def _is_valid(self, cache_datetime: datetime) -> bool:
        return (datetime.now() - cache_datetime) < timedelta(minutes=self._ttl_minutes)
