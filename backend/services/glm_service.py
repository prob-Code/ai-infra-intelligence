import os
import requests
from dotenv import load_dotenv
import json
from models.ai_response import AIResponse

from utils.json_parser import extract_json
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

URL = "https://router.huggingface.co/v1/chat/completions"


def glm_analysis(prompt: str):

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "zai-org/GLM-5.2",
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
    }


    response = requests.post(
        URL,
        headers=headers,
        json=payload,
        timeout=60,
    )


    response.raise_for_status()

    data = response.json()

    content = data["choices"][0]["message"]["content"]

    parsed = extract_json(content)

    validated = AIResponse(**parsed)

    return validated.model_dump()
