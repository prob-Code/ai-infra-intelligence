from database.session import get_db
from models.ai_event import AIEvent


def search_similar_incident(root_cause: str):

    db = next(get_db())

    incident = (
        db.query(AIEvent)
        .filter(AIEvent.root_cause == root_cause)
        .order_by(AIEvent.created_at.desc())
        .first()
    )

    if not incident:
        return {
            "found": False
        }

    return {
        "found": True,
        "incident_id": incident.incident_id,
        "recommendation": incident.recommendation,
        "action": incident.action,
        "status": incident.status
    }
