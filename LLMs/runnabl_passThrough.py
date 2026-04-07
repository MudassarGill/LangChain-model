from langchain_huggingface import HuggingFacePipeline,ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.runnables import RunnablePassthrough,RunnableParallel,RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model=HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
   
)

prompt1=PromptTemplate(
    template='write a joke on {topic}',
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template='write a detailed summmary of the following text \n {text}',
    input_variables=["text"]
)

parser=StrOutputParser()


joke_gen_chain=RunnableSequence(
    prompt1,
    model,
    parser
)


parallel_chain=RunnableParallel(
    {
        'joke':RunnablePassthrough(),
        'explnations':RunnableSequence(prompt2,model,parser),
    }
)

final_chain=RunnableSequence(
    parallel_chain,joke_gen_chain

)

result=final_chain.invoke({'topic': 'cricket'})
print(result)
