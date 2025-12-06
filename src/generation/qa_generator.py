import sys
from src.retriever.retriever import retrieve
from src.embeddings.embedder import embed_texts

def generate_answer(query, retrieved_chunks):
    ctx = "\n\n".join([
        f"(page {c.get('page')}) {c.get('text')[:300]}"
        for c in retrieved_chunks
    ])
    answer = (
        f"Question: {query}\n\n"
        f"Context:\n{ctx}\n\n"
        f"Answer: (Based on the context above. Include page citations.)"
    )
    return answer

if __name__ == "__main__":
    # Take question from command-line argument
    if len(sys.argv) < 2:
        print("Usage: python qa_generator.py \"your question here\"")
        sys.exit(1)

    query = sys.argv[1]

    # Step 1: Retrieve relevant chunks
    retrieved = retrieve(query, k=3)

    # Step 2: Generate answer
    answer = generate_answer(query, retrieved)

    # Step 3: Print answer
    print("\n==================== RAG ANSWER ====================\n")
    print(answer)
    print("\n====================================================\n")