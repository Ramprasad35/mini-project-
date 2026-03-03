from neo4j import GraphDatabase

URI = "neo4j+ssc://86405cce.databases.neo4j.io"
USERNAME = "8605cce"
PASSWORD = "kBtEFN6aZ4TnHpwStGg0dchXlgIvqQUnRjbOeTvXNmM"

driver = GraphDatabase.driver(URI,auth=(USERNAME,PASSWORD))

def store_image_result(user_name, image_name ,label):
    with driver.session() as session:
        session.run(""" 
                    MERGE (u:User {name: $user_name})
                    MERGE (i:Image {name: $image_name})
                    MERGE (o:Object{name: $label})
                    MERGE (U)-[:UPLOADED] -> (i)
                    MERGE (i)-[:CONTAINS] -> (o)
                """,user_name=user_name, image_name=image_name, label=label)
        
        return "Data stored successully in Neo4j" 

