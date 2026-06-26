from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

load_dotenv()

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://neo4j:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")


class Neo4jService:

    def __init__(self):
        self.driver = GraphDatabase.driver(
            NEO4J_URI,
            auth=(NEO4J_USER, NEO4J_PASSWORD)
        )

    def close(self):
        self.driver.close()

    def create_incident_graph(
        self,
        incident_id,
        risk,
        root_cause,
        recommendation,
        action
    ):

        query = """
        MERGE (i:Incident {id:$incident_id, risk:$risk})
        MERGE (r:RootCause {name:$root_cause})
        MERGE (rec:Recommendation {name:$recommendation})
        MERGE (a:Action {name:$action})

        MERGE (i)-[:CAUSED_BY]->(r)
        MERGE (r)-[:RECOMMENDS]->(rec)
        MERGE (rec)-[:EXECUTES]->(a)
        """

        with self.driver.session() as session:
            session.run(
                query,
                incident_id=incident_id,
                risk=risk,
                root_cause=root_cause,
                recommendation=recommendation,
                action=action
            )
