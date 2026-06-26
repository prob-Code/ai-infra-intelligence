from pydantic import BaseModel
from typing import List


class AIResponse(BaseModel):
    risk: str
    confidence: int
    root_cause: str
    recommendation: str
    actions: List[str]
