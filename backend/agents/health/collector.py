# backend/agents/health/collector.py

def collect_metrics():
    return {
        "mgs-mds": {
            "cpu": 25,
            "memory": 45,
            "disk": 60
        },
        "oss1": {
            "cpu": 40,
            "memory": 55,
            "disk": 70
        },
        "oss2": {
            "cpu": 85,
            "memory": 80,
            "disk": 88
        }
    }