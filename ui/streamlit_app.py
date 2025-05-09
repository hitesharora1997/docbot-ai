import streamlit as st
import asyncio
import sys
import os

# Add root path to sys.path before doing any imports from core/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Now import from the core module
from core.llm_client import ask_gemini

st.set_page_config(page_title="DocBot", layout="wide")
st.title("📄 Ask Your Docs (Gemini-powered Chatbot)")

query = st.text_input("Ask a question about your documents:")

if st.button("Ask") and query:
    with st.spinner("Thinking..."):
        answer = asyncio.run(ask_gemini(query))
        st.markdown("### 💬 Answer:")
        st.write(answer)
