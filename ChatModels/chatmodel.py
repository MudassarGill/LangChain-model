from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage,SystemMessage
from dotenv import load_dotenv

load_dotenv()


model = ChatOpenAI(model="gpt-4o-mini", temperature=0,max_completion_tokens=10)

massage=[
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="What is the capital of Pakistan")
]

response=model.invoke(massage)

print(response.content)