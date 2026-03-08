class CacheService:

    def __init__(self):
        self.cache = {}

    def set(self, key, value):

        self.cache[key] = value

    def get(self, key):

        return self.cache.get(key)

    def delete(self, key):

        if key in self.cache:
            del self.cache[key]


# Demo
if __name__ == "__main__":

    cache = CacheService()

    cache.set("abc123", "https://example.com")

    print(cache.get("abc123"))
