import pytest
from application import create_app


@pytest.fixture
def app(scope="module"):
    """Instance of Main Flask App"""
    app = create_app("testing")
    yield app


# @pytest.fixture
# def client(app):
#     return app.test_client()
