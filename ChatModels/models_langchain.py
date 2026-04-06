from langchain_huggingface import ChatHuggingFace
from langchain.promot import PromptTemplate
from langchain.parse import StrOutputParser
from dotenv import load_dotenv
from pydantic import Basemodel
from typing import Field,Optional
import pandas as pd 
import numpy as np 
import os 
import sys


load_dotenv()

model=ChatHuggingFace('prism-ml/Bonsai-8B-gguf')
promot=PromptTemplate(
      input_variables=["job"],
      template="Write a job application email for {job}",
)

parser=StrOutputParser()

chain=promot | model | parser

result=chain.invoke({"job":"Software Engineer"})

print(result)

