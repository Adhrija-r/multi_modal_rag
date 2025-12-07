📘 Multi-Modal Retrieval-Augmented Generation (RAG) System

This project implements a complete multi-modal Retrieval-Augmented Generation (RAG) pipeline, designed as part of an AI/ML internship assessment.
It demonstrates the ability to process documents, generate embeddings, store vectors, retrieve relevant information, and produce responses using LLMs — all following modular, scalable design principles.

🚀 Project Overview

The Multi-Modal RAG system enables:

Document ingestion (PDFs and text)

Text extraction & cleaning

Chunking using configurable strategies

Embedding generation

Vector database storage

Similarity search for retrieval

LLM-powered answer generation

(Optional) Streamlit-based UI

The architecture follows industry-standard patterns and is fully extensible for future development.

🧩 Features
📥 1. Document Ingestion
Extracts text from PDFs and pre-processes it for downstream modules.

✂️ 2. Intelligent Chunking
Splits text using customizable logic for optimal embedding performance.

🧠 3. Embeddings
Generates numerical vector representations for each chunk.

📚 4. Vector Store
Uses FAISS (or other stores) for efficient similarity search.

🔎 5. Retriever
Fetches the most relevant chunks for a user query.

📝 6. RAG Response Generator
Combines:
Retrieved context
User query
to generate high-quality answers.

🎨 7. Streamlit UI (Local)
A simple interface to upload documents and ask questions.

📁 Project Structure
multi_modal_rag/
│
├── src/
│   ├── ingestion/          # PDF/Text extraction modules
│   ├── chunking/           # Splitting logic
│   ├── embeddings/         # Embedding generator
│   ├── retriever/          # Vector search
│   ├── generation/         # LLM response generation
│   └── ui/                 # (Optional) Streamlit UI
│
├── docs/                   # Technical report, notes
├── demos/                  # Demo video or screenshots
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/Adhrija-r/multi_modal_rag.git
cd multi_modal_rag

2️⃣ Create a virtual environment
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

▶️ Running the RAG Pipeline
Run the backend modules

Each component can be executed independently for testing:

python src/ingestion/pdf_parser.py
python src/chunking/chunker.py
python src/embeddings/embedder.py
python src/retriever/search.py
python src/generation/generator.py

Running the Streamlit Interface (optional)
streamlit run src/ui/app.py

🧪 How the System Works
1. Ingestion
Extract text from PDF → returns raw text.

2. Chunking
Breaks long text into overlapping windows.

3. Embeddings
Each chunk → vector via embedding model.

4. Vector Store
FAISS index stores all chunk embeddings.

5. Retrieval
For each query:
Convert query → embedding
Retrieve top-k similar chunks

6. Generation
Send context + user query to the LLM.
