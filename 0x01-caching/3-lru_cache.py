#!/usr/bin/env python3
"""BasicCache that inherits from BaseCaching and is a caching system"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Defines a BasicCache class that inherits from BaseCaching"""

    def __init__(self):
        self.cache_data = {}
        self.access_order = []

    def get(self, key):
        if key in self.cache_data:
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data[key]
        return None

    def put(self, key, item):
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                lru_key = self.access_order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")
            self.cache_data[key] = item
            self.access_order.append(key)  