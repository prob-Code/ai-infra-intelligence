from database.session import get_db
from models.ai_event import AIEvent
from sqlalchemy import func


def get_ai_performance():

    db = next(get_db())

    avg_confidence = (
        db.query(func.avg(AIEvent.confidence))
        .scalar()
    )

    top_action = (
        db.query(
            AIEvent.action,
            func.count(AIEvent.action).label("count")
        )
        .group_by(AIEvent.action)
        .order_by(func.count(AIEvent.action).desc())
        .first()
    )

    top_recommendation = (
        db.query(
            AIEvent.recommendation,
            func.count(AIEvent.recommendation).label("count")
        )
        .group_by(AIEvent.recommendation)
        .order_by(func.count(AIEvent.recommendation).desc())
        .first()
    )

    top_root_cause = (
        db.query(
            AIEvent.root_cause,
            func.count(AIEvent.root_cause).label("count")
        )
        .group_by(AIEvent.root_cause)
        .order_by(func.count(AIEvent.root_cause).desc())
        .first()
    )

    return {
        "average_confidence": round(avg_confidence or 0, 2),
        "most_common_action": top_action[0] if top_action else None,
        "most_common_recommendation": top_recommendation[0] if top_recommendation else None,
        "most_common_root_cause": top_root_cause[0] if top_root_cause else None
    }
