from config.database import SessionLocal

from models.ai_event import AIEvent


def save_learning_event(
    prediction,
    recommendation,
    action,
    risk_level
):

    db = SessionLocal()

    try:

        event = AIEvent(
            prediction=prediction,
            recommendation=recommendation,
            action=action,
            risk_level=risk_level
        )

        db.add(event)

        db.commit()

        return {
            "status": "saved"
        }

    finally:

        db.close()
