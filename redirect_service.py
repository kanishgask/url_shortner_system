class RedirectService:

    def __init__(self, shortener_service):
        self.shortener_service = shortener_service
        self.click_count = {}

    def redirect(self, short_key):

        url = self.shortener_service.get_original_url(short_key)

        if not url:
            return "URL not found"

        if short_key not in self.click_count:
            self.click_count[short_key] = 0

        self.click_count[short_key] += 1

        return url


# Demo
if __name__ == "__main__":

    from shortener_service import URLShortener

    shortener = URLShortener()
    redirector = RedirectService(shortener)

    short = shortener.shorten_url("https://example.com")

    key = short.split("/")[-1]

    print(redirector.redirect(key))
