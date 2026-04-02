from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os 
import numpy as np 

load_dotenv()

model1=HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        
        "temperature": 0.5,

    }
)

model2=HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        
        "temperature": 0.5,

    }
)

template1=PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=["topic"]
)
template2=PromptTemplate(
    template='write a 5 pointer summary of the following text \n {text}',
    input_variables=["text"]
)

parser=StrOutputParser()


chain=template1 | model | parser|template2 | model | parser

result=chain.invoke({"topic":"Pakistan"})

print(result)