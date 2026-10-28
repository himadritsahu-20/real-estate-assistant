# Real Estate Assistant

An AI-powered conversational assistant for real estate inquiries, leveraging Retrieval-Augmented Generation (RAG) to answer questions based on property documents, listings, and guidelines.

---

## Overview

The Real Estate Assistant uses language models combined with vector retrieval to provide grounded, accurate answers to client queries. By retrieving context from real estate documentation and property data, it reduces hallucinations and helps users quickly find relevant listing information.

---

## Features

- **Retrieval-Augmented Generation (RAG):** Queries vector embeddings of property listings and documentation to generate context-aware responses.
- **Python-Powered Backend:** Core execution flow and assistant endpoints driven by `main.py` and `rag.py`.
- **Modular Design:** Clear separation between prompt orchestration, retrieval logic, and application runtime.

---

## Repository Structure

```text
├── main.py            # Main application runner / API entry point
├── rag.py             # RAG logic (document chunking, embedding, retrieval, LLM prompt)
└── requirements.txt   # Python package dependencies

```

---

## Getting Started

### Prerequisites

* Python 3.9+
* An API key for your chosen LLM provider (e.g., OpenAI, Hugging Face, Cohere, etc.)

### 1. Clone the Repository

```bash
git clone [https://github.com/himadritsahu-20/real-estate-assistant.git](https://github.com/himadritsahu-20/real-estate-assistant.git)
cd real-estate-assistant

```

### 2. Set Up a Virtual Environment

```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Configure Environment Variables

Set your provider API keys:

```bash
# Example for OpenAI
export OPENAI_API_KEY="your-api-key-here"

# On Windows Command Prompt
set OPENAI_API_KEY="your-api-key-here"

```

### 5. Run the Application

```bash
python main.py

```

---

## Configuration & Data Ingestion

1. **Add Property Data:** Place your real estate listing documents, PDFs, or CSVs into your target data directory.
2. **Vector Indexing:** Run the indexing routine in `rag.py` to embed documents into your vector database (e.g., Chroma, FAISS).
3. **Querying:** Use `main.py` to test sample prompts against your ingested knowledge base.

---

## Roadmap

* [ ] Add support for multiple document formats (PDF, DOCX, CSV).
* [ ] Implement persistent vector storage.
* [ ] Build a web interface using Streamlit or FastAPI.
* [ ] Add filtering by budget, location, and property type.

---

## License

This project is licensed under the MIT License.

```

```
