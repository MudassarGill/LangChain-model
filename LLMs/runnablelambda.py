from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnableLambda
from langchain_huggingface import HuggingFacePipeline,ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

def word_counter(text):
    return len(text.split())


lambda_chain=RunnableLambda(word_counter)

result=lambda_chain.invoke("Hello, how are you?")
print(result)
