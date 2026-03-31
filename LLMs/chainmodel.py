from langchain_huggingface import HuggingFaceEndpoint,HuggingFacePipeline
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
import os 
import numpy as np 

load_dotenv()

model=HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        
        "temperature": 0.5,

    }
)

template=PromptTemplate(
    template='Genarate 5 intersting fact about this {topic}',
    input_variables=["topic"]
)

parser=StrOutputParser()


chain = template | model | parser

result = chain.invoke({"topic": "Pakistan"})

print(result)