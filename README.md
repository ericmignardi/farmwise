# FarmWise 🌾

> Full-stack AgTech application featuring a RAG-powered AI assistant using LangChain, ChromaDB, and Google Gemini. Built with Django REST Framework (Python) and Vue.js (TypeScript).

## Tech Stack

| Layer            | Technology                             |
| ---------------- | -------------------------------------- |
| **Backend**      | Django 5.1 + Django REST Framework     |
| **Frontend**     | Vue.js 3 + TypeScript + Tailwind CSS   |
| **LLM**          | Google Gemini 2.0 Flash                |
| **Embeddings**   | HuggingFace `all-MiniLM-L6-v2` (local) |
| **Vector DB**    | ChromaDB                               |
| **AI Framework** | LangChain (LCEL)                       |

## Features

- 📊 **Farm Dashboard** — KPIs for farms, crops, assets, and wealth tracking
- 🤖 **AI Chat Assistant** — RAG-powered Q&A using your farm data
- 🔍 **Semantic Search** — Vector similarity search over indexed farm records

## API Endpoints

| Method | Endpoint           | Description         |
| ------ | ------------------ | ------------------- |
| `GET`  | `/api/farms/`      | List all farms      |
| `GET`  | `/api/farms/<id>/` | Get farm details    |
| `GET`  | `/api/crops/`      | List all crops      |
| `GET`  | `/api/assets/`     | List all assets     |
| `GET`  | `/api/wealth/`     | List wealth records |
| `POST` | `/api/chat/`       | AI chat (RAG)       |

## Data Models

- **Farm** — name, location, owner, total acreage
- **Crop** — name, planted/harvest dates, expected yield, current value
- **Asset** — equipment, land, livestock, buildings, vehicles
- **WealthRecord** — daily snapshot of farm value

## Quick Start

```bash
# Backend
cd backend
source venv/Scripts/activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data # Seed data into SQLite DB
python manage.py index_data   # Index data into ChromaDB
python manage.py runserver

# Frontend
cd frontend
npm install
npm run dev
```

## Environment Variables

```env
GOOGLE_API_KEY=your_gemini_api_key
```

## Architecture

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for detailed diagrams.

---

## Skills Demonstrated

| Skill                  | Evidence                           |
| ---------------------- | ---------------------------------- |
| Full-Stack Development | Django backend + Vue.js frontend   |
| REST API Design        | DRF with proper serializers        |
| LangChain/RAG          | Vector search + LLM integration    |
| Modern LLM Integration | Gemini 2.0 Flash, local embeddings |
| Vector Databases       | ChromaDB for semantic search       |
| TypeScript             | Frontend with type safety          |
