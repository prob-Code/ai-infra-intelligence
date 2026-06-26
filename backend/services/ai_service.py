from services.glm_service import glm_analysis
from services.risk_service import calculate_risk


def run_ai_analysis():

    risk = calculate_risk()

    prompt = f"""
You are an AI Infrastructure Engineer.

Analyze this server.

CPU Growth: {risk["metrics"]["cpu_growth"]}
Memory Growth: {risk["metrics"]["memory_growth"]}
Disk Growth: {risk["metrics"]["disk_growth"]}

Risk Score:
{risk["risk_score"]}

Risk Level:
{risk["risk_level"]}

Explain:

1. Why this happened.
2. Possible impact.
3. Recommendation.

Return plain English.
"""

    result = glm_analysis(prompt)

    return {
        "analysis": result
    }
