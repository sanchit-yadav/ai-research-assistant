from backend.app.rag.pdf_loader import load_pdf
from backend.app.rag.text_splitter import split_documents
from backend.app.rag.vector_store import create_vector_store
from backend.app.rag.llm import get_answer
from backend.app.rag.memory import add_message, get_history, format_history

vector_store = None


def build_index(pdf_path: str):
    global vector_store

    documents = load_pdf(pdf_path)
    chunks = split_documents(documents)

    vector_store = create_vector_store(chunks)

    return "Index built successfully"


def ask_question(query: str):

    global vector_store

    if vector_store is None:
        return "Please upload a PDF first."

    # store user message
    add_message("user", query)

    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    docs = retriever.invoke(query)

    context = "\n\n".join([d.page_content for d in docs])

    history = format_history()

    answer = get_answer(query, context, history)

    # store assistant response
    add_message("assistant", answer)

    return answer