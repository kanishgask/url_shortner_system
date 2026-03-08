class AnalyticsService:

    def __init__(self):
        self.click_data = {}

    def record_click(self, short_key):

        if short_key not in self.click_data:
            self.click_data[short_key] = 0

        self.click_data[short_key] += 1

    def get_clicks(self, short_key):

        return self.click_data.get(short_key, 0)

    def get_all_stats(self):

        return self.click_data


# Demo
if __name__ == "__main__":

    analytics = AnalyticsService()

    analytics.record_click("abc1")
    analytics.record_click("abc1")
    analytics.record_click("xyz2")

    print(analytics.get_all_stats())
