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
