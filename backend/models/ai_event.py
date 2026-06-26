from sqlalchemy import Column, Integer, String, DateTime, Float
from datetime import datetime

from config.database import Base


class AIEvent(Base):

    __tablename__ = "ai_events"

    id = Column(Integer, primary_key=True)

    incident_id = Column(String, unique=True)

    risk = Column(String)

    confidence = Column(Integer)

    cpu_growth = Column(Float)

    memory_growth = Column(Float)

    disk_growth = Column(Float)

    root_cause = Column(String)

    recommendation = Column(String)

    action = Column(String)

    status = Column(String)

    resolution = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)

    resolved_at = Column(DateTime, nullable=True)
