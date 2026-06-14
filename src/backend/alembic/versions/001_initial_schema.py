"""initial schema

Revision ID: 001
Revises:
Create Date: 2026-06-13
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "user_profile",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("height_cm", sa.Numeric(5, 2), nullable=False),
        sa.Column("birth_date", sa.Date(), nullable=False),
        sa.Column("sex", sa.Enum("male", "female", name="sex_enum"), nullable=False),
        sa.Column("activity_factor", sa.Numeric(4, 3), nullable=False),
        sa.Column("target_kcal", sa.Integer(), nullable=False),
        sa.Column("target_protein_g", sa.Numeric(6, 2), nullable=False),
        sa.Column("target_fat_g", sa.Numeric(6, 2), nullable=False),
        sa.Column("target_carbs_g", sa.Numeric(6, 2), nullable=False),
        sa.Column("initial_weight_kg", sa.Numeric(5, 2), nullable=False),
        sa.Column("setup_completed", sa.Boolean(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "food_presets",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(200), nullable=False),
        sa.Column("kcal", sa.Integer(), nullable=False),
        sa.Column("protein_g", sa.Numeric(6, 2), nullable=False),
        sa.Column("fat_g", sa.Numeric(6, 2), nullable=False),
        sa.Column("carbs_g", sa.Numeric(6, 2), nullable=False),
        sa.Column("sort_order", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("idx_food_presets_sort", "food_presets", ["sort_order", "id"])
    op.create_table(
        "meal_logs",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("log_date", sa.Date(), nullable=False),
        sa.Column("name", sa.String(200), nullable=False),
        sa.Column("kcal", sa.Integer(), nullable=False),
        sa.Column("protein_g", sa.Numeric(6, 2), nullable=False),
        sa.Column("fat_g", sa.Numeric(6, 2), nullable=False),
        sa.Column("carbs_g", sa.Numeric(6, 2), nullable=False),
        sa.Column("food_preset_id", sa.BigInteger(), nullable=True),
        sa.Column("logged_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("idx_meal_logs_date", "meal_logs", ["log_date", "logged_at"])
    op.create_table(
        "daily_steps",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("step_date", sa.Date(), nullable=False),
        sa.Column("steps", sa.Integer(), nullable=False),
        sa.Column("source", sa.String(50), nullable=False),
        sa.Column("synced_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("step_date", name="uq_daily_steps_date"),
    )
    op.create_table(
        "weight_logs",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("weight_kg", sa.Numeric(5, 2), nullable=False),
        sa.Column("source", sa.Enum("manual", "shortcuts", name="weight_source_enum"), nullable=False),
        sa.Column("logged_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("idx_weight_logs_logged_at", "weight_logs", ["logged_at"])
    op.create_table(
        "walk_sessions",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("walked_at", sa.DateTime(), nullable=False),
        sa.Column("discovery_note", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("idx_walk_sessions_walked_at", "walk_sessions", ["walked_at"])
    op.create_table(
        "treadmill_logs",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("logged_at", sa.DateTime(), nullable=False),
        sa.Column("minutes", sa.Integer(), nullable=False),
        sa.Column("speed_kmh", sa.Numeric(4, 1), nullable=True),
        sa.Column("incline_pct", sa.Numeric(4, 1), nullable=True),
        sa.Column("machine_kcal", sa.Integer(), nullable=True),
        sa.Column("calculated_kcal", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("idx_treadmill_logs_logged_at", "treadmill_logs", ["logged_at"])
    op.create_table(
        "strength_logs",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("logged_at", sa.DateTime(), nullable=False),
        sa.Column("exercise_code", sa.String(20), nullable=False),
        sa.Column("minutes", sa.Integer(), nullable=False),
        sa.Column("calculated_kcal", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("idx_strength_logs_logged_at", "strength_logs", ["logged_at"])


def downgrade() -> None:
    op.drop_table("strength_logs")
    op.drop_table("treadmill_logs")
    op.drop_table("walk_sessions")
    op.drop_table("weight_logs")
    op.drop_table("daily_steps")
    op.drop_table("meal_logs")
    op.drop_table("food_presets")
    op.drop_table("user_profile")
