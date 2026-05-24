from pathlib import Path

from backend.app.rag.pdf_loader import load_pdf
from backend.app.rag.text_splitter import split_documents
from backend.app.rag.vector_store import create_vector_store
from backend.app.rag.llm import get_answer

BASE_DIR = Path(__file__).resolve().parent
pdf_path = BASE_DIR.parent / "data" / "sample.pdf"

# Load PDF
documents = load_pdf(str(pdf_path))

# Split
chunks = split_documents(documents)

# Vector DB
vector_store = create_vector_store(chunks)

# Retriever
retriever = vector_store.as_retriever(search_kwargs={"k": 3})

query = input("\nAsk a question: ")

docs = retriever.invoke(query)

# Combine context
context = "\n\n".join([doc.page_content for doc in docs])

# Get AI answer
answer = get_answer(query, context)

print("\n================ ANSWER ================\n")
print(answer)