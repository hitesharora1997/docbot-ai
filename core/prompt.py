def build_prompt(query: str, context_chunks: list[str]) -> str:
    context_text = "\n\n".join([f"- {chunk.strip()}" for chunk in context_chunks])

    prompt = f"""
You are a smart assistant. Use the context below to answer the question.
Only use the context — do not make things up.

Context:
{context_text}

Question:
{query}

Answer in 3–5 sentences based only on the context.
""".strip()

    return prompt
