import os 
import random
def vision_tool(image_path):
    try:
        if not os.path.exists(image_path):
            return f"Image '{image_path}' not found."
        
        lower_path = image_path.lower()

        if "cat" in lower_path:
            label = "cat"
            description =  "Cats are small domesticated animals known for agility and curiosity"

        elif "dog" in lower_path:
            label = "Dog"
            description = "Dogs are loyal animals often kept as pets and known for companionship."

        elif "car" in lower_path:
            label = "Car" 
            description = "Cars are motor vehicles used for transportation."

        elif  "person" in lower_path:
            label = "person"
            description = "A person is  a human being " 

        elif  "laptop" in lower_path:
            label = "laptop"
            description = "A laptop is a portable personal computer"

        elif "Tree" in lower_path:
            label = "Tree"
            description = "A Tree is a tall plant with a trunk and branches"

        else:
            label = "Unknown Object"
            description = "I could not confidently determine the object in the image."
        
        confidence = random.randint(85,99)

        metadata = { 
            "Format": image_path.split(".")[-1].upper(),
            "Resolution" : "1024x768"
        }

        phrases = [
             f"This image appears to show a {label}.",
             f"I beleive this is a {label} ." ,
             f"The image most likely contains a {label} ." ,
             f"This looks like a {label} ." ,
        ]
        
        opening_sentence = random_choice(phrases)

        return(
                f"{opening_sentence}.\n"
                f"I am {confidence}% confident about this prediction.\n" 
                f"{description}\n"
                f"The image format is {metadata['Format']} "
                f"with an estimated resolution of {metadata['Resolution']}."
        )  


    except Exception as  e :
        return f"Error analyzing image:{str(e)}"
    
if __name__ == "__main__":
    image_path = input("Enter image path: ")
    result = vision_tool(image_path)
    print(result) 