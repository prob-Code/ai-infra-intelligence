from database.session import get_db
from models.metrics import NodeMetric

from datetime import datetime

from config.database import SessionLocal


def save_metric(
    node_name,
    cpu_usage,
    memory_usage,
    disk_usage
):

    db = SessionLocal()

    try:

        metric = NodeMetric(
            node_name=node_name,
            cpu_usage=cpu_usage,
            memory_usage=memory_usage,
            disk_usage=disk_usage,
            timestamp=datetime.utcnow()
        )

        db.add(metric)

        db.commit()

        db.refresh(metric)

        return metric

    finally:

        db.close()
