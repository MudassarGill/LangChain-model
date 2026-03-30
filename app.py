from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from contextlib import asynccontextmanager
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import warnings
import transformers
import os

warnings.filterwarnings("ignore")
transformers.logging.set_verbosity_error()

# Global dict to hold our model
ml_models = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Loading TinyLlama model... This might take a minute...")
    # Load the LLM exactly like chatmodel_local.py but increase max_new_tokens slightly
    llm = HuggingFacePipeline.from_model_id(
        model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        task="text-generation",
        pipeline_kwargs={
            "temperature": 0.5,
            "max_new_tokens": 150, 
            "do_sample": True
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
    # Return the HTML file directly on the root endpoint
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    model = ml_models.get("chat")
    if not model:
        return {"response": "Model is still loading... Please wait a moment."}
    
    try:
        response = model.invoke(request.message)
        return {"response": response.content}
    except Exception as e:
        return {"response": f"An error occurred: {str(e)}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
