"""Transparent Four Pillars foundation for the Iron Plate mini app.

This module calculates civil-time Ganzhi pillars from Gregorian birth data.
It deliberately does not claim to implement a complete Iron Plate Shen Shu
numbering/verification lineage.
"""
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import math

import swisseph as swe

STEMS = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
BRANCHES = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
JIE_TERMS = [
    (315, "立春", 0), (345, "惊蛰", 1), (15, "清明", 2),
    (45, "立夏", 3), (75, "芒种", 4), (105, "小暑", 5),
    (135, "立秋", 6), (165, "白露", 7), (195, "寒露", 8),
    (225, "立冬", 9), (255, "大雪", 10), (285, "小寒", 11),
]
YEAR_START = 1984  # 1984 is a 甲子 year.


def _sun_lon(jd_ut):
    values, _ = swe.calc_ut(jd_ut, swe.SUN, swe.FLG_MOSEPH | swe.FLG_SPEED)
    return values[0] % 360


def _signed_angle(value, target):
    return (value - target + 180.0) % 360.0 - 180.0


def _last_solar_crossing(target, jd_end, lookback_days):
    """Find the latest increasing solar-longitude crossing before jd_end."""
    step = 0.25
    left = jd_end - lookback_days
    previous_jd = left
    previous_delta = _signed_angle(_sun_lon(previous_jd), target)
    jd = left + step
    while jd <= jd_end + 1e-9:
        current_delta = _signed_angle(_sun_lon(jd), target)
        if previous_delta < 0 <= current_delta:
            lo, hi = previous_jd, jd
            for _ in range(42):
                mid = (lo + hi) / 2
                delta = _signed_angle(_sun_lon(mid), target)
                if delta >= 0:
                    hi = mid
                else:
                    lo = mid
            return (lo + hi) / 2
        previous_jd, previous_delta = jd, current_delta
        jd += step
    return None


def _ganzhi(index):
    value = index % 60
    return {
        "index": value,
        "stem": STEMS[value % 10],
        "branch": BRANCHES[value % 12],
        "name": STEMS[value % 10] + BRANCHES[value % 12],
    }


def calculate_tieshan_pillars(payload, latitude, longitude, place_label, timezone_name):
    if str(payload.get("calendar", "solar")).lower() != "solar":
        raise ValueError("当前版本暂只支持公历出生日期；农历转公历模块尚未接入，请先切换为公历。")

    birth_date = str(payload.get("birth_date") or "").strip()
    birth_time = str(payload.get("birth_time") or "").strip()
    if not birth_date or not birth_time:
        raise ValueError("计算四柱必须提供公历出生日期和出生时间。")
    try:
        local_naive = datetime.strptime(birth_date + " " + birth_time, "%Y-%m-%d %H:%M")
    except ValueError as exc:
        raise ValueError("出生日期或时间格式不正确。") from exc

    try:
        tz = ZoneInfo(timezone_name)
    except Exception as exc:
        raise ValueError("出生地点对应的时区无效，请核对出生地点。") from exc

    valid = []
    for fold in (0, 1):
        candidate = local_naive.replace(tzinfo=tz, fold=fold)
        back = candidate.astimezone(timezone.utc).astimezone(tz).replace(tzinfo=None)
        if back == local_naive:
            valid.append(candidate)
    if not valid:
        raise ValueError("该出生地的当地钟表时间处于夏令时跳时区间，请核对出生记录。")
    offsets = {x.utcoffset() for x in valid}
    warnings = []
    if len(offsets) > 1:
        local_dt = valid[0]
        warnings.append("出生时间处于夏令时重复时段，暂按第一次出现的当地时间计算，请核对记录。")
    else:
        local_dt = valid[0]

    utc_dt = local_dt.astimezone(timezone.utc)
    decimal_hour = utc_dt.hour + utc_dt.minute / 60 + utc_dt.second / 3600
    jd_ut = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day, decimal_hour, swe.GREG_CAL)

    # Year pillar changes at the astronomical Li Chun (solar longitude 315°).
    lichun_jd = _last_solar_crossing(315, jd_ut, 370)
    if lichun_jd is None:
        raise ValueError("未能定位出生年份的立春交节点，暂不能可靠计算年柱。")
    effective_year = local_dt.year if jd_ut >= lichun_jd else local_dt.year - 1
    year_index = (effective_year - YEAR_START) % 60
    year_pillar = _ganzhi(year_index)

    # Month pillar changes at the twelve Jie (节), not at Gregorian month boundaries.
    candidates = []
    for longitude_target, term_name, month_index in JIE_TERMS:
        crossing = _last_solar_crossing(longitude_target, jd_ut, 40)
        if crossing is not None:
            candidates.append((crossing, term_name, month_index))
    if not candidates:
        raise ValueError("未能定位出生时刻之前的节气交界，暂不能可靠计算月柱。")
    month_boundary_jd, month_term, month_index = max(candidates, key=lambda item: item[0])
    # Five-tiger month-stem rule.
    first_month_stem_by_year_stem = [2, 4, 6, 8, 0, 2, 4, 6, 8, 0]
    month_stem = (first_month_stem_by_year_stem[year_index % 10] + month_index) % 10
    month_branch = (2 + month_index) % 12
    month_pillar = {
        "stem": STEMS[month_stem], "branch": BRANCHES[month_branch],
        "name": STEMS[month_stem] + BRANCHES[month_branch],
        "month_index_from_yin": month_index,
        "last_jie": month_term,
    }

    # Day pillar uses the local civil date and a midnight day-boundary convention.
    local_jdn = int(math.floor(swe.julday(local_dt.year, local_dt.month, local_dt.day, 12.0, swe.GREG_CAL) + 0.5))
    day_pillar = _ganzhi(local_jdn + 49)

    # Two-hour branch; 23:00-00:59 is 子时. Day stem uses the midnight convention above.
    hour = local_dt.hour
    minute = local_dt.minute
    hour_branch_index = ((hour + 1) // 2) % 12
    first_hour_stem_by_day_stem = [0, 2, 4, 6, 8, 0, 2, 4, 6, 8]
    hour_stem = (first_hour_stem_by_day_stem[day_pillar["index"] % 10] + hour_branch_index) % 10
    hour_pillar = {
        "stem": STEMS[hour_stem], "branch": BRANCHES[hour_branch_index],
        "name": STEMS[hour_stem] + BRANCHES[hour_branch_index],
        "branch_period": "23:00–00:59" if hour_branch_index == 0 else
            f"{(hour_branch_index * 2 - 1):02d}:00–{(hour_branch_index * 2 + 1):02d}:59",
    }

    if hour == 23:
        warnings.append("出生时间在23点子时段。部分传统流派采用子初换日，本版日柱暂按当地民用日期零点换日；需在后续流派设置中明确切换。")
    if not payload.get("place"):
        warnings.append("出生地点未填写，当前时区/经度来源可能不足；时柱暂按提交的当地钟表时间计算。")

    return {
        "ok": True,
        "engine": "pyswisseph Moshier solar longitude + Ganzhi cycle rules",
        "birth": {
            "local_datetime": local_dt.isoformat(timespec="minutes"),
            "utc_datetime": utc_dt.isoformat(timespec="minutes"),
            "timezone": timezone_name,
            "place_resolved": place_label,
            "latitude": round(float(latitude), 6),
            "longitude": round(float(longitude), 6),
        },
        "pillars": {
            "year": year_pillar,
            "month": month_pillar,
            "day": day_pillar,
            "hour": hour_pillar,
        },
        "solar_term_boundary": {
            "year_boundary": "立春",
            "month_boundary": month_term,
            "month_boundary_julian_day_ut": round(month_boundary_jd, 8),
        },
        "method": [
            "年柱以出生时刻是否已过天文立春为界。",
            "月柱以十二节的太阳黄经交界为界，不按公历月份直接切换。",
            "日柱按出生地当地民用日期计算，换日点暂采用00:00。",
            "时柱按当地民用钟表时间划分十二时辰；尚未校正真太阳时。",
        ],
        "warnings": warnings + [
            "本接口只计算四柱基础数据，不等于完整铁板神数定数算法。",
            "真太阳时校正、子初换日流派差异、农历转换和考刻规则将在后续版本中单独实现并标明。",
        ],
    }
