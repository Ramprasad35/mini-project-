from db_tool import store_image_result ,get_user_images
from db_tool import get_all_users
def run_tool(tool_name,args):

    if tool_name == "store_image_result":
        return store_image_result(
            args["user_name"],
            args["image_name"],
            args["label"]
        )
    elif tool_name == "get_user_images":
        return get_user_images(
            args["user_name"]
        )
    
    elif tool_name == "get_all_users":
        return get_all_users()

print(run_tool("get_all_users", {}))
print(run_tool("get_user_images",{"user_name": "ram"}))
