import requests


NODES = {
    "mgs-mds": "http://192.168.56.105:9100/metrics",
    "oss1": "http://192.168.56.106:9100/metrics",
    "oss2": "http://192.168.56.107:9100/metrics"
}


def check_node(node_name, url):

    try:

        response = requests.get(
            url,
            timeout=5
        )

        if response.status_code == 200:

            return {
                "node": node_name,
                "status": "online"
            }

        return {
            "node": node_name,
            "status": "offline"
        }

    except Exception:

        return {
            "node": node_name,
            "status": "offline"
        }


def collect_cluster_status():

    results = []

    for node, url in NODES.items():

        results.append(
            check_node(
                node,
                url
            )
        )

    return results
