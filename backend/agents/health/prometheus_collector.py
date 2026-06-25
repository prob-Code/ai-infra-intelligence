from prometheus_api_client import PrometheusConnect


class PrometheusCollector:

    def __init__(self):
        self.prom = PrometheusConnect(
            url="http://ai-prometheus:9090",
            disable_ssl=True
        )

    def get_cpu_usage(self):

        query = """
           100 - (
            avg(
              rate(node_cpu_seconds_total{mode="idle"}[1m])
                ) * 100
                 )
                 """

        return self.prom.custom_query(query)

    def get_memory_usage(self):

        query = """
        (
          1 -
          (
            node_memory_MemAvailable_bytes
            /
            node_memory_MemTotal_bytes
          )
        ) * 100
        """

        return self.prom.custom_query(query)

    def get_disk_usage(self):

        query = """
        (
          1 -
          (
            node_filesystem_avail_bytes
            /
            node_filesystem_size_bytes
          )
        ) * 100
        """

        return self.prom.custom_query(query)

    def get_total_memory(self):

        query = """
        node_memory_MemTotal_bytes
        """

        return self.prom.custom_query(query)
