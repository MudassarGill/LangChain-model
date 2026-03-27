from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import os 
import numpy as np 


load_dotenv()

model=HuggingFaceEndpoint(
    repo_id="google/flan-t5-base",
    task="text-generation",
)

model=ChatHuggingFace(llm=model)

response=model.invoke("What is the capital of Pakistan?")

print(response)
