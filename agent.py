from mcp_server import run_tool 
from db_tool import store_image_result, get_user_images
from openai import OpenAI 
from db_tool import store_image_result
import json 

client = OpenAI()

tools = [
    {
        "type": "function",
        "function" : {
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
    },
    
    {
    "type":"function",
    "function":{
        "name":"get_user_images",
        "description": "Get images uploaded by the user",
        "parameters":{
         "type":"object",
         "properties": {
          "user_name":{"type":"string"}
         },
         "required":["user_name"]
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
                        
    if tool_call.function.name == "store_image_result":                    
        result = run_tool(tool_call.function.name,arguments)
    

    elif tool_call.function.name == "get_user_images":
        arguments = json.loads(tool_call.function.arguments)
        result = run_tool(tool_call.function.name,arguments)

    
    print(result) 