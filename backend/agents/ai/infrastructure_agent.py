import os
import requests

from dotenv import load_dotenv

load_dotenv()


def analyze_infrastructure(metrics):

    api_key = os.getenv("OPENROUTER_API_KEY")

    prompt = f"""
You are an AI Infrastructure Operations Engineer.

Analyze these metrics:

{metrics}

Return:
1. Risk Level
2. Explanation
3. Recommendation

Keep response concise.
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-oss-120b:free",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
    )

    result = response.json()

    if "choices" not in result:

        return {
            "analysis": f"AI Provider Error: {result.get('error', {}).get('message', 'Unknown error')}"
        }

    return {
        "analysis": result["choices"][0]["message"]["content"]
    }
