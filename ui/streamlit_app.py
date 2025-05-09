# ui/streamlit_app.py
import streamlit as st
import os
import requests

# Config
BACKEND_API = os.getenv("BACKEND_API_URL", "http://localhost:8000/chat")

# Streamlit layout
st.set_page_config(page_title="DocBot AI", layout="centered")
st.title("📄 Ask Your Docs (Gemini-powered Chatbot)")

# Input
query = st.text_input("Ask a question from your documents:")

# Ask button
if st.button("Ask") and query:
    with st.spinner("Thinking..."):
        try:
            res = requests.post(BACKEND_API, json={"query": query})
            answer = res.json().get("answer", "No answer returned.")
        except Exception as e:
            answer = f"❌ Error: {str(e)}"

        st.markdown("### 💬 Answer")
        st.write(answer)
