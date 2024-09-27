#!/usr/bin/env python3
"""BasicCache that inherits from BaseCaching and is a caching system"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Defines a BasicCache class that inherits from BaseCaching"""

    def __int__(self):
        super().__init__()

    def put(self, key: str, item: str) -> None:
        """Adds an item to the cache if both key and item are not None"""
        if key is not None and item is not None:  # Check both key and item
            if len(self.cache_data) >= self.MAX_ITEMS:
                first_key = list(self.cache_data.keys())[-1]
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

                self.cache_data[key] = item
            self.cache_data[key] = item

    def get(self, key: str) -> str:
        """Retrieves an item from the cache"""
        if key is None:
            return None
        return self.cache_data.get(key)
