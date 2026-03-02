from neo4j import GraphDatabase

URI = "neo4j+ssc://86405cce.databases.neo4j.io"
USERNAME = "86405cce"
PASSWORD = "kBtEFN6aZ4TnHpwStGg0dchXlgIvqQUnRjbOeTvXNmM"

driver =  GraphDatabase.driver(URI,auth=(USERNAME, PASSWORD))

def test_connection():
    with driver.session() as session:
        result = session.run("RETURN 'Connected to Neo4j!' As message")
        for record in result:
            print(record["message"])

test_connection()
driver.close()
