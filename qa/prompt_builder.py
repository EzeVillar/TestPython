def build_prompt(question, chunks):
    context = "\n\n".join(f"[{c['id']}]\n{c['text']}" for c in chunks)
    prompt = (
        "You are a helpful assistant. Using ONLY the context below, answer the user's question.\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {question}"
    )
    return prompt