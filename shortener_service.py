from id_generator import IDGenerator

BASE62 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

class URLShortener:

    def __init__(self):
        self.db = {}
        self.generator = IDGenerator()

    def encode(self, num):
        base = len(BASE62)
        short = []

        while num > 0:
            short.append(BASE62[num % base])
            num //= base

        return "".join(reversed(short))

    def shorten_url(self, long_url):
        new_id = self.generator.generate_id()
        short_key = self.encode(new_id)

        self.db[short_key] = long_url

        return f"https://short.ly/{short_key}"

    def get_original_url(self, short_key):
        return self.db.get(short_key)


# Demo
if __name__ == "__main__":

    shortener = URLShortener()

    short = shortener.shorten_url("https://example.com/very-long-url")
    print(short)

    key = short.split("/")[-1]
    print(shortener.get_original_url(key))
