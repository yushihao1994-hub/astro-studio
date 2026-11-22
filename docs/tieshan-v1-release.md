# 铁板神数独立研究版 V1

发布日期：2026-11-22  
入口：<https://yushihao1994-hub.github.io/astro-studio/tieshan.html>

## 产品定位

V1 是一个可以独立打开的手机优先网页小程序。它把出生资料、历法转换、四柱基础计算、规则资料展示和 AI 基础解读放在同一条操作流程中。它是后续完整铁板神数系统的可运行底座，不宣称已经完成完整考刻、定数。

## 用户操作流程

1. 打开铁板神数独立页面。
2. 填写称呼（可选）、性别、出生历法、年月日、出生时间和出生地点。
3. 选择省、市、县区、乡镇及村级地址；自然村可手动补充。
4. 点击“计算四柱并建立档案”。
5. 查看历法校验、四柱排定、专业细盘和铁板推演资料。
6. 点击 AI 深度解读，调用后端 DeepSeek 接口生成五个主题的四柱基础文化解读。

## V1 已接入的后端接口

- `GET /api/health`
- `GET /api/tieshan/calendar/months?year=YYYY`
- `POST /api/tieshan/pillars`
- `POST /api/tieshan/analyze`
- `GET /api/tieshan/kunji/glossary`
- `GET /api/tieshan/collections/progress`
- `GET /api/tieshan/collections/<地支>/groups`
- `GET /api/tieshan/collections/<地支>/entries`

## 计算口径与限制

- 年柱以立春交节为界，月柱以十二节交界为界。
- 出生时间按出生地 IANA 时区转换；当前日柱采用当地民用日期零点换日。子初换日等流派差异尚未提供可切换选项。
- 当前使用 pyswisseph Moshier 模式进行太阳黄经计算，不应宣传为使用完整 Swiss Ephemeris 星历文件。
- 五行数量为天干与藏干简单计数，不等于旺衰权重。
- AI 只解释已计算的四柱及其基础派生数据，不自行补算考刻、定数或古籍条文。
- 出生资料保存在当前浏览器 localStorage；V1 尚无账号体系和跨设备云端同步。
- AI 解读依赖 Render 环境变量 `DEEPSEEK_API_KEY`；未配置时会返回明确提示。

## 明确不属于 V1 的功能

完整考刻、定数、六亲数、秘钞密码表、完整卦序推演、清刻足本全量条文索引和逐页扫描图像核验，均不标记为已完成。所有未经底本证据核验的 OCR 候选不得进入正式条文索引。

## 发布核对

- 前端文件：`tieshan.html`
- 后端：`backend/app.py` 及 `backend/tieshan*.py`
- 部署配置：`render.yaml`
- 行政区划数据：`data/china-regions.json` 与 `data/china-villages/`
- AI 服务：`backend/deepseek_client.py`

注意：GitHub Pages 页面部署与 Render API 服务是两项独立部署。页面能打开不代表 Render API 或 DeepSeek 密钥一定可用；上线验收必须分别检查页面、`/api/health`、四柱接口和 AI 接口。
