"""
test_url_shortener_utility.py
~~~~~~~~
utility module test cases for url shortener
"""
from app.utilities.url_shortener_utility import URLShortenerUtil


class TestURLShortenerUtil:

    def test_base_62_encode(self):
        result = URLShortenerUtil.base_62_encode(10000)
        expected = "2Bi"
        assert result == expected
