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
                    "label":{"type":"string"}
                },
                "required":["user_name", "image_name","label"]
            }
        }
    } 
]
response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [
        {"role":"user","content":"Store that Ram uploaded cat.jpg with a label Cat"}
    ],  
    tools= tools 
)
if response.choices[0].message.tool_calls:
    tool_call = response.choices[0].message.tool_calls[0]
    arguments = json.loads(tool_call.function.arguments)
                        
    result = store_image_result(
        arguments["user_name"],             
        arguments["image_name"],
        arguments["label"],
    )
    print(result)