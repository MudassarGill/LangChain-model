from langchain_core.runnables import RunnableSequence
from langchain_huggingface import HuggingFacePipeline,ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model=HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    
)

prompt1=PromptTemplate(
    template='Genrate a tweet on {topic}',
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template='Genrate a post for Linkedin on {topic}',
    input_variables=["topic"]
)



parser=StrOutputParser()

parallel_chain=RunnableParallel(
     {
        'tweet':RunnableSequence(prompt1,model,parser),
        'linkedin':RunnableSequence(prompt2,model,parser)
     }
)

result=parallel_chain.invoke({'topic': 'AI'})
print(result)