from langchain_huggingface import ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv



load_dotenv()

model=ChatHuggingFace.from_model_id(
    model_id='prism-ml/Bonsai-8B-gguf',
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.5,
    }
)
promot=PromptTemplate(
      input_variables=["job"],
      template="Write a job application email for {job}",
)

parser=StrOutputParser()

chain=promot | model | parser

result=chain.invoke({"job":"Software Engineer"})

print(result)

