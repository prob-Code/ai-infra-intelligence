# backend/agents/health/analyzer.py

from .collector import collect_metrics
from .scorer import calculate_status


def analyze_cluster():

    metrics = collect_metrics()

    results = []

    for node, data in metrics.items():

        status = calculate_status(
            data["cpu"],
            data["memory"],
            data["disk"]
        )

        results.append({
            "name": node,
            "cpu": data["cpu"],
            "memory": data["memory"],
            "disk": data["disk"],
            "status": status
        })

    return results