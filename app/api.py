from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from core.retriever import retrieve_similar_chunks
from core.prompt import build_prompt
from core.llm_client import ask_gemini

router = APIRouter()

class ChatRequest(BaseModel):
    query: str

@router.post("/chat")
async def chat(request: ChatRequest):
    try:
        chunks, meta = retrieve_similar_chunks(request.query)
        top_chunks = chunks[:3]
        prompt = build_prompt(request.query, top_chunks)
        print("==== PROMPT ====")
        print(prompt[:300], "...\n================")
        answer = await ask_gemini(prompt)
        return {
            "query": request.query,
            "answer": answer,
            "source_chunks": chunks,
            "metadata": meta
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")
