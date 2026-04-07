from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnableLambda,RunnablePassthrough,RunnableBranch
from langchain_huggingface import HuggingFacePipeline,ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

def word_counter(text):
    return len(text.split())

model=HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
   
)

prompt=PromptTemplate(
    template='write a joke on {topic}',
    input_variables=["topic"]
)



parser=StrOutputParser()

joke_gen_chain=RunnableSequence(
    prompt,
    model,
    parser
)

parallel_chain=RunnableParallel(
    {
        'joke':RunnablePassthrough(),
        'word_count':RunnableLambda(word_counter)
    }
)

final_chain=RunnableSequence(
    joke_gen_chain,
    parallel_chain
)

result=final_chain.invoke({'topic': 'cricket'})
print(result)