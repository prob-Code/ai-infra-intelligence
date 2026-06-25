from services.risk_service import calculate_risk

def dashboard_summary():

    risk = calculate_risk()

    return {
        "platform": "AI Infrastructure Intelligence Platform",
        "cluster_status": "HEALTHY",
        "risk": risk,
        "capabilities": [
            "Observe",
            "Analyze",
            "Predict",
            "Explain",
            "Recommend",
            "Execute",
            "Learn"
        ]
    }
