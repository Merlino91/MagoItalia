import random
from curl_cffi.requests import AsyncSession
from fake_headers import Headers


class HeaderRotator:
    def __init__(self):
        self.browsers = [
            "chrome110",
            "chrome120",
            "edge101",
            "safari15_3"
        ]

    def get_headers(self):
        return Headers(headers=True).generate()

    def get_browser(self):
        return random.choice(self.browsers)

    async def get(self, client: AsyncSession, url, method="GET", **kwargs):
        headers = self.get_headers()
        browser = self.get_browser()

        # Override user-agent explicitly to appear as a regular browser
        headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

        response = await client.request(
            method,
            url,
            headers=headers,
            impersonate=browser,
            timeout=30,
            **kwargs
        )

        return response

