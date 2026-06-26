from neo4j import GraphDatabase

URI = "bolt://ai-neo4j:7687"
USERNAME = "neo4j"
PASSWORD = "password123"

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)
