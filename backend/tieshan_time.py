"""Time subdivision for the documented eight-ke-per-double-hour convention.

This calculates a clock-time bucket only. It is NOT historical time correction,
traditional birth-time verification (考刻), or a complete Iron Plate number.
"""

BRANCHES = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]


def _format_clock(total_minutes):
    value = total_minutes % (24 * 60)
    return f"{value // 60:02d}:{value % 60:02d}"


def derive_eight_ke(birth_time, hour_branch):
    """Split a two-hour branch period into eight 15-minute clock-time segments."""
    if not isinstance(birth_time, str) or len(birth_time) != 5 or birth_time[2] != ":":
        raise ValueError("出生时间必须使用 HH:MM 格式。")
    try:
        hour, minute = (int(x) for x in birth_time.split(":"))
    except (TypeError, ValueError) as exc:
        raise ValueError("出生时间必须使用 HH:MM 格式。") from exc
    if not (0 <= hour <= 23 and 0 <= minute <= 59):
        raise ValueError("出生时间超出有效范围。")
    if hour_branch not in BRANCHES:
        raise ValueError("出生时支必须是子至亥中的一个。")

    clock_minutes = hour * 60 + minute
    elapsed_from_zi_start = (clock_minutes - 23 * 60) % (24 * 60)
    branch_index = elapsed_from_zi_start // 120
    within_branch = elapsed_from_zi_start % 120
    calculated_branch = BRANCHES[int(branch_index)]
    if calculated_branch != hour_branch:
        raise ValueError(
            f"出生时间 {birth_time} 按当地钟表时间对应{calculated_branch}时，"
            f"与已排时柱地支{hour_branch}不一致。"
        )

    ke_index = int(within_branch // 15) + 1
    start = clock_minutes - (minute % 15)
    return {
        "hour_branch": calculated_branch,
        "ke_number": ke_index,
        "ke_label": f"{calculated_branch}时第{ke_index}刻",
        "within_branch_minute": int(within_branch),
        "segment_start": _format_clock(start),
        "segment_end": _format_clock(start + 15),
        "segment_minutes": 15,
        "basis": "出生地当地钟表时间；每个时辰120分钟，分为8段，每段15分钟",
        "source_note": "康节说易全书·铁板神数，乾集开篇关于每时八刻、每刻十五分的说明",
        "status": "clock_time_partition_only",
        "limitations": [
            "这是将钟表时间按15分钟切段，不是传统意义上的考刻定盘。",
            "尚未进行经度真太阳时、均时差和历史地方时修正。",
            "尚未核实不同版本对刻初、刻正及子时跨日的细分口径。",
            "不得仅凭此刻数推定人生条文或最终铁板神数。",
        ],
    }
