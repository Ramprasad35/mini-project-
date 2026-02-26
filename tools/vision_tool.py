import os 
import random
def vision_tool(image_path):
    try:
        if not os.path.exists(image_path):
            return f"Image '{image_path}' not found."
        
        lower_path = image_path.lower()

        if "cat" in lower_path:
            label = "cat"
            description =  "Cats are small domesticated animals know for agility and curiousity"

        elif "dog" in lower_path:
            label = "Dog"
            description = "Dogs are loyal animals often kept as pets and known for companionship."
        elif "car" in lower_path:
            label = "Car"
            description = "Cars are motor vehicles used for transportation."
        else:
            label = "Unknown Object"
            description = "I could not confidently determine the object in the image."
        
        confidence = random.randint(85,99)

        metadata = {
            "Format": image_path.split(".")[-1].upper(),
            "Resolution" : "1024x768"
        }

        return(
            f"Recognized :{label}\n"
            f"Confidence: {confidence}%\n"
            f"{description}\n"
            f"Format: {metadata['Format']}\n"
            f"Resolution: {metadata['Resolution']}"
        )

        

    except Exception as  e :
        return f"Error analyzing image:{str(e)}"
    
if __name__ == "__main__":
    image_path = input("Enter image path: ")
    result = vision_tool(image_path)
    print(result) 