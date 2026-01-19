# FarmWise Architecture

## Database Schema

```mermaid
erDiagram
    Farm ||--o{ Crop : "has many"
    Farm ||--o{ Asset : "has many"
    Farm ||--o{ WealthRecord : "has many"

    Farm {
        int id PK
        string name
        string location
        string owner
        decimal total_acreage
        datetime created_at
        datetime updated_at
    }

    Crop {
        int id PK
        int farm_id FK
        string name
        date planted_date
        date harvest_date
        decimal expected_yield
        decimal current_value
        text notes
        datetime created_at
    }

    Asset {
        int id PK
        int farm_id FK
        string name
        enum asset_type
        date purchase_date
        decimal purchase_price
        decimal current_value
        text description
        datetime created_at
    }

    WealthRecord {
        int id PK
        int farm_id FK
        date date
        decimal total_crop_value
        decimal total_asset_value
        decimal total_value
        text notes
        datetime created_at
    }
```

## API Routes

```mermaid
flowchart LR
    subgraph API["API Endpoints"]
        F1["GET /api/farms/"]
        F2["GET /api/farms/:id/"]
        C1["GET /api/crops/"]
        A1["GET /api/assets/"]
        W1["GET /api/wealth/"]
    end

    subgraph Views["Views"]
        V1["farm_list"]
        V2["farm_detail"]
        V3["crop_list"]
        V4["asset_list"]
        V5["wealth_list"]
    end

    subgraph Models["Models"]
        M1[("Farm")]
        M2[("Crop")]
        M3[("Asset")]
        M4[("WealthRecord")]
    end

    F1 --> V1 --> M1
    F2 --> V2 --> M1
    C1 --> V3 --> M2
    A1 --> V4 --> M3
    W1 --> V5 --> M4
```

## Endpoints

| Method | Endpoint           | View          | Description         |
| ------ | ------------------ | ------------- | ------------------- |
| `GET`  | `/api/farms/`      | `farm_list`   | List all farms      |
| `GET`  | `/api/farms/<id>/` | `farm_detail` | Get farm details    |
| `GET`  | `/api/crops/`      | `crop_list`   | List all crops      |
| `GET`  | `/api/assets/`     | `asset_list`  | List all assets     |
| `GET`  | `/api/wealth/`     | `wealth_list` | List wealth records |
| `POST` | `/api/chat/`       | `chat`        | AI chat assistant   |

## Asset Types

| Value       | Display   |
| ----------- | --------- |
| `equipment` | Equipment |
| `land`      | Land      |
| `livestock` | Livestock |
| `building`  | Building  |
| `vehicle`   | Vehicle   |
| `other`     | Other     |

---

## AI Chat / RAG Flow

```mermaid
sequenceDiagram
    participant User
    participant Vue as ChatView.vue
    participant Django as /api/chat/
    participant RAG as LangChain RAG
    participant Chroma as ChromaDB
    participant LLM as Gemini

    User->>Vue: Send message
    Vue->>Django: POST {message}
    Django->>RAG: invoke(message)
    RAG->>Chroma: Retrieve docs (k=5)
    Chroma-->>RAG: Context documents
    RAG->>LLM: Prompt + Context
    LLM-->>Django: Generated response
    Django-->>Vue: {response}
    Vue-->>User: Display AI message
```

### Components

| Component    | File              | Purpose                                |
| ------------ | ----------------- | -------------------------------------- |
| LLM          | `services/llm.py` | Google Gemini 2.0 Flash                |
| RAG Chain    | `services/rag.py` | LCEL chain with retriever + prompt     |
| Embeddings   | `services/rag.py` | HuggingFace `all-MiniLM-L6-v2` (local) |
| Vector Store | `chroma_db/`      | ChromaDB                               |
| Frontend     | `ChatView.vue`    | Chat UI with markdown rendering        |
