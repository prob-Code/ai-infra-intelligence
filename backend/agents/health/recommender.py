from agents.health.predictor import predict_resource_usage


def recommend_actions():

    prediction = predict_resource_usage()

    recommendations = []

    if prediction["cpu_growth"] > 5:
        recommendations.append(
            "Investigate high CPU usage"
        )

    if prediction["memory_growth"] > 3:
        recommendations.append(
            "Consider increasing memory"
        )

    if prediction["disk_growth"] > 1:
        recommendations.append(
            "Review storage utilization"
        )

    if not recommendations:
        recommendations.append(
            "No action required"
        )

    return {
        "recommendations": recommendations
    }
