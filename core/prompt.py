def build_prompt(query: str, context_chunks: list[str], max_chunks=3) -> str:
    context = "\n\n".join(context_chunks[:max_chunks])

    prompt = f"""
You are a knowledgeable and helpful assistant.

Use the following context to answer the user's question. If the context contains relevant details, summarize or explain them in a clear, confident way. You can combine ideas across multiple context chunks if it helps. Avoid saying "sorry" or "I can't" — do your best using the information given.

Only use the context. Do not make up facts.

---

Context:
{context}

---

Question: {query}

Answer:
""".strip()

    return prompt
