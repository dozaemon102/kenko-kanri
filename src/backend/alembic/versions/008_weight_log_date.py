"""weight_logs: one row per log_date (JST calendar day)

Revision ID: 008
Revises: 007
Create Date: 2026-06-16
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "008"
down_revision: Union[str, None] = "007"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table("weight_logs")
    op.create_table(
        "weight_logs",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("log_date", sa.Date(), nullable=False),
        sa.Column("weight_kg", sa.Numeric(5, 2), nullable=False),
        sa.Column("bmi", sa.Numeric(4, 1), nullable=True),
        sa.Column("lbm_kg", sa.Numeric(5, 2), nullable=True),
        sa.Column("body_fat_pct", sa.Numeric(4, 1), nullable=True),
        sa.Column(
            "source",
            sa.Enum("manual", "shortcuts", name="weight_source_enum"),
            nullable=False,
        ),
        sa.Column("logged_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("log_date", name="uq_weight_logs_log_date"),
    )
    op.create_index("ix_weight_logs_log_date", "weight_logs", ["log_date"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_weight_logs_log_date", table_name="weight_logs")
    op.drop_table("weight_logs")
    op.create_table(
        "weight_logs",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("weight_kg", sa.Numeric(5, 2), nullable=False),
        sa.Column("bmi", sa.Numeric(4, 1), nullable=True),
        sa.Column("lbm_kg", sa.Numeric(5, 2), nullable=True),
        sa.Column("body_fat_pct", sa.Numeric(4, 1), nullable=True),
        sa.Column(
            "source",
            sa.Enum("manual", "shortcuts", name="weight_source_enum"),
            nullable=False,
        ),
        sa.Column("logged_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_weight_logs_logged_at", "weight_logs", ["logged_at"], unique=False)
