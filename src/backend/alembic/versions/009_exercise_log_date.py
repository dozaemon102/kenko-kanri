"""treadmill_logs / strength_logs: add log_date (JST calendar day)

Revision ID: 009
Revises: 008
Create Date: 2026-06-16
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "009"
down_revision: Union[str, None] = "008"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def _column_names(table: str) -> set[str]:
    insp = sa.inspect(op.get_bind())
    return {c["name"] for c in insp.get_columns(table)}


def _index_names(table: str) -> set[str]:
    insp = sa.inspect(op.get_bind())
    return {ix["name"] for ix in insp.get_indexes(table)}


def upgrade() -> None:
    if "log_date" not in _column_names("treadmill_logs"):
        op.add_column("treadmill_logs", sa.Column("log_date", sa.Date(), nullable=True))
    if "log_date" not in _column_names("strength_logs"):
        op.add_column("strength_logs", sa.Column("log_date", sa.Date(), nullable=True))

    op.execute("UPDATE treadmill_logs SET log_date = DATE(logged_at) WHERE log_date IS NULL")
    op.execute("UPDATE strength_logs SET log_date = DATE(logged_at) WHERE log_date IS NULL")

    op.alter_column(
        "treadmill_logs",
        "log_date",
        existing_type=sa.Date(),
        nullable=False,
    )
    op.alter_column(
        "strength_logs",
        "log_date",
        existing_type=sa.Date(),
        nullable=False,
    )

    if "ix_treadmill_logs_log_date" not in _index_names("treadmill_logs"):
        op.create_index("ix_treadmill_logs_log_date", "treadmill_logs", ["log_date"], unique=False)
    if "ix_strength_logs_log_date" not in _index_names("strength_logs"):
        op.create_index("ix_strength_logs_log_date", "strength_logs", ["log_date"], unique=False)


def downgrade() -> None:
    if "ix_strength_logs_log_date" in _index_names("strength_logs"):
        op.drop_index("ix_strength_logs_log_date", table_name="strength_logs")
    if "ix_treadmill_logs_log_date" in _index_names("treadmill_logs"):
        op.drop_index("ix_treadmill_logs_log_date", table_name="treadmill_logs")
    if "log_date" in _column_names("strength_logs"):
        op.drop_column("strength_logs", "log_date")
    if "log_date" in _column_names("treadmill_logs"):
        op.drop_column("treadmill_logs", "log_date")
