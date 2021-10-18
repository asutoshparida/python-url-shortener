"""
test_url_shortener_controller.py
~~~~~~~~
controller module endpoint test cases for url shortener
"""
from unittest.mock import patch
from flask.testing import FlaskClient
from app.tests.fixtures import client, app

from app.services.url_shortener_service import URLShortenerService as Service
from app.controllers.url_shortener_controller import EncodeURLResource
from app.schemas.url_shortener_schema import URLSchema


class TestEncodeURLResource:

    def test_post(self, client: FlaskClient):
        payload = dict(original_url="https://www.google.com/")
        result = client.post("/api/url/encode", json=payload).get_json()
        expected = (
            URLSchema().dump(dict(original_url="https://www.google.com/", shorten_url="http://short-url.com/g8"))
        )
        assert result == expected


class TestDecodeURLResource:

    def test_post(self, client: FlaskClient):
        payload = dict(shorten_url="http://short-url.com/g8")
        result = client.post("/api/url/decode", json=payload).get_json()
        expected = (
            URLSchema().dump(dict(original_url="No Data Found", shorten_url="http://short-url.com/g8"))
        )
        assert result == expected
