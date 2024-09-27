#!/usr/bin/env python3
"""BasicCache that inherits from BaseCaching and is a caching system"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Defines a BasicCache class that inherits from BaseCaching"""

    def __init__(self):
        super().__init__()
        self.access_order = []


    def put(self, key: str, item: str) -> None:
        """Adds an item to the cache if both key and item are not None"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                least_recently_used_key = self.access_order.pop(0)
                del self.cache_data[least_recently_used_key]
                self.cache_data[key] = item
            self.cache_data[key] = item
            self.access_order.append(key)
    def get(self, key: str) -> str:
        """Retrieve an item from the cache"""
        if key in self.cache_data:
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data[key]
        return None
