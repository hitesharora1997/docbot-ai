from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from app.api import router
import os

PORT = int(os.environ.get("PORT", 8000))


app = FastAPI(title="DocBot AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: replace with ["https://your-frontend.com"] in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html><body style="font-family: sans-serif; text-align: center; margin-top: 50px;">
      <h1>✅ DocBot AI is Running</h1>
      <p>This is a Gemini-powered document chatbot API.</p>
      <p>Use <a href='/docs'>/docs</a> to explore the API, or <strong>visit the Streamlit frontend.</strong></p>
    </body></html>
    """
