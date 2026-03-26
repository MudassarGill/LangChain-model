import os
from langchain_openai import OpenAI

os.environ["OPENAI_API_KEY"] = "sk-xxxxxxxx"

llm = OpenAI(model="gpt-3.5-turbo-instruct")

response = llm.invoke("What is the capital of Pakistan")

print(response)