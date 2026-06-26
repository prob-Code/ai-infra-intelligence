from database.session import get_db
from models.ai_event import AIEvent


def get_history(limit=20):

    db = next(get_db())

    events = (
        db.query(AIEvent)
        .order_by(AIEvent.timestamp.desc())
        .limit(limit)
        .all()
    )

    history = []

    for event in events:

        history.append({

            "id": event.id,

            "risk": event.risk,

            "confidence": event.confidence,

            "root_cause": event.root_cause,

            "recommendation": event.recommendation,

            "action": event.action,

            "status": event.status,

            "timestamp": event.timestamp

        })

    return history
