from fastapi import APIRouter
from pydantic import BaseModel
from core.retriever import retrieve_similar_chunks
from core.prompt import build_prompt
from core.llm_client import ask_gemini

router = APIRouter()

class ChatRequest(BaseModel):
    query: str

@router.post("/chat")
def chat(request: ChatRequest):
    chunks, meta = retrieve_similar_chunks(request.query)
    top_chunks = chunks[:3]
    prompt = build_prompt(request.query, top_chunks)
    answer = ask_gemini(prompt)

    print("==== PROMPT ====")
    print(prompt)
    print("================")

    return {
        "query": request.query,
        "answer": answer,
        "source_chunks": chunks,
        "metadata": meta
    }
