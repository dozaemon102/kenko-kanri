"""drop walk params from user_profile (Health sync daily_steps only)

Revision ID: 007
Revises: 006
Create Date: 2026-06-15
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "007"
down_revision: Union[str, None] = "006"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column("user_profile", "walking_speed_kmh")
    op.drop_column("user_profile", "stride_cm")


def downgrade() -> None:
    op.add_column(
        "user_profile",
        sa.Column("walking_speed_kmh", sa.Numeric(4, 2), nullable=True),
    )
    op.add_column(
        "user_profile",
        sa.Column("stride_cm", sa.Numeric(5, 2), nullable=True),
    )
