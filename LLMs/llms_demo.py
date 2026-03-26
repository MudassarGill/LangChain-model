from langchain_openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

llm=OpenAI('gpt-3.5-turbo-instruct')

llm.invoke()

