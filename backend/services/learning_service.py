from database.session import get_db
from models.ai_event import AIEvent
from sqlalchemy import func


def get_learning_statistics():

    db = next(get_db())

    total = db.query(AIEvent).count()

    success = (
        db.query(AIEvent)
        .filter(AIEvent.status == "RESOLVED")
        .count()
    )

    failed = (
        db.query(AIEvent)
        .filter(AIEvent.status != "RESOLVED")
        .count()
    )

    success_rate = 0

    if total > 0:
        success_rate = round((success / total) * 100, 2)

    return {
        "total_learning_events": total,
        "successful_resolutions": success,
        "unsuccessful_resolutions": failed,
        "learning_success_rate": success_rate
    }
