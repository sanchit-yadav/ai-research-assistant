from pathlib import Path
from app.rag.pdf_loader import load_pdf

BASE_DIR = Path(__file__).resolve().parent
pdf_path = BASE_DIR.parent / "data" / "sample.pdf"

docs = load_pdf(str(pdf_path))

print(docs[0].page_content)