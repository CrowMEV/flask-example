from enum import Enum
from typing import Any

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from core.db import Base


class Role(Enum):
    USER = "user"
    ADMIN = "admin"


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    password: Mapped[str]
    role: Mapped[Role] = mapped_column(server_default=Role.USER.name)

    @property
    def to_dict(self) -> dict[str, Any]:
        return {"email": self.email, "password": self.password, "id": self.id}
