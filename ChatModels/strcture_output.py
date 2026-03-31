from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from dotenv import load_dotenv
import os 
import numpy as np 
from typing import TypedDict

load_dotenv()

model=ChatHuggingFace.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        
        "temperature": 0.5,
        "max_new_tokens": 100,
        "do_sample": True
    }
)


class Review(TypedDict):
    rating: int
    summary: str
    sentiment: str

structed_model=model.with_structured_output(Review)



result=structed_model.invoke("This product is amazing! I love it.")

print(result)
