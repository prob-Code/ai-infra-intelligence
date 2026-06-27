from config.neo4j import driver


def save_incident_graph(
    incident_id,
    risk,
    root_cause,
    recommendation,
    action,
    host="OSS1",
    service="LustreFS",
    ai_engine="Hybrid AI",
    workflow="Storage Alert Workflow"
):

    with driver.session() as session:

        session.run(
            """
            MERGE (h:Host {name:$host})

            MERGE (s:Service {name:$service})

            MERGE (i:Incident {id:$incident})

            SET i.risk = $risk

            MERGE (r:Risk {name:$risk})

            MERGE (c:RootCause {name:$cause})

            MERGE (rec:Recommendation {name:$recommendation})

            MERGE (a:Action {name:$action})

            MERGE (ai:AIEngine {name:$ai_engine})

            MERGE (w:Workflow {name:$workflow})

            MERGE (h)-[:RUNS_SERVICE]->(s)

            MERGE (s)-[:GENERATED_INCIDENT]->(i)

            MERGE (i)-[:HAS_RISK]->(r)

            MERGE (i)-[:CAUSED_BY]->(c)

            MERGE (i)-[:DETECTED_BY]->(ai)

            MERGE (i)-[:RESOLVED_BY]->(rec)

            MERGE (rec)-[:EXECUTES]->(a)

            MERGE (a)-[:AUTOMATED_BY]->(w)""",
            incident=incident_id,
            risk=risk,
            cause=root_cause,
            recommendation=recommendation,
            action=action,
            host=host,
            service=service,
            ai_engine=ai_engine,
            workflow=workflow
        )

    return {
        "status": "graph saved"
    }
