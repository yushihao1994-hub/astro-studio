import json
import os

import requests


class DeepSeekNotConfigured(Exception):
    pass


class DeepSeekError(Exception):
    pass


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

    system_prompt = (
        "你是严谨的西方占星研究报告撰写者。你只能解释用户提供的结构化星盘证据，"
        "不得自行计算星体位置、宫位、相位或行运，不得补造缺失数据。"
        "占星属于文化与自我探索框架，不是科学验证的命运预测。"
        "若证据不足或相互矛盾，必须明确说明不确定，不得用确定语气预测事件。"
        "输出必须是合法 JSON 对象，字段为 summary、sections、limitations。"
        "sections 是数组，每项包含 title、conclusion、reasoning、evidence_ids、advice。"
        "evidence_ids 只能使用输入证据中真实存在的 id；每项至少引用一个直接相关的证据。"
        "用自然、具体、易懂的简体中文，避免空话、重复句和堆砌占星术语。"
        "区分盘面倾向、现实表现和建议，不承诺发财、结婚、复合或具体事件。"
    )
    user_payload = {
        "analysis_topic": topic_name,
        "evidence": evidence,
        "required_style": "面向普通用户，具体解释可能表现、证据依据、现实建议；不要展示内部技术术语清单。"
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
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": json.dumps(user_payload, ensure_ascii=False)}
                ],
                "response_format": {"type": "json_object"},
                "temperature": 0.4,
                "max_tokens": 3000,
                "stream": False
            },
            timeout=(10, 90)
        )
        if response.status_code >= 400:
            raise DeepSeekError("DeepSeek HTTP " + str(response.status_code))
        body = response.json()
        content = body["choices"][0]["message"]["content"]
        result = json.loads(content)
        if not isinstance(result, dict) or not isinstance(result.get("sections"), list):
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
        raise DeepSeekError("DeepSeek 返回内容无法解析。") from exc
