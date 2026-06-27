import os
from openai import OpenAI
from dotenv import load_dotenv

from models.ai_response import AIResponse
from utils.json_parser import extract_json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

MODEL = os.getenv("OPENAI_MODEL", "gpt-5.5")


def glm_analysis(prompt: str):

    response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": (
                "You are an AI Infrastructure Operations Engineer. "
                "Always return ONLY valid JSON."
            ),
        },
        {
            "role": "user",
            "content": prompt,
        },
    ]
)

    content = response.choices[0].message.content

    parsed = extract_json(content)

    validated = AIResponse(**parsed)

    return validated.model_dump()
