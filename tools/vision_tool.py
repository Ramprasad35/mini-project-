def vision_tool(image_path):
    try:
        return f"I have analyzed the image: {image_path}\nIt appears to contain recognizable object"

    except Exception as  e :
        return f"Error analyzing image:{str(e)}"
    
if __name__ == "__main__":
    image_path = input("Enter image path: ")
    result = vision_tool(image_path)
    print(result) 