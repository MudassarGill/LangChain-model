from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain.output_parsers import StrcutureOutputParser,ResponseSchema
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

    }
)

schema=[
    ResponseSchema(name="review",description="review of the topic"),
    ResponseSchema(name="rating",description="rating out of 5")
]

parser=StrcutureOutputParser(schema=schema)

prompt=PromptTemplate(
    template='write a detiled review of the following topic {topic} and also give a rating out of 5',
    input_variables=["topic"],
    output_parser=parser
)

chain=prompt|model|parser

result=chain.invoke({"topic":"Babar Azam"})

print(result)