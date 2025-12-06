import faiss
import numpy as np
import pickle
from pathlib import Path

INDEX_PATH = "data/faiss.index"
META_PATH = "data/faiss_meta.pkl"

def build_index(embeddings, metadatas, dim=None):
    if dim is None:
        dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    Path("data").mkdir(parents=True, exist_ok=True)
    faiss.write_index(index, INDEX_PATH)
    with open(META_PATH, "wb") as f:
        pickle.dump(metadatas, f)
    return index

def load_index():
    if not Path(INDEX_PATH).exists():
        return None, None
    index = faiss.read_index(INDEX_PATH)
    import pickle
    with open(META_PATH, "rb") as f:
        meta = pickle.load(f)
    return index, meta

def search(index, q_emb, k=5):
    D, I = index.search(q_emb, k)
    return D, I