from config.neo4j import driver


def save_incident_graph(
    incident_id,
    risk,
    root_cause,
    recommendation,
    action
):

    with driver.session() as session:

        session.run(
            """
            MERGE (i:Incident {id:$incident})

            MERGE (r:Risk {name:$risk})

            MERGE (c:Cause {name:$cause})

            MERGE (rec:Recommendation {name:$recommendation})

            MERGE (a:Action {name:$action})

            MERGE (i)-[:HAS_RISK]->(r)

            MERGE (i)-[:CAUSED_BY]->(c)

            MERGE (i)-[:RECOMMENDS]->(rec)

            MERGE (i)-[:EXECUTES]->(a)
            """,
            incident=incident_id,
            risk=risk,
            cause=root_cause,
            recommendation=recommendation,
            action=action
        )

    return {
        "status": "graph saved"
    }
