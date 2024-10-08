"""User roles

Revision ID: 4519e7feb5b2
Revises: ac7d22ca002b
Create Date: 2024-08-09 14:39:20.495555

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

from models.user import Role

# revision identifiers, used by Alembic.
revision: str = "4519e7feb5b2"
down_revision: Union[str, None] = "ac7d22ca002b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

role = postgresql.ENUM(Role, name="role")


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    role.create(op.get_bind(), checkfirst=True)
    op.add_column(
        "users",
        sa.Column(
            "role",
            role,
            server_default="USER",
            nullable=False,
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "role")

    role.drop(op.get_bind())
    # ### end Alembic commands ###
