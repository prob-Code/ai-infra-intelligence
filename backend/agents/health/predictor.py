from services.trend_service import get_recent_metrics


def predict_resource_usage():

    history = get_recent_metrics(limit=10)

    if len(history) < 2:
        return {
            "prediction": "Not enough historical data"
        }

    oldest = history[-1]
    latest = history[0]

    cpu_growth = latest.cpu_usage - oldest.cpu_usage
    memory_growth = latest.memory_usage - oldest.memory_usage
    disk_growth = latest.disk_usage - oldest.disk_usage

    prediction = {
        "cpu_growth": round(cpu_growth, 2),
        "memory_growth": round(memory_growth, 2),
        "disk_growth": round(disk_growth, 2),
    }

    if cpu_growth > 10:
        prediction["cpu_prediction"] = "CPU usage is rising rapidly"
    elif cpu_growth > 0:
        prediction["cpu_prediction"] = "CPU usage increasing slowly"
    else:
        prediction["cpu_prediction"] = "CPU usage stable"

    if memory_growth > 5:
        prediction["memory_prediction"] = "Memory usage increasing"
    else:
        prediction["memory_prediction"] = "Memory usage stable"

    if disk_growth > 1:
        prediction["disk_prediction"] = "Disk usage increasing"
    else:
        prediction["disk_prediction"] = "Disk usage stable"

    return prediction
