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


def upgrade() -> None:
    op.add_column("treadmill_logs", sa.Column("log_date", sa.Date(), nullable=True))
    op.add_column("strength_logs", sa.Column("log_date", sa.Date(), nullable=True))
    op.execute("UPDATE treadmill_logs SET log_date = DATE(logged_at)")
    op.execute("UPDATE strength_logs SET log_date = DATE(logged_at)")
    op.alter_column("treadmill_logs", "log_date", nullable=False)
    op.alter_column("strength_logs", "log_date", nullable=False)
    op.create_index("ix_treadmill_logs_log_date", "treadmill_logs", ["log_date"], unique=False)
    op.create_index("ix_strength_logs_log_date", "strength_logs", ["log_date"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_strength_logs_log_date", table_name="strength_logs")
    op.drop_index("ix_treadmill_logs_log_date", table_name="treadmill_logs")
    op.drop_column("strength_logs", "log_date")
    op.drop_column("treadmill_logs", "log_date")
