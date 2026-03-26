import os
from langchain_openai import ChatOpenAI

os.environ["OPENAI_API_KEY"] = "sk-xxxxxxxx"

llm = ChatOpenAI(model="gpt-4o-mini")

response = llm.invoke("What is the capital of Pakistan")

print(response.content)