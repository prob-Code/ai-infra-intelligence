from agents.health.prometheus_collector import PrometheusCollector


collector = PrometheusCollector()


def get_cluster_health():

    return {
        "cpu": collector.get_cpu_usage(),
        "memory": collector.get_memory_usage(),
        "disk": collector.get_disk_usage()
    }