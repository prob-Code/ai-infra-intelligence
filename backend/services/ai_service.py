from services.glm_service import glm_analysis
from services.risk_service import calculate_risk


def run_ai_analysis():

    risk = calculate_risk()

    prompt = f"""
You are an autonomous AI Infrastructure Operations Engineer.

Analyze the following infrastructure metrics.

CPU Growth: {risk["metrics"]["cpu_growth"]}
Memory Growth: {risk["metrics"]["memory_growth"]}
Disk Growth: {risk["metrics"]["disk_growth"]}

Risk Score: {risk["risk_score"]}
Risk Level: {risk["risk_level"]}

Your task is to determine:

- Infrastructure risk
- Root cause
- Best recommendation
- Actions that should be executed automatically

Return ONLY valid JSON.

Do NOT return Markdown.

Do NOT explain anything outside JSON.

Return exactly this format:

{{
  "risk": "LOW | MEDIUM | HIGH",
  "confidence": 95,
  "root_cause": "Short explanation",
  "recommendation": "Recommended action",
  "actions": [
    "Create Storage Alert",
    "Notify Administrator"
  ]
}}
"""
    return glm_analysis(prompt)
