from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from config.database import Base


class AIEvent(Base):

    __tablename__ = "ai_events"

    id = Column(Integer, primary_key=True)

    prediction = Column(String)

    recommendation = Column(String)

    action = Column(String)

    risk_level = Column(String)

    timestamp = Column(DateTime, default=datetime.utcnow)
