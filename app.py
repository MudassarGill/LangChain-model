from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from contextlib import asynccontextmanager
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import warnings
import transformers
import os

warnings.filterwarnings("ignore")
transformers.logging.set_verbosity_error()

# Global dict to hold our model
ml_models = {}

# Global list to hold chat history
chat_history = [
    SystemMessage(content="You are a helpful, smart, and concise AI programming assistant.")
]

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Loading TinyLlama model... This might take a minute...")
    llm = HuggingFacePipeline.from_model_id(
        model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        task="text-generation",
        pipeline_kwargs={
            "temperature": 0.5,
            "max_new_tokens": 512, # increased token limit for code generation
            "do_sample": True,
            "return_full_text": False # Attempt to prevent returning prompt
        }
    )
    ml_models["chat"] = ChatHuggingFace(llm=llm)
    print("Model loaded successfully! You can now chat.")
    yield
    ml_models.clear()

app = FastAPI(lifespan=lifespan)

# Ensure static folder exists
os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

class ChatRequest(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
async def get_frontend():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/clear")
async def clear_chat():
    global chat_history
    chat_history = [
        SystemMessage(content="You are a helpful, smart, and concise AI programming assistant.")
    ]
    return {"status": "cleared"}

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    global chat_history
    model = ml_models.get("chat")
    if not model:
        return {"response": "Model is still loading... Please wait a moment."}
    
    try:
        # Add user's new message to history
        chat_history.append(HumanMessage(content=request.message))
        
        # Pass the entire history to the model
        response = model.invoke(chat_history)
        output_text = response.content

        # Strict cleaning to remove <|user|>, <|assistant|>, and repeats
        if "<|assistant|>" in output_text:
            output_text = output_text.split("<|assistant|>")[-1]
        
        output_text = output_text.replace("</s>", "").strip()
        
        # Save AI's response to history
        chat_history.append(AIMessage(content=output_text))

        return {"response": output_text}
    except Exception as e:
        # If error occurs, remove the last human message so it doesn't break future context
        if chat_history and isinstance(chat_history[-1], HumanMessage):
            chat_history.pop()
        return {"response": f"An error occurred: {str(e)}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
