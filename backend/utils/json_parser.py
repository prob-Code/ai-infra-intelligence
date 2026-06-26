import json
import re


def extract_json(text: str):
    """
    Extract the first JSON object from an LLM response.
    """

    # Remove Markdown code fences
    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    # Find the first JSON object
    match = re.search(r"\{.*\}", text, re.DOTALL)

    if not match:
        raise ValueError("No JSON object found in AI response.")

    return json.loads(match.group())
