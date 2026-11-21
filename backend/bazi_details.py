"""Traditional Bazi reference annotations; not Iron Plate number generation."""
STEMS = ["甲","乙","丙","丁","戊","己","庚","辛","壬","癸"]
BRANCHES = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
NAYIN = ["海中金","炉中火","大林木","路旁土","剑锋金","山头火","涧下水","城头土","白蜡金","杨柳木","泉中水","屋上土","霹雳火","松柏木","长流水","沙中金","山下火","平地木","壁上土","金箔金","覆灯火","天河水","大驿土","钗钏金","桑柘木","大溪水","沙中土","天上火","石榴木","大海水"]
STAGES = ["长生","沐浴","冠带","临官","帝旺","衰","病","死","墓","绝","胎","养"]
GROWTH_START = {"甲":11,"乙":6,"丙":2,"丁":9,"戊":2,"己":9,"庚":5,"辛":0,"壬":8,"癸":3}
YANG_STEMS = {"甲","丙","戊","庚","壬"}

def _pillar_index(p):
    if isinstance(p.get("index"), int):
        return p["index"] % 60
    stem, branch = p.get("stem"), p.get("branch")
    if stem not in STEMS or branch not in BRANCHES:
        raise ValueError("四柱数据缺少有效干支。")
    for i in range(60):
        if STEMS[i % 10] == stem and BRANCHES[i % 12] == branch:
            return i
    raise ValueError("无效干支组合。")

def _xun_void(index):
    start = (index % 12 - index % 10) % 12
    return [BRANCHES[(start + 10) % 12], BRANCHES[(start + 11) % 12]]

def derive_bazi_details(pillars):
    if not isinstance(pillars, dict) or any(k not in pillars for k in ("year","month","day","hour")):
        raise ValueError("四柱资料不完整。")
    day_stem = pillars["day"].get("stem")
    if day_stem not in GROWTH_START:
        raise ValueError("日干无效，无法计算十二长生。")
    day_void = _xun_void(_pillar_index(pillars["day"]))
    result = {"method":"纳音按六十甲子表；空亡按旬首；十二长生以日干为主，阳干顺行、阴干逆行。","day_master":day_stem,"pillars":{}}
    for key in ("year","month","day","hour"):
        p = pillars[key]
        index = _pillar_index(p)
        branch = p.get("branch")
        direction = 1 if day_stem in YANG_STEMS else -1
        offset = ((BRANCHES.index(branch) - GROWTH_START[day_stem]) * direction) % 12
        own_void = _xun_void(index)
        result["pillars"][key] = {"nayin":NAYIN[index // 2],"xun_void":own_void,"day_xun_void":day_void,"is_day_xun_void":branch in day_void,"day_master_growth_stage":STAGES[offset]}
    result["limitations"] = ["十二长生采用日干为主的常用排法；不同门派可能采用年干或其他取法。","空亡同时展示各柱自身旬空与日柱旬空，不直接解释为吉凶事件。","纳音、空亡、十二长生属于四柱辅助标注，不是铁板神数密码数或条文匹配。"]
    return result
