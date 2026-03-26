from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0,max_completion_tokens=10)

response=model.invoke("What is the capital of Pakistan")

print(response.content)