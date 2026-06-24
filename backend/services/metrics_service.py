from datetime import datetime

from models.metrics import NodeMetric


def save_metric(
    db,
    node_name,
    cpu,
    memory,
    disk
):

    metric = NodeMetric(
        node_name=node_name,
        cpu_usage=cpu,
        memory_usage=memory,
        disk_usage=disk,
        timestamp=datetime.utcnow()
    )

    db.add(metric)

    db.commit()

    db.refresh(metric)

    return metric 
    