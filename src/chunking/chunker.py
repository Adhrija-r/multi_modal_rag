# very small chunker: splits text into paragraph chunks
import uuid

def chunk_text(pages):
    chunks = []
    for p in pages:
        text = p.get("text","")
        paras = [t.strip() for t in text.split("\n\n") if t.strip()]
        for para in paras:
            # if para too long, split roughly
            for i in range(0, len(para), max_chars):
                chunk_text = para[i:i+max_chars]
                chunks.append({
                    "id": str(uuid.uuid4()),
                    "page": p.get("page"),
                    "text": chunk_text
                })
    return chunks