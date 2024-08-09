import pytest

from app import app as project_app


@pytest.fixture
def app():

    project_app.config.update(
        {
            "TESTING": True,
        }
    )

    # other setup can go here

    yield project_app

    # clean up / reset resources here


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
