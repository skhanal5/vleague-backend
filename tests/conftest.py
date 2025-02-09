import pytest
from flask import Flask
from flask.testing import FlaskClient

from flask_refapp.app import create_app


@pytest.fixture()
def app():
    app = create_app({"TESTING": True})
    yield app


@pytest.fixture()
def client(app: Flask) -> FlaskClient:
    return app.test_client()
