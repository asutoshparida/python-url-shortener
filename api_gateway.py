"""
api_gateway.py
~~~~~~~~
API Gateway entry point module
"""
import os
from logging.config import dictConfig
import yaml
from pkg_resources import resource_stream
from app import create_app

# setup logger
dictConfig(yaml.load(resource_stream(__name__, 'logging.yaml'), Loader=yaml.FullLoader))
app = create_app(os.getenv("FLASK_ENV") or "dev")

if __name__ == "__main__":
    app.run(debug=True)
