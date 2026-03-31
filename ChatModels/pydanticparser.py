from langchain_huggingface import ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatHuggingFace.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={"temperature": 0.5}
)

class Person(BaseModel):
    name: str = Field(description='Name of the person')
    age: int = Field(description='Age of the person')
    city: str = Field(description='City of the person')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='''
Generate name, age and city of a fictional {place} person.
Return ONLY valid JSON.
{format_instructions}
''',
    input_variables=['place'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

prompt = template.invoke({'place': 'Multan'})
result = model.invoke(prompt)

print("RAW OUTPUT:\n", result.content)   # debug

final_result = parser.parse(result.content)

print("\nPARSED OUTPUT:\n", final_result)