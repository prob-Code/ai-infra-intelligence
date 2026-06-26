import os
import requests
from dotenv import load_dotenv

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
    print("HF_TOKEN:", HF_TOKEN[:10] + "..." if HF_TOKEN else "None")
    print("Headers:", headers)


    response = requests.post(
        URL,
        headers=headers,
        json=payload,
        timeout=60,
    )

    print("Status Code:", response.status_code)
    print("Response:", response.text)

    response.raise_for_status()

    data = response.json()
    return data["choices"][0]["message"]["content"]
