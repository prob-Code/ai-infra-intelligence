from fastapi import FastAPI

from agents.health.analyzer import analyze_cluster

app = FastAPI(
    title="AI Infrastructure Intelligence Platform",
    version="1.0.0"
)


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