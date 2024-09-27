#!/usr/bin/env python3
"""BasicCache that inherits from BaseCaching and is a caching system"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Defines a BasicCache class that inherits from BaseCaching"""

    def __init__(self):
        super().__init__()
        self.access_order = []
        self.used_ord = {}

    def put(self, key: str, item: str) -> None:
        """Adds an item to the cache if both key and item are not None"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.used_ord[key] += 1
            self.access_order.remove(key)
            self.access_order.append(key)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_used_keys = [
                    k for k, v in self.used_ord.items()
                    if v == min(self.used_ord.values())
                ]
                least_recently_used_key = min_used_keys[0]
                del self.cache_data[least_recently_used_key]
                del self.used_ord[least_recently_used_key]
                print(f"DISCARD: {least_recently_used_key}")

            self.cache_data[key] = item
            self.used_ord[key] = 1
            self.access_order.append(key)

    def get(self, key: str) -> str:
        """Retrieve an item from the cache"""
        if key in self.cache_data:
            self.access_order.remove(key)
            self.access_order.append(key)
            self.used_ord[key] += 1
            return self.cache_data[key]
        return None
