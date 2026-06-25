from config.database import SessionLocal
from models.metrics import NodeMetric


def get_recent_metrics(limit=20):

    db = SessionLocal()

    try:

        metrics = (
            db.query(NodeMetric)
            .order_by(NodeMetric.timestamp.desc())
            .limit(limit)
            .all()
        )

        return metrics

    finally:

        db.close()
