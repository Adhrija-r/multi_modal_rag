from src.embeddings.embedder import embed_texts
from src.index.vector_store import load_index, search
import numpy as np

def retrieve(query, k=5):
    index, meta = load_index()
    if index is None:
        return []
    q_emb = embed_texts([query])
    D, I = search(index, np.array(q_emb).astype('float32'), k=k)
    results = []
    for idx in I[0]:
        if idx == -1: continue
        results.append(meta[idx])
    return results
