import os
def generate_answer(query, retrieved_chunks):
    # Simple deterministic template — replace with your LLM call
    ctx = "\n\n".join([f"(page {c.get('page')}) {c.get('text')[:500]}" for c in retrieved_chunks])
    answer = f"Question: {query}\n\nContext: {ctx}\n\nAnswer: (use the context above; include citations like (page N))."
    return answer