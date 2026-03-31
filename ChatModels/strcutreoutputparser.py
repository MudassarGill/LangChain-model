from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
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

schema = [
    ResponseSchema(name="fact1", description="fact 1 about the topic"),
    ResponseSchema(name="fact2", description="fact 2 about the topic"),
    ResponseSchema(name="fact3", description="fact 3 about the topic"),
    ResponseSchema(name="fact4", description="fact 4 about the topic"),
    ResponseSchema(name="fact5", description="fact 5 about the topic")
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 5 facts about {topic}.\n{format_instructions}',
    input_variables=["topic"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

prompt = template.invoke({"topic": "Babar Azam"})
result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)