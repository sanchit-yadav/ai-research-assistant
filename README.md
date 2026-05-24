# 🤖 AI Research Assistant

An AI-powered Research Assistant built using **FastAPI**, **LangChain**, **Google Gemini API**, and **RAG (Retrieval-Augmented Generation)**.

This project allows users to upload research papers/documents and interact with them using AI-powered contextual conversations.

---

# 🚀 Features

- 📄 PDF document upload and processing
- 🔍 Semantic search using vector embeddings
- 💬 Conversational AI chat interface
- 🧠 Retrieval-Augmented Generation (RAG)
- ⚡ FastAPI backend
- 🔗 Google Gemini API integration
- 📚 Context-aware responses

---

# 🛠️ Tech Stack

## Backend
- FastAPI
- Python

## AI/ML
- LangChain
- Google Gemini API
- ChromaDB
- Sentence Transformers

## Other Tools
- Python-dotenv
- Uvicorn
- PyPDF

---

# 📂 Project Structure

```bash
AI-RESEARCH-ASSISTANT/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── rag/
│   │   ├── services/
│   │   └── main.py
│   │
│   ├── data/
│   ├── models/
│   └── chromadb/
│
├── frontend/
├── screenshots/
├── app.py
├── requirements.txt
├── runtime.txt
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/sanchit-yadav/ai-research-assistant.git
```

---

## Move Into Project Folder

```bash
cd ai-research-assistant
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

---

# ▶️ Run Backend Server

```bash
uvicorn backend.app.main:app --reload
```

---

# 🌐 API Documentation

After running the server:

```text
http://127.0.0.1:8000/docs
```

---

# 📸 Screenshots

(Add screenshots here later)

---

# 🚀 Future Improvements

- Multi-document support
- Chat history memory
- Frontend chat UI
- User authentication
- Deployment integration
- Citation-aware responses
- PDF summary export

---

# 👨‍💻 Author

Sanchit Yadav

- GitHub: https://github.com/sanchit-yadav

---

# ⭐ Project Status

Currently under active development.