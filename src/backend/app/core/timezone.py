from datetime import date, datetime
from zoneinfo import ZoneInfo

from app.core.config import settings

JST = ZoneInfo(settings.tz)


def now_jst() -> datetime:
    return datetime.now(JST)


def today_jst() -> date:
    return now_jst().date()
