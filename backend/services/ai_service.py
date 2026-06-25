from agents.health.predictor import predict_resource_usage
from agents.health.explainer import explain_cluster
from agents.ai.infrastructure_agent import analyze_infrastructure


def run_ai_analysis():

    prediction = predict_resource_usage()

    explanation = explain_cluster()

    payload = {
        "prediction": prediction,
        "explanation": explanation
    }

    return analyze_infrastructure(payload)
