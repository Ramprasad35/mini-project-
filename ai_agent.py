import re
conversation_memory = []
last_topic = None
document_text = ""
document_chunks = []

def system_prompt(): 
    return """
You are an AI knowledge assistant.
Your job is to understand the user's question
and decide what action is required.
Only use available tools.
"""

def get_user_input():
    print("Waiting for user input...")
    return input("User: ")
def agent_decision(user_input):
    if "define" in user_input.lower():
        return "definition_tool"
    elif "example" in user_input.lower():
        return "example_tool"
    else:
        return "default_tool"

def detect_intent(user_input):
    user_input = user_input.lower()
    
    if "load document" in user_input:
        return "load_document"

    elif "document" in user_input:
        return "document_question"
    
    elif "define" in user_input or "what is " in user_input:
        return "definition"   
    
    elif "example" in user_input:
        return "example"
    
    elif "exit" in user_input or "quit" in user_input:
        return "exit"
    
    elif "memory" in user_input:
        return "memory"
    
    elif "last_topic" in user_input:
        return "last topic"

    else:
        return "unknown"

def extract_topic(user_input):
    cleaned = user_input.lower()

    for phrase in  ["what is ","define","explain","example","of","?" , "document"]:      
        cleaned = cleaned.replace(phrase,"")

    return cleaned.strip().title()
        

def definition_tool(topic):
    print("DEBUG Tool received:", repr(topic))
    topic = topic.strip().title()
    definition = {
        "Ai": "Artificial Intelligence (AI) refers to machines designed to perform tasks that normally require human intelligence.",
        "Machine Learning": "Machine Learning is a subset of AI where systems learn patterns from data.",
        "Neural Networks": "Neural Networks are models ins  pired by the human brain used in deep learning."
    }
    return definition.get(topic,f"Sorry,I don't have a definiton for {topic}.")

def example_tool(topic):
    topic = topic.strip().title()
    examples = {
        "Ai": "Example: A voice assistant like Siri or Alexa.",
        "Machine Learning": "Example: Email spam detection.",
        "Neural Networks": "Example: Image recognition systems."  
    }
    return examples.get(topic,f"Sorry,I don't have an  example for {topic}.")

def default_tool(topic):
    return f"I still learning.Please ask a clearer question"

def show_memory():
    print("DEBUG Memory contents:", conversation_memory)

    if not conversation_memory:
        return "No conversation memory yet."
    
    history = ""
    for role,text in conversation_memory:
        history += f"{role}: {text}\n"
    return history 

def clean_text(text):
    return re.sub(r"[^\w\s]", "",text.lower())

def chunk_text(text , chunk_size=1):
    sentences = re.split(r'(?<=[.!?])\s*|\n\n+',text)
    sentences = [s.strip() for s in sentences if s.strip()]  
    chunks = [] 

    for i in range(0, len(sentences), chunk_size):
        chunk = " ".join(sentences[i:i+chunk_size])
        chunks.append(chunk)   

    return chunks 

def load_document (filename): 
    global document_text, document_chunks

    try:
        with open(filename, "r", encoding="utf-8") as file:
            document_text = file.read()
            document_chunks = chunk_text(document_text)
            print ("DEBUG -> dOCUMENT LOADED SUCCESFULLY")
            print("DEBUG ->length:" ,len(document_text))
        return f"Document '{filename}' loaded successfully."
    
    except FileNotFoundError:
        return "Sorry,I could not find that file ."
    
    except Exception as e:
        print("DEBUG -> ERROR:" , str(e))
        return f"Error loading document:{str(e)}"
    

def document_tool(question):    
    global document_chunks
    cleaned_question = clean_text(question)
    words = cleaned_question.split()
    print("DEBUG -> File read",document_text) 

    stop_words = ['document', 'what', 'is', 'the', 'a', 'an', 'how', 'why', 'when', 'where']

    keywords = [w for w in words if len(w)>2 and w not in stop_words]

    if not document_chunks:
        return "No document loaded. Please load a document first."      
    
    best_chunk = None 
    best_score = 0 
    
    for chunk in document_chunks:
        cleaned_chunk = clean_text(chunk)
        chunk_words = cleaned_chunk.split()

        score = sum(1 for keyword in keywords if keyword in chunk_words)

        if score > best_score:
            best_score = score 
            best_chunk = chunk 

    if best_chunk and best_score > 0 :
             return f"relavent info found: \n{best_chunk}"                       

    else:
        return "I could not find relevant information in the document."
    
def extract_filename(user_input):
    return user_input.lower().replace("load document","").strip()
    
def main():
    global last_topic
    print(system_prompt().strip()) 

    while True:
        user_input = get_user_input()
            
        intent = detect_intent(user_input)
        print("DEBUG Intend:", repr(intent))

        if intent != "memory":
            conversation_memory.append(("User",user_input))             


        topic = extract_topic(user_input)

        if not topic and last_topic:
            topic = last_topic
            print (f"DEBUG Using last topic: {repr(topic)}")

        if topic:
            last_topic = topic                                                                     

        if intent == "definition":
            print("DEBUG → Entered definition branch")                                   
            response = definition_tool(topic)

        elif intent == "example":
            response = example_tool(topic)
            

        elif intent == "exit":
            print("Agent:Goodbye") 
            break

        elif intent == "memory":
            response = show_memory()

        elif intent == "load_document":
              filename = extract_filename(user_input)
              response = load_document(filename)

        elif intent == "document_question":
              response = document_tool(user_input)

        else:
            response = "I'm not sure what do you mean.Can you rephrase "

        if intent != "memory":
              conversation_memory.append(("Agent",response))

        print("Agent:",response)
    
if __name__ == "__main__":
        main()
