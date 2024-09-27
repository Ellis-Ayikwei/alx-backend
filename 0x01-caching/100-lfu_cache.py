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
        if key is not None and item is not None:
            if key in self.cache_data:
                # Update the item if the key already exists
                self.cache_data[key] = item
                self.used_ord[key] += 1  # Increase the usage count
                self.access_order.remove(key)
                self.access_order.append(key)  # Update access order
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    # Cache is full; find the least frequently used key
                    min_used = min(self.used_ord.values())
                    keys_with_min_value = [
                        k for k, v in self.used_ord.items() if v == min_used
                    ]

                    the_key_to_del = None
                    for key in keys_with_min_value:
                        if key in self.access_order:
                            the_key_to_del = key
                            break
                    if the_key_to_del:
                        del self.cache_data[the_key_to_del]
                        del self.used_ord[the_key_to_del]
                        self.access_order.remove(the_key_to_del)
                        print(f"DISCARD: {the_key_to_del}")

                # Add the new item
                self.cache_data[key] = item
                self.used_ord[key] = 1  # Initialize usage count
                self.access_order.append(key)  # Track the new key access order

    def get(self, key: str) -> str:
        """Retrieve an item from the cache"""
        if key in self.cache_data:
            # Update the access order and usage count
            self.access_order.remove(key)
            self.access_order.append(key)
            self.used_ord[key] += 1
            return self.cache_data[key]
        return None
