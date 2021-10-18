"""
url_shortener_service.py
~~~~~~~~
service module for URl shortener
"""
from app.utilities.url_shortener_utility import URLShortenerUtil as Util
from app import decode_cache as dc


class URLShortenerService(object):

    @staticmethod
    def encode_service(original_url):
        """
        Method to shorten the original URL
        :param original_url: String
        :return: shorten_url: String
        """
        return Util.shorten_url(original_url)

    @staticmethod
    def decode_service(shorten_url):
        """
        Method to retrieve original URL from cache for a shorten_url
        :param shorten_url: String
        :return: original_url: String
        """
        return dc.get(shorten_url)
