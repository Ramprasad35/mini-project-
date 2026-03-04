from openai import OpenAI 
from db_tool import store_image_result
import json

client = OpenAI()

tools = [
    {
        "type": "function",
        "function": {
            "name": "store_image_result",
            "description": "Store image recognition result in Neo4j database",
            "parameters": {
                "type": "object",
                "properties": {
                    "user_name": {"type": "string"},
                    "image_name": {"type":"string"},
                }
            }
        }
    }
]
