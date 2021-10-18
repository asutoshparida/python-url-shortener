"""
url_shortener_schema.py
~~~~~~~~
marshmallow schema validation module for URl shortener
"""

from marshmallow import Schema, fields, validates, ValidationError
import validators


def validate_url(url, field):
    if not url:
        raise ValidationError("Input {} cannot be blank !".format(field))
    else:
        if not validators.url(url):
            raise ValidationError("Please enter a valid {} !".format(field))
        else:
            return True


class URLEncodeSchema(Schema):
    original_url = fields.String()

    @validates('original_url')
    def validate_original_url(self, url):
        """
        Method to validate original_url using URL validators
        :param url: String
        :return: String
        """
        validate_url(url, 'original_url')


class URLDecodeSchema(Schema):
    shorten_url = fields.String()

    @validates('shorten_url')
    def validate_shorten_url(self, url):
        """
        Method to validate shorten_url using URL validators
        :param url: String
        :return: String
        """
        validate_url(url, 'shorten_url')


class URLSchema(Schema):

    original_url = fields.String()
    shorten_url = fields.String()
