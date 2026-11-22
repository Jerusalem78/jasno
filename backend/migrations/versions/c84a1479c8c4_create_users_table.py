"""create users table

Revision ID: c84a1479c8c4
Revises:
Create Date: 2026-11-22 11:50:31.108790

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "c84a1479c8c4"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


lang_enum = sa.Enum("EN", "RU", name="langenum")
level_enum = sa.Enum("A1", "A2", "B1", "B2", "C1", "C2", name="levelenum")


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password_hash", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("native_language", lang_enum, nullable=False),
        sa.Column("learning_language", lang_enum, nullable=False),
        sa.Column("daily_goal_minutes", sa.Integer(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("language_level", level_enum, nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column("email_verified_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )


def downgrade() -> None:
    op.drop_table("users")
    level_enum.drop(op.get_bind(), checkfirst=True)
    lang_enum.drop(op.get_bind(), checkfirst=True)
