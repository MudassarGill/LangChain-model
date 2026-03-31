from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Optional
import os 
import numpy as np 

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

class Review(BaseModel):
    rating: int
    summary: str
    sentiment: str

parser=PydanticOutputParser(pydantic_object=Review)

template=PromptTemplate(
    template='Give a review of the following topic {topic} \n {format_instructions}',
    input_variables=["topic"],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

prompt=template.invoke({"topic":"Babar Azam"})
result=model.invoke(prompt)
final_result=parser.parse(result.content)
print(final_result)