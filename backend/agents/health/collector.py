# backend/agents/health/collector.py

from .prometheus_collector import PrometheusCollector
from services.metric_service import save_metric


def collect_metrics():

    prom = PrometheusCollector()

    cpu_data = prom.get_cpu_usage()
    memory_data = prom.get_memory_usage()
    disk_data = prom.get_disk_usage()

    cpu = float(cpu_data[0]["value"][1]) if cpu_data else 0
    memory = float(memory_data[0]["value"][1]) if memory_data else 0
    disk = float(disk_data[0]["value"][1]) if disk_data else 0

    cpu = round(cpu, 2)
    memory = round(memory, 2)
    disk = round(disk, 2)

    save_metric(
        node_name="digitalocean-vps",
        cpu_usage=cpu,
        memory_usage=memory,
        disk_usage=disk
    )

    return {
        "digitalocean-vps": {
            "cpu": cpu,
            "memory": memory,
            "disk": disk
        }
    }
