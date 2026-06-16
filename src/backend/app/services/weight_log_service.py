from datetime import date
from decimal import Decimal

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.timezone import now_jst
from app.models.entities import WeightLog


def _to_decimal(value: float | None) -> Decimal | None:
    if value is None:
        return None
    return Decimal(str(value))


def upsert_weight_day(
    db: Session,
    log_date: date,
    source: str,
    *,
    weight_kg: float | None = None,
    bmi: float | None = None,
    lbm_kg: float | None = None,
    body_fat_pct: float | None = None,
    default_weight_kg: float | None = None,
) -> WeightLog:
    """Upsert one row per log_date; only provided fields are updated."""
    now = now_jst()
    row = db.scalar(select(WeightLog).where(WeightLog.log_date == log_date))
    if row is None:
        resolved_weight = weight_kg if weight_kg is not None else default_weight_kg
        if resolved_weight is None:
            raise ValueError("weight_kg or default_weight_kg required for new weight log")
        row = WeightLog(
            log_date=log_date,
            weight_kg=_to_decimal(resolved_weight),
            bmi=_to_decimal(bmi),
            lbm_kg=_to_decimal(lbm_kg),
            body_fat_pct=_to_decimal(body_fat_pct),
            source=source,
            logged_at=now,
        )
        db.add(row)
        return row

    row.logged_at = now
    row.source = source
    if weight_kg is not None:
        row.weight_kg = _to_decimal(weight_kg)
    if bmi is not None:
        row.bmi = _to_decimal(bmi)
    if lbm_kg is not None:
        row.lbm_kg = _to_decimal(lbm_kg)
    if body_fat_pct is not None:
        row.body_fat_pct = _to_decimal(body_fat_pct)
    return row
