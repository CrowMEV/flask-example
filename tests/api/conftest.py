from typing import Iterator
from urllib.parse import urlsplit

import pytest
import sqlalchemy as sa
from utils import tmp_database

from app import create_app
from core.db import Base, db
from core.settings import config


@pytest.fixture(scope="session", autouse=True)
def postgres_temlate(pg_url: str) -> Iterator[str]:
    """
    Creates empty template database with migrations.
    """
    with tmp_database(pg_url, db_name="api_template") as tmp_url:
        engine = sa.create_engine(tmp_url)
        Base.metadata.create_all(bind=engine)
        engine.dispose()
        yield tmp_url


@pytest.fixture
def postgres(postgres_temlate: str) -> Iterator[str]:
    """
    Creates empty temporary database.
    """
    with tmp_database(
        postgres_temlate, suffix="api", template="api_template"
    ) as tmp_url:
        yield tmp_url


@pytest.fixture
def app(postgres: str):
    config.DB_NAME = urlsplit(postgres).path[1:]
    project_app = create_app(config.dsn)
    project_app.config.update(
        {
            "TESTING": True,
        }
    )

    yield project_app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
