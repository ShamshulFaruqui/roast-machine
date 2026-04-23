# 🔥 AI Roast Machine

A multimodal AI app that roasts you based on what you tell it or show it. Built with LangChain, Groq, and Streamlit.

---

## What it does

- **Text roast** — describe yourself and get roasted by the AI
- **Photo roast** — upload a photo and the AI analyses it and roasts what it sees
- **Fire back** — keep the roast battle going with a back-and-forth chat
- **Guardrails** — prompt injection and harmful content are blocked before reaching the AI
- **RAG-powered** — the AI reads a knowledge base of comedy techniques before every roast

---

## Tech stack

| Tool | Purpose |
|---|---|
| Groq (LLaMA 3.3) | Main LLM for text generation |
| Groq Vision (LLaMA 4 Scout) | Image analysis for photo roasts |
| LangChain | Agent orchestration and chaining |
| Chroma | Vector store for RAG knowledge base |
| LangSmith | Tracing and monitoring of LLM calls |
| Streamlit | Frontend UI and deployment |

---

## How to run locally

**1. Clone the repo**
```bash
git clone https://github.com/ShamshulFaruqui/roast-machine.git
cd roast-machine
```

**2. Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Add your API keys**

Create a `.env` file in the root folder:

GROQ_API_KEY=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
LANGCHAIN_API_KEY=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
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_PROJECT=RoastMachine

**5. Run the app**
```bash
streamlit run app.py
```

---

## Live demo

🔗 [roast-machine.streamlit.app](https://roast-machine.streamlit.app)

---

## Project structure
roast-machine/
├── app.py           # Streamlit frontend
├── roaster.py       # LangChain roast agents
├── guardrails.py    # Input/output safety checks
├── rag.py           # Chroma RAG knowledge base
├── requirements.txt
├── GRANDMA.md
└── .env             # Not committed — add your own keys

---

## AI criteria covered

- ✅ Working AI application
- ✅ RAG + vector store (Chroma)
- ✅ Guardrails + prompt injection defence
- ✅ LangChain agentic framework
- ✅ Multimodal input (text + image)
- ✅ Chatbot with session memory
- ✅ LangSmith tracing and monitoring
- ✅ Deployed live on Streamlit Cloud

---

## Problem statement

Existing AI chatbots are too polite and overly cautious - there's no tool that delivers sharp, witty, personalised humour while still maintaining guardrails against genuinely harmful content.

---

