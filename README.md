# 🦜🔗 LangChain Model — Learning Repository

A hands-on learning repository exploring **LangChain** with multiple AI providers including OpenAI, Anthropic, Google Gemini, and HuggingFace (both API-based and fully local). This repo covers Chat Models, Output Parsers, Prompt Templates, Chains, and Structured Outputs — and includes a full **FastAPI + Web UI** for chatting with a local LLM.

---

## 📁 Project Structure

```
LangChain-model/
│
├── ChatModels/                   # All Chat Model experiments
│   ├── chatmodel.py              # OpenAI GPT-4o-mini chat model
│   ├── chatmodel_anthorpic.py    # Anthropic Claude chat model
│   ├── chatmodel_google.py       # Google Gemini chat model
│   ├── chatmodel_hf.py           # HuggingFace Endpoint (cloud) chat model
│   ├── chatmodel_local.py        # HuggingFace local model (TinyLlama)
│   │
│   ├── stroutputparse.py         # StrOutputParser + LangChain Chains
│   ├── jsonparser.py             # JsonOutputParser with PromptTemplate
│   ├── strcutreoutputparser.py   # StructuredOutputParser with ResponseSchema
│   ├── strcture_output.py        # with_structured_output() using TypedDict
│   ├── pydanticparser.py         # PydanticOutputParser with BaseModel
│   ├── pydantic2.py              # Pydantic BaseModel basics (practice)
│   ├── typedic.py                # TypedDict basics (practice)
│   ├── json_schema.json          # JSON Schema definition (Student model)
│   └── .env                      # API keys (not committed to git)
│
├── LLMs/                         # LLM (non-chat) experiments
│   ├── llms_demo.py              # OpenAI LLM (completion style)
│   └── .env                      # API keys
│
├── EmbaddedModels/               # Embedding models (coming soon)
│
├── static/                       # Web UI frontend files
│   ├── index.html                # Chat UI HTML page
│   ├── style.css                 # Dark-themed chat UI styles
│   └── script.js                 # Frontend JS logic
│
├── app.py                        # FastAPI backend — local TinyLlama chat server
├── requirements.txt              # All Python dependencies
├── .gitignore                    # Git ignore rules
├── LICENSE                       # MIT License
└── README.md                     # This file
```

---

## ✅ What We've Done So Far

### 🤖 1. Chat Models — Multi-Provider Support
Explored LangChain's `ChatModel` interface across 4 different AI providers:

| File | Provider | Model |
|------|----------|-------|
| `chatmodel.py` | OpenAI | `gpt-4o-mini` |
| `chatmodel_anthorpic.py` | Anthropic | `claude-3-5-sonnet` |
| `chatmodel_google.py` | Google | `gemini-2.5-flash` |
| `chatmodel_hf.py` | HuggingFace (API) | `TinyLlama-1.1B-Chat` |
| `chatmodel_local.py` | HuggingFace (Local) | `TinyLlama-1.1B-Chat` |

### 🧰 2. Output Parsers
Learned and implemented all major LangChain output parsers:

- **`StrOutputParser`** (`stroutputparse.py`) — Parses raw string output. Also used **chaining** (`chain1 | chain2`) to pipe multiple prompts together.
- **`JsonOutputParser`** (`jsonparser.py`) — Parses JSON-formatted responses from the model using format instructions.
- **`StructuredOutputParser`** (`strcutreoutputparser.py`) — Uses `ResponseSchema` to define expected fields (e.g., 5 facts about a topic).
- **`PydanticOutputParser`** (`pydanticparser.py`) — Uses a Pydantic `BaseModel` (`Person`) to validate and parse structured output (name, age, city).
- **`with_structured_output()`** (`strcture_output.py`) — Native structured output using `TypedDict` (Review: rating, summary, sentiment).

### 🔗 3. LangChain Chains
- Built sequential chains using the `|` pipe operator
- Example: `template1 | model | parser` → feeds result into `template2 | model | parser`

### 📋 4. Prompt Templates
- Used `PromptTemplate` with `input_variables` and `partial_variables`
- Injected `format_instructions` directly into prompts using output parsers

### 🧱 5. Pydantic & TypedDict Practice
- **`pydantic2.py`** — Practiced Pydantic `BaseModel` with optional fields
- **`typedic.py`** — Practiced `TypedDict` for typed chat history management
- **`json_schema.json`** — JSON Schema definition for a Student object

### 🖥️ 6. Local LLM + FastAPI Web App
Built a complete **local AI chatbot** using:
- **Model**: `TinyLlama/TinyLlama-1.1B-Chat-v1.0` (runs on your machine — no API key needed)
- **Backend**: `FastAPI` with lifespan model loading, `/chat` and `/clear` endpoints
- **Frontend**: Custom dark-themed chat UI (HTML + CSS + JS) in `static/`
- **Features**: Full conversation memory (chat history), error handling, clean token output

### 📦 7. LLM (Non-Chat) Example
- **`llms_demo.py`** — Used OpenAI's `gpt-3.5-turbo-instruct` with LangChain's `OpenAI` LLM class (completion-style, not chat-style)

---

## 🚀 What We're Working On / Coming Next

- [ ] **EmbeddedModels/** — Explore text embedding models (OpenAI, HuggingFace)
- [ ] **Vector Stores** — Store and search embeddings using FAISS or Chroma
- [ ] **RAG (Retrieval-Augmented Generation)** — Q&A over custom documents
- [ ] **Memory** — Add `ConversationBufferMemory` or `ConversationSummaryMemory`
- [ ] **Agents & Tools** — Build LangChain agents with custom tools
- [ ] **LangGraph** — Explore stateful multi-step agent workflows
- [ ] **More Parsers** — `XMLOutputParser`, `DatetimeOutputParser`, etc.

---

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/MudassarGill/LangChain-model.git
cd LangChain-model
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate       # Windows
# source venv/bin/activate  # Mac/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables
Create a `.env` file inside `ChatModels/` and `LLMs/`:
```env
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here
GOOGLE_API_KEY=your_google_key_here
HUGGINGFACEHUB_ACCESS_TOKEN=your_hf_token_here
```

---

## 🖥️ Running the Local Chat App (FastAPI)

```bash
python app.py
```

Then open your browser at **http://127.0.0.1:8000**

> ⚠️ First run will download `TinyLlama` model (~600MB). This is a one-time download.

---

## 🧪 Running Individual Scripts

```bash
# Run any ChatModel example
python ChatModels/chatmodel_local.py
python ChatModels/stroutputparse.py
python ChatModels/pydanticparser.py

# Run LLM example
python LLMs/llms_demo.py
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| `LangChain` | Core AI orchestration framework |
| `langchain-openai` | OpenAI GPT integration |
| `langchain-anthropic` | Anthropic Claude integration |
| `langchain-google-genai` | Google Gemini integration |
| `langchain-huggingface` | HuggingFace models (local + API) |
| `transformers` | HuggingFace model pipeline |
| `Pydantic` | Data validation & structured output |
| `FastAPI` | Backend API server |
| `python-dotenv` | Environment variable management |
| `NumPy / Scikit-learn` | ML utilities |

---

## 👨‍💻 Author

**Mudassar Hussain**  
AI/ML Engineer  
[GitHub](https://github.com/MudassarGill) | [Portfolio](https://mudassar-portfolio.onrender.com)

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.