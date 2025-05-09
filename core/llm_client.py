import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")  # Explicit path

async def ask_gemini(prompt: str) -> str:
    try:
        response = await model.generate_content_async(prompt)
        return response.text.strip() if response.text else "No response from Gemini."
    except Exception as e:
        print(f"Gemini error: {e}")
        return f"Gemini error: {e}"

