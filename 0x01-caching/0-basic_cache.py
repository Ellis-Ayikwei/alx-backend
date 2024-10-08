#!/usr/bin/env python3
"""BasicCache that inherits from BaseCaching and is a caching system"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Defines a BasicCache class that inherits from BaseCaching"""

    def put(self, key: str, item: str) -> None:
        """Adds an item to the cache if both key and item are not None"""
        if key is not None and item is not None:  # Check both key and item
            self.cache_data[key] = item

    def get(self, key: str) -> str:
        """Retrieves an item from the cache"""
        if key is None:
            return None
        return self.cache_data.get(key)
