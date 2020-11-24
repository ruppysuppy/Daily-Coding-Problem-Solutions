"""
Problem:

Implement a URL shortener with the following methods:

shorten(url), which shortens the url into a six-character alphanumeric string, such as
zLg6wl.
restore(short), which expands the shortened string into the original url. If no such
shortened string exists, return null.
Hint: What if we enter the same URL twice?
"""

from hashlib import sha224
from typing import Optional


class URL_Shortner:
    def __init__(self, prefix: str = "http://short_url.in/") -> None:
        self.shortened_url_map = {}
        self.url_prefix = prefix

    def shorten(self, url: str) -> str:
        shortened_url_hash = sha224(url.encode()).hexdigest()[:6]
        if shortened_url_hash not in self.shortened_url_map:
            self.shortened_url_map[shortened_url_hash] = url
        return self.url_prefix + shortened_url_hash

    def restore(self, short: str) -> Optional[str]:
        if short[-6:] in self.shortened_url_map:
            return self.shortened_url_map[short[-6:]]
        return None


if __name__ == "__main__":
    us = URL_Shortner()

    url = "https://www.google.com/"
    shortened_url = us.shorten(url)
    print(shortened_url)

    print(us.restore(shortened_url))
    print(us.restore("http://short_url.in/64f827"))
