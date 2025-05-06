# core/llm_client.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-pro")

def ask_gemini(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text.strip()
