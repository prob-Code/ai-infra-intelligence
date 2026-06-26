from services.glm_service import glm_analysis
from agents.health.explainer import explain_cluster
from agents.health.predictor import predict_resource_usage
from services.analysis_service import analyze_trends
from fastapi import FastAPI
from services.trend_service import get_recent_metrics
from agents.health.analyzer import analyze_cluster
from agents.health.recommender import recommend_actions
from services.ai_service import run_ai_analysis
from services.learn_service import save_learning_event
from config.database import Base, engine
from models.ai_event import AIEvent
from services.dashboard_service import dashboard_summary
from services.execute_service import execute_ai_action
from services.risk_service import calculate_risk
from pydantic import BaseModel
from services.save_event_service import save_ai_event
from services.history_service import get_history
app = FastAPI(
    title="AI Infrastructure Intelligence Platform",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)
@app.get("/")
def root():
    return {
        "message": "AI Infrastructure Intelligence Platform Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/cluster/health")
def cluster_health():

    nodes = analyze_cluster()

    return {
        "cluster_status": "healthy",
        "nodes": nodes
    }

@app.get("/metrics/history")
def metrics_history():

    metrics = get_recent_metrics()

    return [
        {
            "cpu": m.cpu_usage,
            "memory": m.memory_usage,
            "disk": m.disk_usage,
            "timestamp": str(m.timestamp)
        }
        for m in metrics
    ]

@app.get("/analysis/trends")
def trend_analysis():

    return analyze_trends()
@app.get("/predict")
def predict():

    return predict_resource_usage()
@app.get("/explain")
def explain():

    return explain_cluster()
@app.get("/recommend")
def recommend():

    return recommend_actions()

@app.get("/ai-analysis")
def ai_analysis():

    return run_ai_analysis()
@app.get("/execute")
def execute():

    return execute_action()
@app.get("/risk")
def risk():

    return calculate_risk()
@app.get("/learn")
def learn():

    return save_learning_event(
        prediction="Disk usage increasing",
        recommendation="Expand storage capacity",
        action="Create Storage Alert",
        risk_level="MEDIUM"
    )
@app.get("/learn")
def learn():

    return save_learning_event(
        prediction="Disk usage increasing",
        recommendation="Expand storage capacity",
        action="Create Storage Alert",
        risk_level="MEDIUM"
    )

@app.get("/dashboard")
def dashboard():

    return dashboard_summary()
from pydantic import BaseModel


class ActionRequest(BaseModel):
    action: str

class SaveEventRequest(BaseModel):
    risk: str
    confidence: int
    root_cause: str
    recommendation: str
    action: str
    status: str
@app.post("/execute-action")
def execute_action_endpoint(request: ActionRequest):

    return execute_ai_action(request.action)
@app.post("/save-ai-event")
def save_event_endpoint(request: SaveEventRequest):

    return save_ai_event(
        risk=request.risk,
        confidence=request.confidence,
        root_cause=request.root_cause,
        recommendation=request.recommendation,
        action=request.action,
        status=request.status
    )
@app.get("/history")
def history():

    return get_history()
