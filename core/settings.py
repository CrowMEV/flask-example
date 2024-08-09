from pathlib import Path

from pydantic import computed_field
from pydantic_settings import BaseSettings


class Config(BaseSettings):

    ROOT_DIR: Path = Path(__file__).parent.parent.resolve()

    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_NAME: str = "db"
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432

    @computed_field
    def dsn(self) -> str:
        return (
            f"postgresql://{self.DB_USER}:"
            f"{self.DB_PASSWORD}@{self.DB_HOST}:"
            f"{self.DB_PORT}/{self.DB_NAME}"
        )


config = Config()
