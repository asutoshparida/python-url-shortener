import flask.scaffold
import werkzeug
from flask_restx import Api
from flask_caching import Cache
from flask import Flask, jsonify

flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
werkzeug.cached_property = werkzeug.utils.cached_property

encode_cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
decode_cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})


def create_app(env=None):
    '''
    Method to initialise flask app and setting up Api gateway
    Then it configures both encode_cache & decode_cache(data store for URl Shortener)
    '''
    from .config import config_by_name
    from app.controllers import register_routes

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "tests"])
    api = Api(app, title="API Gateway", version="0.1.0", prefix="/api", url_scheme="/api")
    encode_cache.init_app(app)
    decode_cache.init_app(app)

    register_routes(api, app)

    @app.route("/health")
    def health():
        return jsonify("healthy")

    return app
