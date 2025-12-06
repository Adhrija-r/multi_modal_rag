import streamlit as st
from src.ingestion.pdf_parser import parse_pdf
from src.chunking.chunker import chunk_text
from src.embeddings.embedder import embed_chunks
from src.retriever.retriever import retrieve
from src.generation.qa_generator import generate_answer

st.title("📄 Multi-Modal RAG System")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    with open("uploaded.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PDF uploaded successfully!")

    if st.button("Process PDF"):
        with st.spinner("Parsing PDF..."):
            pages = parse_pdf("uploaded.pdf")

        with st.spinner("Chunking text..."):
            chunks = chunk_text(pages)

        with st.spinner("Embedding text..."):
            embed_chunks(chunks)

        st.success("PDF processed and indexed!")

query = st.text_input("Ask a question about the PDF:")

if st.button("Get Answer"):
    if not query.strip():
        st.warning("Enter a question first.")
    else:
        with st.spinner("Retrieving info..."):
            retrieved = retrieve(query)

        answer = generate_answer(query, retrieved)

        st.subheader("Answer:")
        st.write(answer)
