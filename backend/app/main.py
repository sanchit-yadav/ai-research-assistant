from fastapi import FastAPI
from backend.app.api.routes import router

app = FastAPI(
    title="AI Research Assistant",
    description="RAG-based document Q&A system"
)

app.include_router(router)

@app.get("/")
def home():
    return {"status": "running"}