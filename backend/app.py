import os
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

from flask import Flask, jsonify, request
from flask_cors import CORS
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import swisseph as swe

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

SIGNS = ["白羊座", "金牛座", "双子座", "巨蟹座", "狮子座", "处女座",
         "天秤座", "天蝎座", "射手座", "摩羯座", "水瓶座", "双鱼座"]
PLANETS = [
    ("太阳", swe.SUN), ("月亮", swe.MOON), ("水星", swe.MERCURY),
    ("金星", swe.VENUS), ("火星", swe.MARS), ("木星", swe.JUPITER),
    ("土星", swe.SATURN), ("天王星", swe.URANUS),
    ("海王星", swe.NEPTUNE), ("冥王星", swe.PLUTO),
    ("北交点", swe.TRUE_NODE)
]
ASPECTS = [(0, "合相"), (60, "六分相"), (90, "四分相"),
           (120, "三分相"), (180, "冲相")]


def sign_position(longitude):
    value = longitude % 360
    sign_index = int(value // 30)
    within = value % 30
    degree = int(within)
    minute_float = (within - degree) * 60
    minute = int(minute_float)
    second = round((minute_float - minute) * 60)
    if second == 60:
        second = 0
        minute += 1
    if minute == 60:
        minute = 0
        degree += 1
    return {
        "sign": SIGNS[sign_index],
        "degree": degree,
        "minute": minute,
        "second": second,
        "longitude": round(value, 6)
    }


def angular_distance(a, b):
    return abs((a - b + 180) % 360 - 180)


def geocode_place(place):
    geolocator = Nominatim(user_agent="astro-studio/0.1 (birth chart calculation)")
    try:
        result = geolocator.geocode(place, exactly_one=True, timeout=12)
    except Exception as exc:
        app.logger.exception("Birthplace geocoding failed")
        raise ValueError(
            "出生地点解析服务暂时不可用（" + type(exc).__name__ +
            "）。请稍后重试，或改用经纬度计算。"
        ) from exc
    if not result:
        raise ValueError("无法识别出生地点。请补充到市/县/乡镇，或直接提供经纬度。")
    return float(result.latitude), float(result.longitude), result.address


def calculate_chart(payload):
    required = ["birth_date", "birth_time", "timezone"]
    missing = [key for key in required if not payload.get(key)]
    if missing:
        raise ValueError("缺少必填字段：" + ", ".join(missing))

    tz_name = str(payload["timezone"])
    try:
        tz = ZoneInfo(tz_name)
    except Exception:
        raise ValueError("无效的时区名称，请使用 IANA 时区，例如 Asia/Shanghai。")

    local_naive = datetime.strptime(
        payload["birth_date"] + " " + payload["birth_time"], "%Y-%m-%d %H:%M"
    )
    local_dt = local_naive.replace(tzinfo=tz)
    utc_dt = local_dt.astimezone(timezone.utc)

    if payload.get("latitude") is not None and payload.get("longitude") is not None:
        lat = float(payload["latitude"])
        lon = float(payload["longitude"])
        place_label = payload.get("place", "用户提供坐标")
    elif payload.get("place"):
        lat, lon, place_label = geocode_place(str(payload["place"]))
    else:
        raise ValueError("请提供出生地点，或同时提供 latitude 和 longitude。")

    if not (-90 <= lat <= 90 and -180 <= lon <= 180):
        raise ValueError("经纬度超出有效范围。")
    detected_tz = TimezoneFinder().timezone_at(lat=lat, lng=lon)
    timezone_warning = []
    if detected_tz and detected_tz != tz_name:
        timezone_warning.append(f"所选时区 {tz_name} 与坐标推算时区 {detected_tz} 不一致，请核对出生地当地时间。")

    # Convert UTC to Julian day. Moshier is explicitly selected so the API
    # never claims to be using Swiss Ephemeris data files when none are installed.
    hour = utc_dt.hour + utc_dt.minute / 60 + utc_dt.second / 3600
    jd_ut = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day, hour, swe.GREG_CAL)
    flags = swe.FLG_MOSEPH | swe.FLG_SPEED

    positions = []
    longitudes = {}
    speeds = {}
    for name, body in PLANETS:
        values, returned_flags = swe.calc_ut(jd_ut, body, flags)
        longitude = values[0] % 360
        speed = values[3]
        longitudes[name] = longitude
        speeds[name] = speed
        item = sign_position(longitude)
        item.update({
            "name": name,
            "retrograde": speed < 0,
            "longitude_speed_per_day": round(speed, 6)
        })
        positions.append(item)

    # South Node is exactly opposite the calculated True North Node.
    south = sign_position((longitudes["北交点"] + 180) % 360)
    south.update({"name": "南交点", "retrograde": speeds["北交点"] < 0, "longitude_speed_per_day": round(speeds["北交点"], 6)})
    positions.append(south)
    longitudes["南交点"] = south["longitude"]
    speeds["南交点"] = speeds["北交点"]

    try:
        cusps, ascmc = swe.houses_ex(jd_ut, lat, lon, b'P')
    except Exception as exc:
        raise ValueError("此纬度下 Placidus 宫位计算失败；请核对地点，或后续选择其他宫位系统。") from exc

    asc = sign_position(ascmc[0])
    mc = sign_position(ascmc[1])
    angles = {
        "上升点": asc,
        "天顶": mc,
        "下降点": sign_position((ascmc[0] + 180) % 360),
        "天底": sign_position((ascmc[1] + 180) % 360)
    }

    houses = []
    for index, cusp in enumerate(cusps, start=1):
        point = sign_position(cusp)
        point["house"] = index
        houses.append(point)

    def house_for(longitude):
        for i in range(12):
            start = float(cusps[i]) % 360
            end = float(cusps[(i + 1) % 12]) % 360
            span = (end - start) % 360
            offset = (longitude - start) % 360
            if offset < span or (i == 11 and abs(offset - span) < 1e-7):
                return i + 1
        return None

    for item in positions:
        item["house"] = house_for(item["longitude"])

    aspects = []
    names = list(longitudes.keys())
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            a_name, b_name = names[i], names[j]
            a_lon, b_lon = longitudes[a_name], longitudes[b_name]
            separation = angular_distance(a_lon, b_lon)
            relative_speed = speeds[a_name] - speeds[b_name]
            for exact, aspect_name in ASPECTS:
                deviation = abs(separation - exact)
                orb_limit = 8 if exact in (0, 180) else 6
                if deviation <= orb_limit:
                    # The absolute aspect deviation is shrinking when applying.
                    signed = (a_lon - b_lon + 180) % 360 - 180
                    derivative = relative_speed * (1 if signed >= 0 else -1)
                    applying = (separation - exact) * derivative < 0
                    aspects.append({
                        "planet_a": a_name, "planet_b": b_name,
                        "aspect": aspect_name, "angle": exact,
                        "orb": round(deviation, 3),
                        "phase": "趋近" if applying else "分离"
                    })
    aspects.sort(key=lambda x: x["orb"])

    return {
        "calculation": {
            "engine": "pyswisseph / Moshier ephemeris",
            "ephemeris_source": "Moshier analytical ephemeris (not Swiss Ephemeris data files)",
            "zodiac": "Tropical",
            "house_system": "Placidus",
            "julian_day_ut": round(jd_ut, 8)
        },
        "birth": {
            "local_datetime": local_dt.isoformat(),
            "utc_datetime": utc_dt.isoformat(),
            "timezone": tz_name,
            "place_resolved": place_label,
            "latitude": round(lat, 6),
            "longitude": round(lon, 6)
        },
        "planets": positions,
        "angles": angles,
        "houses": houses,
        "aspects": aspects,
        "warnings": timezone_warning + [
            "当前使用 Moshier 星历算法，不是 Swiss Ephemeris 星历数据文件；结果应标注数据来源。",
            "使用地名查询时，出生地点文本会发送给 OpenStreetMap Nominatim 地理编码服务；如不希望发送地名，可改为直接提交经纬度。",
            "出生地点若由地名自动解析，坐标可能是城镇中心或地名匹配点，不一定是实际出生地点。",
            "占星解释属于文化与自我探索内容，不构成科学预测。"
        ]
    }


@app.get("/api/health")
def health():
    return jsonify({"ok": True, "service": "astro-studio-api", "engine": "pyswisseph-moshier"})


@app.post("/api/chart")
def chart():
    payload = request.get_json(silent=True) or {}
    try:
        return jsonify({"ok": True, "chart": calculate_chart(payload)})
    except ValueError as exc:
        return jsonify({"ok": False, "error": str(exc)}), 400
    except Exception as exc:
        app.logger.exception("Chart calculation failed")
        # Return a concise diagnostic class so deployment/runtime faults can be
        # identified without exposing a traceback or server internals.
        return jsonify({
            "ok": False,
            "error": "服务器内部计算异常（" + type(exc).__name__ +
                     "）。请把这条提示发给开发人员。"
        }), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    app.run(host="0.0.0.0", port=port)
