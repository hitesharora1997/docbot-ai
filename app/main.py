from fastapi import FastAPI
from app.api import router

app = FastAPI(title="DocBot AI")
app.include_router(router)

@app.get("/")
def health_check():
    return {"message": "✅ DocBot AI is running. Use /chat endpoint for queries."}
