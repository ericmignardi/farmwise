# FarmWise 🌾

A full-stack AgTech application featuring a RAG-powered AI assistant and real-time dashboard. Manage your farm’s assets, crops, and wealth with a semantic-search-enabled interface.

---

## Features

- **Farm Dashboard**: Visualize KPIs for farms, crops, assets, and wealth tracking in a unified interface.
- **AI Chat Assistant**: RAG-powered Q&A interface that lets you chat with your farm data using Google Gemini.
- **Semantic Search**: Vector similarity search over indexed farm records for fast, context-aware information retrieval.
- **Wealth Tracking**: Snapshot-based tracking of farm valuations and asset performance over time.

## Tech Stack

- **Python 3.12+ (Django / DRF)**: Robust backend API architecture.
- **Vue.js 3 / TypeScript**: Modern, type-safe frontend with a responsive UI.
- **LangChain (Python)**: Orchestrating the RAG (Retrieval-Augmented Generation) pipeline.
- **Google Gemini 2.0 Flash**: State-of-the-art LLM for natural language processing.
- **ChromaDB**: High-performance vector database for semantic search and storage.
- **Tailwind CSS**: Utility-first styling for a premium, clean design.

---

## Installation & Setup

**Prerequisites:**

- Python 3.12+
- Node.js & npm
- [Google API Key](https://aistudio.google.com/app/apikey) for Gemini 2.0 Flash

```bash
# Clone the repository
git clone https://github.com/yourusername/farmwise.git
cd farmwise

# Setup Backend
cd backend
python -m venv venv
source venv/Scripts/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Setup Frontend
cd ../frontend
npm install
```

## Usage

*Note: Ensure your `GOOGLE_API_KEY` is set in a `.env` file within the `backend/` directory.*

**1. Seed and Index Data:**

```bash
# Seed the SQLite database with sample farm data
python manage.py seed_data

# Index the data into ChromaDB for semantic search
python manage.py index_data
```

**2. Start the Backend Server:**

```bash
python manage.py runserver
```

**3. Launch the Frontend Development Server:**

```bash
cd frontend
npm run dev
```

---

## Things Learned

Throughout the development of FarmWise, several core AgTech and AI concepts were explored:

- **RAG Architecture**: Implementing Retrieval-Augmented Generation to ground LLM responses in proprietary data.
- **Vector Embeddings**: Leveraging HuggingFace's `all-MiniLM-L6-v2` for local, high-speed semantic indexing.
- **Full-Stack Orchestration**: Integrating asynchronous AI workflows between a Django REST API and a Vue.js frontend.
- **Semantic Data Modeling**: Designing data structures that bridge traditional relational databases (SQLite) and vector stores (ChromaDB).
- **Modern AI Integration**: Utilizing LangChain (LCEL) to build modular, extensible AI agent pipelines.

