from neo4j import GraphDatabase

URI = "neo4j+ssc://86405cce.databases.neo4j.io"
USERNAME = "86405cce"
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

def get_user_images(user_name):
    with driver.session() as session:
        result = session.run(
            """Match(u:User{name:$user_name})-[:UPLOADED]->(i:Image)
            RETURN i.name AS image_name
            """,
            user_name=user_name
        )         
        images = [record["images_name"]for record in result]
        return images                                               
