from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.core.output_parsers import StrOutputParser
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

template1=PromptTemplate(
    template='write a detiled review of the following topic {topic} and also give a rating out of 5',
    input_variables=["topic"]
)
template2=PromptTemplate(
    template='write a 5 line summary of the following text {text}',
    input_variables=["text"]
)


