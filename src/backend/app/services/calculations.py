STRENGTH_TEMPLATES = [
    {"code": "chest", "name": "胸", "met": 6.0},
    {"code": "back", "name": "背中", "met": 6.0},
    {"code": "legs", "name": "脚", "met": 6.5},
    {"code": "shoulders", "name": "肩", "met": 5.5},
    {"code": "arms", "name": "腕", "met": 5.0},
    {"code": "full", "name": "全身", "met": 6.0},
]

STRENGTH_MET = {t["code"]: t["met"] for t in STRENGTH_TEMPLATES}


def walk_burn_kcal_simple(steps: int, weight_kg: float) -> int:
    return int(steps * weight_kg * 0.0005)


def walking_met(speed_kmh: float) -> float:
    if speed_kmh < 3.2:
        return 2.5
    if speed_kmh < 4.8:
        return 3.5
    if speed_kmh < 6.4:
        return 4.3
    return 5.0


def walk_burn_kcal_met(steps: int, weight_kg: float, stride_cm: float, speed_kmh: float) -> int:
    distance_km = steps * (stride_cm / 100) / 1000
    hours = distance_km / speed_kmh
    return int(walking_met(speed_kmh) * weight_kg * hours)


def walk_burn_kcal(
    steps: int,
    weight_kg: float,
    *,
    stride_cm: float | None = None,
    speed_kmh: float | None = None,
) -> tuple[int, str]:
    if (
        steps > 0
        and stride_cm is not None
        and speed_kmh is not None
        and stride_cm > 0
        and speed_kmh > 0
    ):
        return walk_burn_kcal_met(steps, weight_kg, stride_cm, speed_kmh), "met"
    return walk_burn_kcal_simple(steps, weight_kg), "simple"


def katch_mcardle_bmr(lbm_kg: float) -> int:
    return int(370 + 21.6 * lbm_kg)


def tef_kcal(intake_kcal: int, tef_rate: float) -> int:
    return int(intake_kcal * tef_rate)


def treadmill_met(speed_kmh: float | None) -> float:
    if speed_kmh is None:
        return 9.0
    if speed_kmh < 6:
        return 8.0
    if speed_kmh <= 10:
        return 9.0
    return 10.0


def treadmill_burn_kcal(
    minutes: int,
    weight_kg: float,
    speed_kmh: float | None = None,
    machine_kcal: int | None = None,
) -> int:
    if machine_kcal is not None:
        return machine_kcal
    met = treadmill_met(speed_kmh)
    return int(met * weight_kg * (minutes / 60))


def strength_burn_kcal(exercise_code: str, minutes: int, weight_kg: float) -> int:
    met = STRENGTH_MET.get(exercise_code, 6.0)
    return int(met * weight_kg * (minutes / 60))
