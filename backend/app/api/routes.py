from fastapi import APIRouter, UploadFile, File, HTTPException
from backend.app.services.rag_pipeline import build_index, ask_question
import os

router = APIRouter()

UPLOAD_DIR = "data"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    try:
        file_path = f"{UPLOAD_DIR}/{file.filename}"

        with open(file_path, "wb") as f:
            f.write(await file.read())

        result = build_index(file_path)

        return {"message": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/chat")
def chat(query: str):

    try:
        answer = ask_question(query)
        return {"answer": answer}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))