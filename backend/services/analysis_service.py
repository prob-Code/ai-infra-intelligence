from services.trend_service import get_recent_metrics


def analyze_trends():

    metrics = get_recent_metrics(10)

    if len(metrics) < 2:
        return {
            "message": "Not enough data"
        }

    latest = metrics[0]
    oldest = metrics[-1]

    cpu_trend = latest.cpu_usage - oldest.cpu_usage
    memory_trend = latest.memory_usage - oldest.memory_usage
    disk_trend = latest.disk_usage - oldest.disk_usage

    return {
        "cpu_change": round(cpu_trend, 2),
        "memory_change": round(memory_trend, 2),
        "disk_change": round(disk_trend, 2),
        "cpu_status": (
            "increasing"
            if cpu_trend > 0
            else "decreasing"
        ),
        "memory_status": (
            "increasing"
            if memory_trend > 0
            else "decreasing"
        ),
        "disk_status": (
            "increasing"
            if disk_trend > 0
            else "decreasing"
        )
    }
