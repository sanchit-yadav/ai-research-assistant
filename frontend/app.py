import streamlit as st
import requests

st.set_page_config(page_title="AI Research Assistant", layout="wide")

API_URL = "http://127.0.0.1:8000"

st.title("📚 AI Research Assistant (RAG + Memory)")

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- SIDEBAR ----------------
st.sidebar.header("Upload PDF")

uploaded_file = st.sidebar.file_uploader("Upload your document")

if uploaded_file is not None:
    files = {"file": uploaded_file}

    response = requests.post(f"{API_URL}/upload", files=files)

    if response.status_code == 200:
        st.sidebar.success("PDF uploaded & indexed!")
    else:
        st.sidebar.error("Upload failed")

# ---------------- CHAT INPUT ----------------
user_input = st.chat_input("Ask a question about your document...")

# ---------------- SEND MESSAGE ----------------
if user_input:

    # show user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = requests.post(
        f"{API_URL}/chat",
        params={"query": user_input}
    )

    if response.status_code == 200:
        answer = response.json()["answer"]
    else:
        answer = "Error: Unable to get response"

    # show assistant message
    st.session_state.messages.append({"role": "assistant", "content": answer})

# ---------------- DISPLAY CHAT ----------------
for msg in st.session_state.messages:

    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["content"])

    else:
        with st.chat_message("assistant"):
            st.write(msg["content"])