from database.session import get_db
from models.ai_event import AIEvent
from datetime import datetime


def update_incident_status(
    incident_id: str,
    status: str,
    resolution: str = ""
):
    db = next(get_db())

    incident = (
        db.query(AIEvent)
        .filter(AIEvent.incident_id == incident_id)
        .first()
    )

    if not incident:
        return {
            "status": "error",
            "message": "Incident not found."
        }

    incident.status = status

    if resolution:
        incident.resolution = resolution

    if status == "RESOLVED":
        incident.resolved_at = datetime.utcnow()

    db.commit()
    db.refresh(incident)

    return {
        "status": "success",
        "incident_id": incident.incident_id,
        "current_status": incident.status,
        "resolution": incident.resolution
    }
