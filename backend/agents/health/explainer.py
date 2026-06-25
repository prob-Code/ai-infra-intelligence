from agents.health.predictor import predict_resource_usage


def explain_cluster():

    prediction = predict_resource_usage()

    explanation = []

    if prediction["cpu_growth"] > 5:
        explanation.append(
            "CPU usage trend is increasing"
        )

    if prediction["memory_growth"] > 3:
        explanation.append(
            "Memory consumption is increasing"
        )

    if prediction["disk_growth"] > 1:
        explanation.append(
            "Disk utilization is growing"
        )

    if not explanation:
        explanation.append(
            "Infrastructure appears stable"
        )

    return {
        "prediction": prediction,
        "explanation": explanation
    }
