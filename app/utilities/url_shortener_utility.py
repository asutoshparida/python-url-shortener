"""
url_shortener_utility.py
~~~~~~~~
Module containing URL shortener utility functions
"""
import logging
from app import encode_cache as ec
from app import decode_cache as dc

logger = logging.getLogger('URLShortenerUtil')


class URLShortenerUtil(object):

    url_id = 1000
    shorten_domain = "http://short-url.com/"

    @classmethod
    def shorten_url(cls, original_url):
        """
        Method to retrieve shorten_url URL from cache for a original_url,
        if not found then create a new one and add to cache
        :param original_url: String
        :return: shorten_url: String
        """
        if ec.get(original_url) is not None:
            shorten_url = ec.get(original_url)
            logger.info('returning shorten_url from cache :' + str(shorten_url))
        else:
            shorten_url_code = cls.base_62_encode(cls.url_id)
            shorten_url = cls.shorten_domain + shorten_url_code
            # store shorten_url in both decode_cache & encode_cache
            ec.add(original_url, shorten_url)
            dc.add(shorten_url, original_url)
            # increase cnt for next url
            cls.url_id += 1
            logger.info('returning new shorten_url :' + str(shorten_url))
        return shorten_url

    @staticmethod
    def base_62_encode(url_id):
        """
        Method to generate base62 alphanumeric string for a base10 integer
        :param url_id: int
        :return: String
        """
        base_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        base = len(base_characters)
        result = []
        # convert base10 id into base62 id for having alphanumeric shorten url
        while url_id > 0:
            val = url_id % base
            result.append(base_characters[val])
            url_id = url_id // base

        return "".join(result[::-1])
