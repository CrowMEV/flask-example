from typing import Any
from sqlalchemy.orm import Mapped, mapped_column

from core.db import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    password: Mapped[str]

    @property
    def to_dict(self) -> dict[str, Any]:
        return {"email": self.email, "password": self.password, "id": self.id}
