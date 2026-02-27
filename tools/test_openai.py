from openai import OpenAI 

client = OpenAI()
response = client.responses.create(
    model= "gpt-4.1-mini",
    input = "Say hello in one short sentence."
)
print(response.output_text)