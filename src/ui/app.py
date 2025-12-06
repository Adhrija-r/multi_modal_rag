import streamlit as st
from src.retriever.retriever import retrieve
from src.generation.qa_generator import generate_answer

st.set_page_config(page_title="Multi-Modal RAG System", layout="wide")
st.title("📘 Multi-Modal RAG Demo")

query = st.text_input("Enter your question:")

if st.button("Search"):
    if not query.strip():
        st.error("Please type a question first.")
    else:
        with st.spinner("Retrieving context..."):
            chunks = retrieve(query, k=5)

        with st.expander("Retrieved Chunks"):
            for c in chunks:
                st.write(f"**Page {c.get('page')}** — {c.get('text')[:300]}...")

        answer = generate_answer(query, chunks)
        
        st.subheader("🧠 Answer")
        st.write(answer)
