from database.session import get_db
from models.ai_event import AIEvent
from sqlalchemy import func


def get_incident_statistics():

    db = next(get_db())

    total = db.query(AIEvent).count()

    resolved = (
        db.query(AIEvent)
        .filter(AIEvent.status == "RESOLVED")
        .count()
    )

    open_incidents = total - resolved

    high = (
        db.query(AIEvent)
        .filter(AIEvent.risk == "HIGH")
        .count()
    )

    medium = (
        db.query(AIEvent)
        .filter(AIEvent.risk == "MEDIUM")
        .count()
    )

    low = (
        db.query(AIEvent)
        .filter(AIEvent.risk == "LOW")
        .count()
    )

    return {
        "total_incidents": total,
        "open_incidents": open_incidents,
        "resolved_incidents": resolved,
        "risk_distribution": {
            "high": high,
            "medium": medium,
            "low": low
        }
    }
