from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnableLambda,RunnablePassthrough,RunnableBranch
from langchain_huggingface import HuggingFacePipeline,ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()



prompt1=PromptTemplate(
    template='write a detalied report on {topic}',
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template='summarize the following text \n {text}',
    input_variables=["text"]
)

parser=StrOutputParser()

model=HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
   
)


report_gen_chain=RunnableSequence(
    prompt1,
    model,
    parser
)

branch_chain=RunnableBranch(
    (lambda x: len(x.split())>500,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

final_chain=RunnableSequence(
    report_gen_chain,
    branch_chain
)

result=final_chain.invoke({'topic': 'Russia vs Ukraine war'})
print(result)