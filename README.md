# 🔍 HackGeek Research Agent

An intelligent research agent with persistent memory, built for the HackGeek Hackathon by GeekRoom.

## 🚀 What It Does

HackGeek Research Agent answers research queries using a full RAG (Retrieval-Augmented Generation) pipeline. It remembers past sessions per user, retrieves relevant context from a vector database, and generates detailed answers using a fast LLM.

## 🧠 Architecture
```
User Query
    ↓
Router (quick / deep mode detection)
    ↓
Memory Retrieval (Qdrant vector DB)
    ↓
LLM Answer Generation (Groq + Llama 3)
    ↓
Memory Storage (Qdrant)
    ↓
Response (Answer + Memory + Metrics)
```

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Frontend | Streamlit |
| LLM | Groq (Llama 3.1 8B) |
| Vector DB | Qdrant Cloud |
| Embeddings | Ollama (nomic-embed-text) |
| Memory | Qdrant (user_preferences, research_history, key_facts) |

## ✨ Features

- **Fast responses** via Groq API (under 2 seconds)
- **Persistent memory** — remembers past research per user
- **Quick & Detailed modes** — auto-detected or manually selected
- **Per-user sessions** — separate memory for each user ID
- **Metrics tracking** — latency and cost per query
- **Debug info** — model, context used, Qdrant hits
- **100% free to run** — Groq free tier + Qdrant free tier + Ollama local

## 📦 Installation

### 1. Clone the repo
```bash
git clone https://github.com/yourname/hackgeek-research-agent
cd hackgeek-research-agent/tech_research_agent
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Install and start Ollama
Download from [ollama.com](https://ollama.com) then run:
```bash
ollama pull nomic-embed-text
ollama serve
```

### 4. Set up environment variables
Create a `.env` file in the `tech_research_agent` folder:
```
GROQ_API_KEY=your_groq_api_key
QDRANT_URL=your_qdrant_cluster_url
QDRANT_API_KEY=your_qdrant_api_key
```

- Get Groq API key free at [console.groq.com](https://console.groq.com)
- Get Qdrant free cluster at [cloud.qdrant.io](https://cloud.qdrant.io)

### 5. Initialize Qdrant collections
```bash
python memory/qdrant_db.py
```

### 6. Run the app
```bash
streamlit run app.py
```

## 📁 Project Structure
```
tech_research_agent/
├── app.py                  # Streamlit UI
├── core/
│   ├── agent_controller.py # Main agent orchestrator
│   ├── executor.py         # Groq LLM calls
│   ├── router.py           # Quick/deep mode detection
│   └── clarifier.py        # Query clarification
├── memory/
│   ├── qdrant_db.py        # Qdrant client + collections
│   ├── retrieve.py         # Vector retrieval
│   └── store.py            # Vector storage
├── retrieval/
│   └── citation.py         # Citation handling
├── .env                    # API keys (not committed)
└── requirements.txt
```

## 🎯 How Memory Works

Every query is embedded using `nomic-embed-text` and stored in Qdrant under the user's ID. On the next query, relevant past research, preferences, and key facts are retrieved and injected into the prompt — making answers smarter over time.

## 👨‍💻 Built By

Raj — HackGeek Hackathon, GeekRoom 2026

