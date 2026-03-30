from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from transformers import logging
import warnings

# 🔇 warnings band karo
warnings.filterwarnings("ignore")
logging.set_verbosity_error()

# ✅ LLM setup (clean)
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.5,
        "max_new_tokens": 100,
        "do_sample": True
    }
)

# ✅ Chat wrapper
model = ChatHuggingFace(llm=llm)

# ✅ Response
response = model.invoke("Who is Babar Azam?")

# 🔥 Clean output only
print(response.content)