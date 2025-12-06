from sentence_transformers import SentenceTransformer
_model = None

def get_model(name="all-mpnet-base-v2"):
    global _model
    if _model is None:
        _model = SentenceTransformer(name)
    return _model

def embed_texts(texts):
    model = get_model()
    emb = model.encode(texts, show_progress_bar=False)
    return emb