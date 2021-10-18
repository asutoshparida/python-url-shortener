"""
url_shortener_controller.py
~~~~~~~~
API controller module containing URL shortener endpoints
"""
from flask import request, jsonify
import logging
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from marshmallow import ValidationError
from app.schemas.url_shortener_schema import URLSchema, URLEncodeSchema, URLDecodeSchema
from app.services.url_shortener_service import URLShortenerService as Service
from app.errors import errors

logger = logging.getLogger('URLShortenerController')
url_shortener_api = Namespace("URL Shortener", description="Encode & Decode URLs")


@url_shortener_api.route("/encode")
class EncodeURLResource(Resource):
    """URL encode endpoint
    This class will contain all endpoints related to encoding of a URL
    """

    @accepts(schema=URLEncodeSchema, api=url_shortener_api)
    @responds(schema=URLSchema)
    @url_shortener_api.expect(validate=True)
    def post(self) -> Response:
        """URL encode endpoint
        POST : /api/url/encode
        """
        if not request.json:
            return Response(status=errors['BadRequest'].get('status'), response=errors['BadRequest'].get('response'))

        api_data = request.json
        logger.info('request_data :' + str(api_data))

        # input data validation
        try:
            schema = URLEncodeSchema()
            schema.load(api_data)
        except ValidationError as err:
            return jsonify(err.messages), 400

        try:
            shorten_url = Service.encode_service(api_data['original_url'])
        except (Exception,):
            return Response(status=errors['ServerError'].get('status'), response=errors['ServerError'].get('response'))

        logger.info('shorten_url :' + str(shorten_url))
        api_data['shorten_url'] = shorten_url

        return jsonify(api_data)


@url_shortener_api.route("/decode")
class DecodeURLResource(Resource):
    """URL decode endpoint
    This class will contain all endpoints related to decoding of a URL
    """

    @accepts(schema=URLDecodeSchema, api=url_shortener_api)
    @responds(schema=URLSchema)
    @url_shortener_api.expect(validate=True)
    def post(self) -> Response:
        """URL decode endpoint
        POST : /api/url/decode
        """
        if not request.json:
            return Response(status=errors['BadRequest'].get('status'), response=errors['BadRequest'].get('response'))

        api_data = request.json
        logger.info('request_data :' + str(api_data))

        # input data validation
        try:
            schema = URLDecodeSchema()
            schema.load(api_data)
        except ValidationError as err:
            return jsonify(err.messages), 400

        try:
            original_url = Service.decode_service(api_data['shorten_url'])
        except (Exception,):
            return Response(status=errors['ServerError'].get('status'), response=errors['ServerError'].get('response'))

        logger.info('original_url :' + str(original_url))
        # If not found in cache then return "No Data Found"
        if original_url is None:
            original_url = "No Data Found"

        api_data['original_url'] = original_url

        return jsonify(api_data)
