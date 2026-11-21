"""Chinese lunar/solar calendar conversion helpers.

Uses 6tail/lunar-python (MIT) for validated Chinese calendar dates.
"""
from datetime import date
from lunar_python import Lunar, LunarYear


MIN_YEAR = 1900
MAX_YEAR = 2100


def _validate_year(year):
    try:
        value = int(year)
    except (TypeError, ValueError) as exc:
        raise ValueError("出生年份必须是有效数字。") from exc
    if not MIN_YEAR <= value <= MAX_YEAR:
        raise ValueError(f"目前历法资料支持范围为{MIN_YEAR}年至{MAX_YEAR}年。")
    return value


def lunar_month_options(year):
    year = _validate_year(year)
    result = []
    for item in LunarYear.fromYear(year).getMonths():
        month_number = int(item.getMonth())
        is_leap = month_number < 0
        month = abs(month_number)
        result.append({
            "month": month,
            "is_leap": is_leap,
            "value": str(month_number),
            "days": int(item.getDayCount()),
            "label": ("闰" if is_leap else "") + ("正" if month == 1 else "腊" if month == 12 else str(month)) + "月",
        })
    return result


def lunar_to_solar(year, month, day):
    year = _validate_year(year)
    try:
        month = int(month)
        day = int(day)
        if month == 0 or not -12 <= month <= 12:
            raise ValueError("农历月份无效。")
        month_data = next((x for x in lunar_month_options(year) if int(x["value"]) == month), None)
        if month_data is None:
            raise ValueError("该农历年份不存在所选月份或闰月。")
        if not 1 <= day <= month_data["days"]:
            raise ValueError(f"所选农历月份只有{month_data['days']}天，请重新选择日期。")
        solar = Lunar.fromYmd(year, month, day).getSolar()
        result = date(int(solar.getYear()), int(solar.getMonth()), int(solar.getDay()))
        return result
    except ValueError:
        raise
    except Exception as exc:
        raise ValueError("农历日期无效，请核对年份、月份、闰月和日期。") from exc


def solar_to_lunar(value):
    if isinstance(value, str):
        try:
            value = date.fromisoformat(value)
        except ValueError as exc:
            raise ValueError("公历日期格式应为YYYY-MM-DD。") from exc
    _validate_year(value.year)
    lunar = Lunar.fromDate(value)
    month = int(lunar.getMonth())
    return {
        "year": int(lunar.getYear()),
        "month": abs(month),
        "month_value": month,
        "day": int(lunar.getDay()),
        "is_leap": month < 0,
    }
