# 🧠 DocBot AI

A professional-grade, private chatbot that answers questions based on your own documents using retrieval-augmented generation (RAG) and Google Gemini. Built with FastAPI, ChromaDB, Sentence Transformers, and clean architecture.

---

## 🚀 Features

- 🔍 Semantic search over your documents
- 🧩 Chunking & embedding of raw text files
- 💬 Real-time QA powered by Google Gemini
- 🧠 Local embeddings via `sentence-transformers`
- 🧱 Modular, SOLID code structure
- 🐳 Dockerized for production use
- ✅ Ready for AWS/Azure deployment

---

## 🏗️ Project Architecture


---

## 🛠️ Tech Stack

| Area              | Tool/Library                         |
|-------------------|--------------------------------------|
| Backend API       | FastAPI                              |
| Embeddings        | Sentence Transformers (`all-MiniLM`) |
| Vector Store      | ChromaDB                             |
| LLM (response)    | Google Gemini API                    |
| Chunking          | LangChain's `RecursiveTextSplitter` |
| Deployment        | Docker, GitHub Actions               |

---

## ⚙️ Getting Started

### 1. Clone & Install

```bash
git clone https://github.com/yourusername/docbot-ai.git
cd docbot-ai
pip install -r requirements.txt
```