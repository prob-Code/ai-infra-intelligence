from models.ai_event import AIEvent
from database.session import get_db


def save_ai_event(
    risk,
    confidence,
    root_cause,
    recommendation,
    action,
    status
):
    db = next(get_db())

    event = AIEvent(
        risk=risk,
        confidence=confidence,
        root_cause=root_cause,
        recommendation=recommendation,
        action=action,
        status=status
    )

    db.add(event)
    db.commit()
    db.refresh(event)

    return {
        "message": "AI event saved successfully.",
        "id": event.id
    }
