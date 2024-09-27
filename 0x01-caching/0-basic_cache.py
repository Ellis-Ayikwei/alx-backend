#!/usr/bin/env python3
"""BasicCache that inherits from BaseCaching and is a caching system"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Definese the class for the Basic Cache"""

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        if key is None:
            return None
        """Must return the value in self.cache_data linked to key"""
        the_value = self.cache_data.get(key)
        if not the_value:
            return None
        return the_value
