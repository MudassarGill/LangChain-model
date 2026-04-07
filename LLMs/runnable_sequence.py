from langchain_huggingface import HuggingFacePipeline,ChatHuggingFace,HuggingFaceEndpoint
from langchain.core.prompts import PromptTemplate
from langchain.core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

model=HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.5,
    }
)

prompt=PromptTemplate(
    template='write a joke on {topic}',
    input_variables=["topic"]
)

parser=StrOutputParser()


chain=RunnableSequence(prompt,model,parser)
result =chain.invoke({'topic': 'AI'})
print(result)