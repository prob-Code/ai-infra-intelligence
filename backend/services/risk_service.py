from agents.health.predictor import predict_resource_usage


def calculate_risk():

    prediction = predict_resource_usage()

    score = 0

    if prediction["cpu_growth"] > 1:
        score += 30

    if prediction["memory_growth"] > 1:
        score += 30

    if prediction["disk_growth"] > 1:
        score += 40

    if score < 30:
        level = "LOW"

    elif score < 70:
        level = "MEDIUM"

    else:
        level = "HIGH"

    return {
        "risk_score": score,
        "risk_level": level,
        "metrics": prediction
    }
