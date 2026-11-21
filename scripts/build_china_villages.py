#!/usr/bin/env python3
"""Build province-scoped five-level administrative village data from 2023 NBS snapshot.\nSource snapshot: https://github.com/YangH9/China_area (MIT)."""
import csv, io, json, os, urllib.request
from collections import defaultdict

BASE = "https://raw.githubusercontent.com/YangH9/China_area/master/dist"
FILES = {k: f"{BASE}/{k}.csv" for k in ("provinces", "cities", "areas", "streets", "villages")}

def read_csv(kind):
    req = urllib.request.Request(FILES[kind], headers={"User-Agent": "astro-studio-village-builder"})
    with urllib.request.urlopen(req, timeout=120) as response:
        raw = response.read()
    for enc in ("utf-8-sig", "utf-8", "gb18030"):
        try:
            return list(csv.DictReader(io.StringIO(raw.decode(enc))))
        except UnicodeDecodeError:
            pass
    raise RuntimeError(f"Cannot decode {kind}.csv")

def main():
    provinces, cities, areas, streets, villages = (read_csv(k) for k in FILES)
    def index(rows):
        return {str(x["code"]): x["name"] for x in rows}
    pn, cn, an, tn = map(index, (provinces, cities, areas, streets))
    grouped = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(list))))
    for v in villages:
        pc, cc, ac, tc = (str(v[k]) for k in ("provinceCode", "cityCode", "areaCode", "streetCode"))
        if pc in pn and cc in cn and ac in an and tc in tn:
            grouped[pc][cn[cc]][an[ac]][tn[tc]].append(v["name"])
    out = "data/china-villages"
    os.makedirs(out, exist_ok=True)
    manifest = {"version":"2023-06-30","source":"国家统计局《2023年统计用区划和城乡划分代码》；YangH9/China_area","provinces":{}}
    for pc, citymap in grouped.items():
        pname = pn[pc]
        manifest["provinces"][pname] = pc
        payload = {city:{area:{town:sorted(set(names)) for town,names in towns.items()} for area,towns in areas.items()} for city,areas in citymap.items()}
        with open(f"{out}/{pc}.json","w",encoding="utf-8") as f:
            json.dump(payload,f,ensure_ascii=False,separators=(",",":"))
    with open(f"{out}/manifest.json","w",encoding="utf-8") as f:
        json.dump(manifest,f,ensure_ascii=False,separators=(",",":"))
    print(f"Built {len(grouped)} province shards, {sum(len(v) for v in grouped.values())} province-city groups")

if __name__ == "__main__":
    main()
