from models.ai_event import AIEvent
from database.session import get_db
from utils.incident_id import generate_incident_id
from services.knowledge_graph_service import save_incident_graph

def save_ai_event(
    risk,
    confidence,
    root_cause,
    recommendation,
    action,
    status
):
    db = next(get_db())

    incident_id = generate_incident_id()

    event = AIEvent(
        incident_id=incident_id,
        risk=risk,
        confidence=confidence,
        cpu_growth=0.0,
        memory_growth=0.0,
        disk_growth=0.0,
        root_cause=root_cause,
        recommendation=recommendation,
        action=action,
        status=status,
        resolution="Pending"
    )

    db.add(event)
    db.commit()
    db.refresh(event)
    save_incident_graph(
        incident_id=incident_id,
        risk=risk,
        root_cause=root_cause,
        recommendation=recommendation,
        action=action
)
    return {
        "message": "AI event saved successfully.",
        "id": event.id,
        "incident_id": event.incident_id
    }
