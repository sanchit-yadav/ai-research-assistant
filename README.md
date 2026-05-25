# AI Research Assistant

An AI-powered Research Assistant built using FastAPI, Streamlit, LangChain, ChromaDB, and Google Gemini API.  
This project allows users to upload PDF documents and ask contextual questions using Retrieval-Augmented Generation (RAG).

---

# Live Deployment

## Frontend
[Open Streamlit App](https://ai-research-assistant-cxxtknavp8bs4gefnrgs59.streamlit.app/)

## Backend API
[Open Backend API](https://railway.com/project/627481c8-2fe9-4a14-a8c5-b063cb2aa6bc?)

---

# Features

- PDF Upload & Processing
- AI-powered Question Answering
- Retrieval-Augmented Generation (RAG)
- Semantic Search using Vector Database
- FastAPI Backend
- Streamlit Frontend
- Google Gemini Integration
- ChromaDB Vector Storage
- Clean UI for Research Assistance

---

# Tech Stack

## Backend
- FastAPI
- LangChain
- ChromaDB
- Google Gemini API
- HuggingFace Embeddings

## Frontend
- Streamlit
- Requests

## Deployment
- Backend - Railway
- Frontend - Streamlit cloud

---

# Project Structure

```bash
AI-RESEARCH-ASSISTANT/
│
├── backend/
│   │
│   ├── app/
│   │   │
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   └── routes.py
│   │   │
│   │   ├── rag/
│   │   │
│   │   ├── services/
│   │   │   ├── __pycache__/
│   │   │   └── rag_pipeline.py
│   │   │
│   │   ├── __init__.py
│   │   └── main.py
│   │
│   ├── models/
│   ├── data/
│   │
│   └── tests/
│       ├── test_pdf.py
│       └── test_rag.py
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
├── screenshots/
│   └── ai assistant screenshot.png
│
├── .env
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
└── runtime.txt
```

---

# Application Workflow

1. User uploads PDF document
2. PDF content is processed and split into chunks
3. Text embeddings are generated
4. Embeddings stored in ChromaDB
5. User asks questions
6. Relevant chunks retrieved
7. Gemini LLM generates contextual response

---

# Installation

## Clone Repository

```bash
git clone https://github.com/sanchit-yadav/ai-research-assistant
cd AI-RESEARCH-ASSISTANT
```

---

# Backend Setup

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Backend

```bash
uvicorn backend.app.main:app --reload
```

Backend runs on:

```bash
http://127.0.0.1:8000
```

---

# Frontend Setup

## Move to Frontend

```bash
cd frontend
```

## Install Frontend Dependencies

```bash
pip install -r requirements.txt
```

## Run Streamlit App

```bash
streamlit run app.py
```

Frontend runs on:

```bash
http://localhost:8501
```

---

# Environment Variables

Create a `.env` file in root directory.

```env
GEMINI_API_KEY=your_google_gemini_api_key
```

---

# API Endpoint

## Home Route

```http
GET /
```

Response:

```json
{
  "status": "running"
}
```

---

# Screenshot


```bash
screenshots\ai_assistant_screenshot.png
```

---

# Future Improvements

- User Authentication
- Multiple PDF Upload
- Conversation Memory
- Voice Input
- Docker Support
- Database Integration
- Streaming Responses
- Dark Mode UI

---

# Author

## Sanchit Yadav

B.Tech CSE Student  
Aspiring AI/ML Engineer

---

# License

This project is developed for educational and portfolio purposes.