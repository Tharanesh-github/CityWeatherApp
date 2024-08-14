# app/utils/cache.py

import time

class SimpleCache:
    def __init__(self, expiration=300):
        self.cache = {}
        self.expiration = expiration

    def get(self, key):
        if key in self.cache and time.time() - self.cache[key]['time'] < self.expiration:
            return self.cache[key]['value']
        elif key in self.cache:
            del self.cache[key]
        return None

    def set(self, key, value):
        self.cache[key] = {'value': value, 'time': time.time()}
