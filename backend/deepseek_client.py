import json
import os
import re

import requests


class DeepSeekNotConfigured(Exception):
    pass


class DeepSeekError(Exception):
    pass


def _extract_json_object(content):
    """Accept plain JSON, fenced JSON, or explanatory text surrounding one JSON object."""
    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, dict) and isinstance(item.get("text"), str):
                parts.append(item["text"])
        content = "\n".join(parts)
    if not isinstance(content, str) or not content.strip():
        raise DeepSeekError("DeepSeek 返回了空内容。")

    text = content.strip()
    text = re.sub(r"^\s*```(?:json)?\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*```\s*$", "", text)
    # Some reasoning-capable responses include a think block before the final answer.
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.IGNORECASE | re.DOTALL).strip()

    try:
        value = json.loads(text)
    except json.JSONDecodeError:
        decoder = json.JSONDecoder()
        start = text.find("{")
        if start < 0:
            raise DeepSeekError("DeepSeek 返回内容中没有 JSON 对象。")
        try:
            value, _ = decoder.raw_decode(text[start:])
        except json.JSONDecodeError as exc:
            raise DeepSeekError("DeepSeek 返回的 JSON 格式不完整。") from exc

    if not isinstance(value, dict):
        raise DeepSeekError("DeepSeek 返回的内容不是 JSON 对象。")
    return value


def analyze_with_deepseek(topic, evidence):
    api_key = os.environ.get("DEEPSEEK_API_KEY", "").strip()
    if not api_key:
        raise DeepSeekNotConfigured("DeepSeek API 尚未配置，请在 Render 环境变量中设置 DEEPSEEK_API_KEY。")

    base_url = os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com").rstrip("/")
    model = os.environ.get("DEEPSEEK_MODEL", "deepseek-flash")
    endpoint = base_url + "/chat/completions"

    topic_names = {
        "personality": "性格与个人优势",
        "relationship": "恋爱、伴侣与婚姻关系",
        "finance": "赚钱方式、财务优势与风险",
        "career": "事业方向与职业发展",
        "trends": "近期趋势与阶段性提醒"
    }
    topic_name = topic_names.get(topic)
    if not topic_name:
        raise DeepSeekError("不支持的分析主题。")

    topic_guides = {
        "personality": "重点分析外在给人的感觉、内在需求、思考沟通方式、行动驱动力、优势与容易卡住的地方。结合上升点、太阳、月亮、水星及其宫位和紧密相位；不要把性格写成单一标签。",
        "relationship": "重点分析情感需求、表达爱与冲突的方式、恋爱和长期伴侣关系的不同需求、亲密关系中的边界。优先结合月亮、金星、火星及第5/7/8宫与宫主星证据；不得断言何时结婚、复合或对方身份。",
        "finance": "重点区分赚钱能力/收入渠道（第2宫）、共同资金与风险（第8宫）、事业变现（第10宫）、收益网络（第11宫）。分析机会、稳定性、消费风险和可执行的财务习惯；不能承诺发财或给投资指令。",
        "career": "重点分析职业动力、适合发挥的工作环境、技能表达、日常工作方式、长期发展与团队收益。区分第6宫日常工作、第10宫事业方向、第2宫收入、第11宫团队与收益。",
        "trends": "严格区分过去30天回顾与未来30天提醒。只解释输入的行运时间窗口和触发点，不把相位翻译成必然事件；给出可观察的主题和现实核查建议。"
    }
    system_prompt = (
        "你是严谨的西方占星研究报告撰写者。你只能解释用户提供的结构化星盘证据，"
        "不得自行计算星体位置、宫位、相位或行运，不得补造缺失数据。"
        "占星属于文化与自我探索框架，不是科学验证的命运预测。"
        "若证据不足或相互矛盾，必须明确说明不确定，不得用确定语气预测事件。"
        "输出必须是合法 json 对象，且只能输出 JSON，不得添加 Markdown 代码围栏或解释文字。"
        "必须严格使用以下结构：{\"summary\":\"总体结论\",\"sections\":[{\"title\":\"主题\",\"conclusion\":\"结论\",\"reasoning\":\"依据与解释\",\"evidence_ids\":[\"输入中真实存在的证据id\"],\"advice\":\"建议\"}],\"limitations\":[]}。"
        "sections 必须有 3 至 5 项；每项必须包含 title、conclusion、reasoning、evidence_ids、advice。"
        "evidence_ids 只能使用输入证据中真实存在的 id；每项至少引用一个直接相关的证据。"
        "每一项必须讨论不同问题，不得换词重复同一结论。reasoning 要说明具体证据如何支持结论，"
        "并指出可能的另一面或限制；advice 必须是普通人能执行的具体动作，避免空泛鼓励。"
        "用自然、具体、易懂的简体中文，面向不懂占星术语的付费客户；必要时用生活语言解释术语。"
        "不要虚构用户经历、年龄、职业、伴侣状况、收入或现实事件。"
        "区分盘面倾向、现实表现和建议，不承诺发财、结婚、复合或具体事件。"
    )
    user_payload = {
        "analysis_topic": topic_name,
        "topic_specific_method": topic_guides[topic],
        "evidence": evidence,
        "required_style": "输出像认真阅读个人星盘后的顾问报告，而不是通用星座文章。每一条都要有不同的具体信息、可核验依据和行动建议。"
    }
    try:
        response = requests.post(
            endpoint,
            headers={
                "Authorization": "Bearer " + api_key,
                "Content-Type": "application/json"
            },
            json={
                "model": model,
                "thinking": {"type": "disabled"},
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": json.dumps(user_payload, ensure_ascii=False)}
                ],
                "response_format": {"type": "json_object"},
                "temperature": 0.4,
                "max_tokens": 6000,
                "stream": False
            },
            timeout=(10, 90)
        )
        if response.status_code >= 400:
            raise DeepSeekError("DeepSeek HTTP " + str(response.status_code))
        body = response.json()
        choices = body.get("choices") or []
        if not choices or not isinstance(choices[0], dict):
            raise DeepSeekError("DeepSeek 响应缺少 choices。")
        choice = choices[0]
        finish_reason = choice.get("finish_reason")
        message = choice.get("message") or {}
        content = message.get("content")
        if content is None and isinstance(message.get("reasoning_content"), str):
            content = message["reasoning_content"]
        if not isinstance(content, str) or not content.strip():
            content_length = len(content) if isinstance(content, str) else 0
            raise DeepSeekError(
                "DeepSeek JSON 输出为空（finish_reason=" + str(finish_reason) +
                "，content_length=" + str(content_length) + "）。"
            )
        if finish_reason == "length":
            raise DeepSeekError("DeepSeek 输出达到长度上限，JSON 可能被截断。")
        if finish_reason in ("content_filter", "insufficient_system_resource", "aborted"):
            raise DeepSeekError("DeepSeek 生成中断（finish_reason=" + str(finish_reason) + "）。")
        result = _extract_json_object(content)
        if not isinstance(result.get("sections"), list):
            raise DeepSeekError("DeepSeek 返回的数据结构不符合要求。")
        if not isinstance(result.get("summary"), str):
            raise DeepSeekError("DeepSeek 返回内容缺少摘要。")
        return result
    except DeepSeekError:
        raise
    except requests.Timeout as exc:
        raise DeepSeekError("DeepSeek 请求超时。") from exc
    except requests.RequestException as exc:
        raise DeepSeekError("DeepSeek 网络请求失败。") from exc
    except (ValueError, KeyError, TypeError, IndexError) as exc:
        raise DeepSeekError("DeepSeek 响应结构无法解析。") from exc


def generate_full_report(evidence):
    """Generate a distinct, evidence-audited full natal report."""
    api_key = os.environ.get("DEEPSEEK_API_KEY", "").strip()
    if not api_key:
        raise DeepSeekNotConfigured("DeepSeek API 尚未配置，请在 Render 环境变量中设置 DEEPSEEK_API_KEY。")
    base_url = os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com").rstrip("/")
    model = os.environ.get("DEEPSEEK_MODEL", "deepseek-flash")
    system_prompt = (
        "你是一位严谨的西方本命星盘研究报告撰写者。你只能解释用户提供的结构化证据，"
        "不得自行计算星体位置、宫位、相位或行运，不得补造缺失数据。"
        "占星是文化与自我探索框架，不是科学验证的命运预测。"
        "请生成一份真正完整、彼此有区分的个人报告，不得把单项报告简单扩写或重复。"
        "只输出合法 JSON，不得输出 Markdown 围栏。结构必须为："
        "{\"summary\":\"综合画像\",\"sections\":["
        "{\"id\":\"identity\",\"title\":\"你的整体人格画像\",\"conclusion\":\"\",\"reasoning\":\"\",\"evidence_ids\":[\"真实证据id\"],\"advice\":\"\"},"
        "{\"id\":\"strengths\",\"title\":\"优势、天赋与容易忽略的盲点\",\"conclusion\":\"\",\"reasoning\":\"\",\"evidence_ids\":[\"真实证据id\"],\"advice\":\"\"},"
        "{\"id\":\"mindset\",\"title\":\"思维方式、行动动力与成长卡点\",\"conclusion\":\"\",\"reasoning\":\"\",\"evidence_ids\":[\"真实证据id\"],\"advice\":\"\"},"
        "{\"id\":\"relationship\",\"title\":\"情感需求与长期关系模式\",\"conclusion\":\"\",\"reasoning\":\"\",\"evidence_ids\":[\"真实证据id\"],\"advice\":\"\"},"
        "{\"id\":\"career\",\"title\":\"事业方向、工作方式与发展环境\",\"conclusion\":\"\",\"reasoning\":\"\",\"evidence_ids\":[\"真实证据id\"],\"advice\":\"\"},"
        "{\"id\":\"finance\",\"title\":\"财富观念、收入资源与风险盲点\",\"conclusion\":\"\",\"reasoning\":\"\",\"evidence_ids\":[\"真实证据id\"],\"advice\":\"\"},"
        "{\"id\":\"timing\",\"title\":\"当前阶段与未来30天观察重点\",\"conclusion\":\"\",\"reasoning\":\"\",\"evidence_ids\":[\"真实证据id\"],\"advice\":\"\"}],"
        "\"action_plan\":[\"具体行动\"],\"limitations\":[\"必要限制说明\"]}。"
        "sections 必须恰好7项，顺序和 id 按模板。每项必须包含非空 conclusion、reasoning、advice，"
        "并至少引用一个直接相关的真实 evidence_ids。不得编造证据编号。"
        "每节至少解释两层：星盘结构如何形成线索，以及它在日常生活中可能怎样体现；"
        "说明另一面或适用边界，避免单一星体决定论。七节不得换词重复。"
        "事业与财富必须区分职业环境、收入资源、共同财务/风险等不同主题；"
        "感情分析需求和互动模式，不预测结婚、分手、复合或伴侣身份。"
        "近期趋势只能使用输入中的真实行运证据；如果缺失或不足，明确说明无法作可靠的30天判断，"
        "不得用本命盘伪装成行运预测。"
        "action_plan 给出3至5条按优先级排列、普通人可以执行的具体行动，不得要求用户相信命运。"
        "用自然、细致、易懂的简体中文，不要虚构用户的年龄、职业、收入、经历或关系状态。"
    )
    user_payload = {
        "report_type": "完整人生星盘报告",
        "required_depth": "完整付费产品级报告。每节约180至260个汉字，提供个人化解释，避免空话和重复。",
        "evidence": evidence
    }
    try:
        response = requests.post(
            base_url + "/chat/completions",
            headers={"Authorization": "Bearer " + api_key, "Content-Type": "application/json"},
            json={
                "model": model,
                "thinking": {"type": "disabled"},
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": json.dumps(user_payload, ensure_ascii=False)}
                ],
                "response_format": {"type": "json_object"},
                "temperature": 0.35,
                "max_tokens": 9000,
                "stream": False
            },
            timeout=(10, 150)
        )
        if response.status_code >= 400:
            raise DeepSeekError("DeepSeek HTTP " + str(response.status_code))
        body = response.json()
        choices = body.get("choices") or []
        if not choices or not isinstance(choices[0], dict):
            raise DeepSeekError("DeepSeek 响应缺少 choices。")
        choice = choices[0]
        message = choice.get("message") or {}
        content = message.get("content")
        if not isinstance(content, str) or not content.strip():
            raise DeepSeekError("DeepSeek 完整报告返回内容为空。")
        if choice.get("finish_reason") == "length":
            raise DeepSeekError("完整报告达到输出长度上限，请重试。")
        result = _extract_json_object(content)
        if not isinstance(result.get("summary"), str) or not isinstance(result.get("sections"), list):
            raise DeepSeekError("完整报告结构不符合要求。")
        return result
    except DeepSeekError:
        raise
    except requests.Timeout as exc:
        raise DeepSeekError("DeepSeek 完整报告请求超时。") from exc
    except requests.RequestException as exc:
        raise DeepSeekError("DeepSeek 完整报告网络请求失败。") from exc
    except (ValueError, KeyError, TypeError, IndexError) as exc:
        raise DeepSeekError("DeepSeek 完整报告响应结构无法解析。") from exc



def analyze_tieshan_profile(pillars, birth, gender="", derived=None):
    """Generate a clearly-labeled traditional-culture reading from calculated pillars."""
    api_key = os.environ.get("DEEPSEEK_API_KEY", "").strip()
    if not api_key:
        raise DeepSeekNotConfigured("DeepSeek API 尚未配置，请在 Render 环境变量中设置 DEEPSEEK_API_KEY。")
    base_url = os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com").rstrip("/")
    model = os.environ.get("DEEPSEEK_MODEL", "deepseek-flash")
    if not isinstance(pillars, dict) or not all(
        isinstance(pillars.get(k), dict) and isinstance(pillars[k].get("name"), str)
        for k in ("year", "month", "day", "hour")
    ):
        raise ValueError("缺少有效四柱数据，请先完成四柱计算。")
    system_prompt = (
        "你是一位谨慎的中国传统干支文化研究报告撰写者。"
        "只能依据用户提供的四柱和出生资料进行基础干支文化层面的解释，不得自行改算四柱，"
        "不得声称掌握或执行了未提供的铁板神数定数、考刻、条文编号或秘传口诀。"
        "必须明确说明：当前输出是四柱基础文化解读，不是完整铁板神数定数，也不是古籍原文。"
        "不得编造具体人生经历、六亲事件、婚期、寿命、疾病、财富数额或必然事件。"
        "如果信息不足，明确说明限制。使用自然、具体、易懂的简体中文。"
        "报告必须先给普通用户能直接看懂的明确结论，禁止先堆日主、十神、藏干等术语。"
        "每个专题的conclusion先用2至4句直白中文回答：整体是什么倾向、最明显的优势或风险是什么、用户最该注意什么；不要用空泛的两面话，不要只说因人而异。"
        "reasoning再解释对应四柱数据如何支持判断，必要术语必须顺手翻译成人话；advice给出具体可执行做法。"
        "整体summary必须是可直接阅读的总判断，先说重点，再说明不确定之处。婚姻、事业财运必须分别给结论，不得混在一起。不得编造具体年份事件或保证结果。"
        "只输出合法 JSON，结构为：{\"summary\":\"整体说明\","
        "\"sections\":[{\"title\":\"主题\",\"conclusion\":\"结论\","
        "\"reasoning\":\"依据与解释\",\"advice\":\"现实建议\"}],"
        "\"limitations\":[\"限制说明\"]}。"
        "sections 必须恰好5项，分别讨论整体结构、性格与行事倾向、关系相处、事业与资源、现实行动建议。"
        "每项必须有实质内容，不能换词重复。"
    )
    payload = {
        "four_pillars": {
            key: {"name": pillars[key].get("name"), "stem": pillars[key].get("stem"),
                  "branch": pillars[key].get("branch")}
            for key in ("year", "month", "day", "hour")
        },
        "derived_bazi_data": derived or {},
        "birth_context": {
            "gender": gender,
            "local_datetime": birth.get("local_datetime"),
            "timezone": birth.get("timezone"),
            "place_resolved": birth.get("place_resolved")
        },
        "task": "请做谨慎的传统干支文化基础解读。优先引用输入中的日主、五行简单计数、十神、藏干和地支关系数据，并解释数据如何支持判断。五行简单计数不等于旺衰，禁止仅凭数量断旺弱。不要假称铁板神数定数已经完成。"
    }
    try:
        response = requests.post(
            base_url + "/chat/completions",
            headers={"Authorization": "Bearer " + api_key, "Content-Type": "application/json"},
            json={
                "model": model,
                "thinking": {"type": "disabled"},
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": json.dumps(payload, ensure_ascii=False)}
                ],
                "response_format": {"type": "json_object"},
                "temperature": 0.35,
                "max_tokens": 5000,
                "stream": False
            },
            timeout=(10, 120)
        )
        if response.status_code >= 400:
            raise DeepSeekError("DeepSeek HTTP " + str(response.status_code))
        body = response.json()
        choices = body.get("choices") or []
        if not choices:
            raise DeepSeekError("DeepSeek 响应缺少 choices。")
        choice = choices[0]
        if choice.get("finish_reason") == "length":
            raise DeepSeekError("AI 输出达到长度上限，请重试。")
        message = choice.get("message") or {}
        result = _extract_json_object(message.get("content"))
        sections = result.get("sections")
        if not isinstance(sections, list) or len(sections) != 5:
            raise DeepSeekError("AI 返回的专题结构不完整。")
        for section in sections:
            if not isinstance(section, dict) or any(
                not isinstance(section.get(k), str) or not section[k].strip()
                for k in ("title", "conclusion", "reasoning", "advice")
            ):
                raise DeepSeekError("AI 返回的专题内容不完整。")
        return result
    except (DeepSeekError, DeepSeekNotConfigured, ValueError):
        raise
    except requests.Timeout as exc:
        raise DeepSeekError("DeepSeek 请求超时。") from exc
    except requests.RequestException as exc:
        raise DeepSeekError("DeepSeek 网络请求失败。") from exc
    except (KeyError, TypeError, IndexError) as exc:
        raise DeepSeekError("DeepSeek 响应结构无法解析。") from exc


def analyze_tieshan_topic(topic, pillars, birth, gender="", derived=None):
    """Generate a dedicated finance or marriage reading from supplied Four Pillars evidence."""
    topic = str(topic or "").strip().lower()
    if topic not in ("finance", "marriage"):
        raise ValueError("专项主题只能是 finance 或 marriage。")
    if not isinstance(pillars, dict) or not all(
        isinstance(pillars.get(k), dict) and isinstance(pillars[k].get("name"), str)
        for k in ("year", "month", "day", "hour")
    ):
        raise ValueError("缺少有效四柱数据，请先完成四柱计算。")

    api_key = os.environ.get("DEEPSEEK_API_KEY", "").strip()
    if not api_key:
        raise DeepSeekNotConfigured("DeepSeek API 尚未配置，请在 Render 环境变量中设置 DEEPSEEK_API_KEY。")
    base_url = os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com").rstrip("/")
    model = os.environ.get("DEEPSEEK_MODEL", "deepseek-flash")

    guides = {
        "finance": {
            "name": "财运专项",
            "sections": [
                "整体财务倾向与资源基础",
                "正财、职业收入与稳定现金流",
                "偏财、机会型收入与风险边界",
                "适合积累的能力与求财路径",
                "财务压力、消费与合作风险",
                "阶段性行动建议"
            ],
            "focus": "围绕传统四柱文化中可谨慎讨论的财务资源、劳动收入、机会型收入、风险意识和积累习惯展开。不能仅凭某一个十神或五行数量断定富贵、贫穷或财星旺衰；若输入没有足够的旺衰、格局或大运资料，必须明确降低判断力度。将传统象义与现实经营能力区分开。禁止预测具体收入金额、中奖、发财年份或投资涨跌；不得给出买卖金融产品的指令。"
        },
        "marriage": {
            "name": "婚姻专项",
            "sections": [
                "整体感情与婚姻倾向",
                "情感需求与相处模式",
                "伴侣关系中的优势与磨合点",
                "长期婚姻、家庭责任与沟通",
                "关系风险与择偶边界",
                "现实行动与关系经营建议"
            ],
            "focus": "围绕传统四柱文化中可谨慎讨论的关系需求、相处模式、长期承诺、家庭责任和沟通方式展开。性别信息仅作为传统术语背景，不得刻板化。不得断言配偶身份、外貌、职业、年龄、婚期、离婚、复合或生育事件；缺少大运流年等资料时，不得伪造具体年份或婚恋窗口。强调现实关系以双方持续行为为准。"
        }
    }[topic]

    system_prompt = (
        "你是一位严谨的中国传统干支文化研究报告撰写者。"
        "你只能解释用户提供的四柱与辅助数据，不得自行改算四柱，不得补造十神、旺衰、格局、大运、流年或古籍条文。"
        "必须明确说明：本报告属于四柱基础文化解读，不是完整铁板神数定数，不是古籍原文，也不是科学验证的命运预测。"
        "只输出合法 JSON，不得输出 Markdown。JSON 结构必须为："
        '{"summary":"","sections":[{"title":"","conclusion":"","reasoning":"","advice":""}],"limitations":[]}。'
        "sections 必须恰好6项，标题依照用户任务给出的顺序；每项的 conclusion、reasoning、advice 均须具体且非空。"
        "先用通俗中文回答倾向，再解释对应输入数据；不得把五行简单计数等同于旺衰。"
        "不得虚构用户经历、收入、婚姻状态或现实事件，不得作确定性吉凶断言。"
        "每项至少给出一条普通人能执行的现实建议；内容彼此不得重复。"
    )
    payload = {
        "topic": guides["name"],
        "required_sections": guides["sections"],
        "topic_method": guides["focus"],
        "four_pillars": {
            key: {"name": pillars[key].get("name"), "stem": pillars[key].get("stem"),
                  "branch": pillars[key].get("branch")}
            for key in ("year", "month", "day", "hour")
        },
        "derived_bazi_data": derived or {},
        "birth_context": {
            "gender": gender,
            "local_datetime": (birth or {}).get("local_datetime"),
            "timezone": (birth or {}).get("timezone"),
            "place_resolved": (birth or {}).get("place_resolved")
        },
        "output_style": "输出面向普通用户的专项报告，先给清楚结论，再给依据和建议。不要用空话填充；资料不足时直说不足。"
    }
    try:
        response = requests.post(
            base_url + "/chat/completions",
            headers={"Authorization": "Bearer " + api_key, "Content-Type": "application/json"},
            json={
                "model": model,
                "thinking": {"type": "disabled"},
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": json.dumps(payload, ensure_ascii=False)}
                ],
                "response_format": {"type": "json_object"},
                "temperature": 0.3,
                "max_tokens": 6000,
                "stream": False
            },
            timeout=(10, 120)
        )
        if response.status_code >= 400:
            raise DeepSeekError("DeepSeek HTTP " + str(response.status_code))
        body = response.json()
        choices = body.get("choices") or []
        if not choices:
            raise DeepSeekError("DeepSeek 响应缺少 choices。")
        choice = choices[0]
        if choice.get("finish_reason") == "length":
            raise DeepSeekError("专项报告达到输出长度上限，请重试。")
        message = choice.get("message") or {}
        result = _extract_json_object(message.get("content"))
        sections = result.get("sections")
        if not isinstance(result.get("summary"), str) or not isinstance(sections, list) or len(sections) != 6:
            raise DeepSeekError("专项报告结构不完整。")
        for index, section in enumerate(sections):
            if not isinstance(section, dict) or any(
                not isinstance(section.get(key), str) or not section[key].strip()
                for key in ("title", "conclusion", "reasoning", "advice")
            ):
                raise DeepSeekError("专项报告第" + str(index + 1) + "项内容不完整。")
        if not isinstance(result.get("limitations"), list):
            result["limitations"] = []
        result["report_type"] = guides["name"]
        result["basis"] = "四柱基础文化解读"
        result["not_iron_plate_final_number"] = True
        return result
    except (DeepSeekError, DeepSeekNotConfigured, ValueError):
        raise
    except requests.Timeout as exc:
        raise DeepSeekError("专项分析请求超时。") from exc
    except requests.RequestException as exc:
        raise DeepSeekError("专项分析网络请求失败。") from exc
    except (KeyError, TypeError, IndexError) as exc:
        raise DeepSeekError("专项分析响应结构无法解析。") from exc

