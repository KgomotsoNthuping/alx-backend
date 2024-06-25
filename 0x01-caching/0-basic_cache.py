#!/usr/bin/python3
"""0-basic_cache.py"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A basic cache implementaion"""
    def put(self, key, item):
        """Add item"""
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """Get item"""
        return self.cache_data.get(key, None)
