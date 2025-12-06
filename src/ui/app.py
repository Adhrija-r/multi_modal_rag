import streamlit as st
import os
import json

from src.chunking.chunk_pdf import chunk_pdf
from src.embeddings.embedder import embed_texts
from src.index.index_builder import build_faiss_index
from src.retriever.retriever import retrieve
from src.generation.qa_generator import generate_answer

DATA_DIR = "data"
PARSED_DIR = os.path.join(DATA_DIR, "parsed")
CHUNKS_FILE = os.path.join(DATA_DIR, "chunks.json")

os.makedirs(PARSED_DIR, exist_ok=True)

st.set_page_config(page_title="Multimodal RAG System", layout="wide")

st.title("📄 Multi-Modal RAG System")
st.write("Upload a PDF → Process → Ask questions → View citations")

# ==============================
# Upload PDF
# ==============================
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    pdf_path = os.path.join(PARSED_DIR, uploaded_file.name)

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("PDF uploaded successfully!")
    st.write("File saved to:", pdf_path)

    # ==============================
    # Chunking
    # ==============================
    st.subheader("📌 Step 1: Parsing & Chunking")
    chunks = chunk_pdf(pdf_path)

    with open(CHUNKS_FILE, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2)

    st.success(f"Chunking complete! {len(chunks)} chunks created.")
    st.json(chunks[:3])   # preview first 3 chunks

    # ==============================
    # Embeddings + Vector Index
    # ==============================
    st.subheader("📌 Step 2: Embeddings & FAISS Index")

    texts = [c["text"] for c in chunks]
    vectors = embed_texts(texts)

    index = build_faiss_index(vectors)

    st.success("FAISS index created successfully!")

# ==============================
# Ask question
# ==============================
st.subheader("🔎 Ask a question about the document")

query = st.text_input("Enter your question:")

if st.button("Generate Answer"):
    if not os.path.exists(CHUNKS_FILE):
        st.error("Please upload and process a PDF first.")
    else:
        with open(CHUNKS_FILE, "r", encoding="utf-8") as f:
            chunks = json.load(f)

        # Retrieve
        retrieved_chunks = retrieve(query, k=5)

        st.write("### 📌 Retrieved Context Chunks")
        for c in retrieved_chunks:
            st.write(f"**Page {c['page']}** — {c['text'][:250]}...")

        # Generate Answer
        final_answer = generate_answer(query, retrieved_chunks)

        st.write("### 🧠 Final Answer")
        st.success(final_answer)# paste the app.py content here (from above)
