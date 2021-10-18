import pytest

from app import create_app


@pytest.fixture
def app():
    return create_app("tests")


@pytest.fixture
def client(app):
    return app.test_client()
