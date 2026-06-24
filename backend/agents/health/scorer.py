# backend/agents/health/scorer.py

def calculate_status(cpu, memory, disk):

    if cpu > 90 or memory > 90 or disk > 90:
        return "critical"

    if cpu > 75 or memory > 75 or disk > 75:
        return "warning"

    return "healthy"