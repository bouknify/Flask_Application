import pytest

from model import Model
from app import app as flask_app


@pytest.fixture(scope='module')
def new_model():
    model = Model('8', '390', '190', '3850', '14.0', '76','Europe')
    return model

@pytest.fixture(scope='module')
def app():
    yield flask_app


@pytest.fixture(scope='module')
def test_client(app):
    return app.test_client()