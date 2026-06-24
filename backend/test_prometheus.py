from agents.health.prometheus_collector import PrometheusCollector

collector = PrometheusCollector()

print("\nCPU Usage")
print(collector.get_cpu_usage())

print("\nMemory Usage")
print(collector.get_memory_usage())

print("\nDisk Usage")
print(collector.get_disk_usage())

