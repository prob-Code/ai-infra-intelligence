from config.neo4j import driver

with driver.session() as session:
    result = session.run("RETURN 'Neo4j Connected' AS message")
    print(result.single()["message"])
