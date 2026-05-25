import streamlit as st
import requests
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

API_URL = "https://ai-research-assistant-production-7ce5.up.railway.app"

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Main Background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #111827, #1e293b);
    color: white;
}

/* Header */
.main-title {
    font-size: 3rem;
    font-weight: 700;
    color: white;
    margin-bottom: 0;
}

.subtitle {
    color: #94a3b8;
    font-size: 1.1rem;
    margin-top: -10px;
    margin-bottom: 30px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #111827;
    border-right: 1px solid #1f2937;
}

/* Cards */
.custom-card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(10px);
    margin-bottom: 20px;
}

/* Chat Bubbles */
.user-msg {
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    padding: 14px;
    border-radius: 16px;
    color: white;
    margin-bottom: 12px;
}

.bot-msg {
    background: rgba(255,255,255,0.06);
    padding: 14px;
    border-radius: 16px;
    color: #f1f5f9;
    margin-bottom: 12px;
    border: 1px solid rgba(255,255,255,0.08);
}

/* Upload Box */
.upload-box {
    padding: 18px;
    border-radius: 15px;
    background: rgba(255,255,255,0.04);
    border: 1px dashed #3b82f6;
    text-align: center;
    margin-bottom: 20px;
}

/* Buttons */
.stButton>button {
    width: 100%;
    background: linear-gradient(135deg, #3b82f6, #2563eb);
    color: white;
    border-radius: 12px;
    border: none;
    padding: 12px;
    font-weight: 600;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.02);
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
}

/* Chat Input */
[data-testid="stChatInput"] {
    background: rgba(255,255,255,0.06);
    border-radius: 15px;
}

/* Metrics */
.metric-card {
    background: rgba(255,255,255,0.05);
    padding: 15px;
    border-radius: 15px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.08);
}

.metric-number {
    font-size: 1.8rem;
    font-weight: 700;
    color: #60a5fa;
}

.metric-label {
    color: #cbd5e1;
    font-size: 0.9rem;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "uploaded" not in st.session_state:
    st.session_state.uploaded = False

# ---------------- HEADER ----------------
st.markdown("""
<div>
    <h1 class="main-title">🧠 AI Research Assistant</h1>
    <p class="subtitle">
        Upload PDFs • Ask Questions • Retrieve Intelligent Answers with RAG + Memory
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- TOP METRICS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">RAG</div>
        <div class="metric-label">Powered Retrieval</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">AI</div>
        <div class="metric-label">Gemini Intelligence</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">24/7</div>
        <div class="metric-label">Instant Research</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.markdown("## 📂 Document Center")

    st.markdown("""
    <div class="upload-box">
        <h4>Upload Your PDF</h4>
        <p style="color:#94a3b8; font-size:14px;">
            Upload research papers, notes, reports or documents
        </p>
    </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:

        with st.spinner("Uploading & Indexing PDF..."):

            files = {"file": uploaded_file}

            try:
                response = requests.post(
                    f"{API_URL}/upload",
                    files=files
                )

                if response.status_code == 200:
                    st.success("✅ PDF uploaded successfully!")
                    st.session_state.uploaded = True

                else:
                    st.error("❌ Upload failed")

            except:
                st.error("⚠️ Backend connection failed")

    st.markdown("---")

    st.markdown("### 🚀 Features")

    st.markdown("""
    ✅ Retrieval-Augmented Generation  
    ✅ Conversational Memory  
    ✅ Fast PDF Search  
    ✅ AI-powered Responses  
    ✅ Context-aware Answers  
    """)

    st.markdown("---")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ---------------- MAIN CHAT AREA ----------------
chat_container = st.container()

with chat_container:

    # Welcome Card
    if len(st.session_state.messages) == 0:

        st.markdown("""
        <div class="custom-card">
            <h2>👋 Welcome to AI Research Assistant</h2>
            <p style="color:#cbd5e1;">
                Upload your PDF and ask intelligent questions from your documents.
                This assistant uses Retrieval-Augmented Generation (RAG)
                and conversational memory for smarter answers.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Display messages
    for msg in st.session_state.messages:

        if msg["role"] == "user":

            st.markdown(f"""
            <div class="user-msg">
                <b>🧑 You</b><br><br>
                {msg["content"]}
            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown(f"""
            <div class="bot-msg">
                <b>🤖 AI Assistant</b><br><br>
                {msg["content"]}
            </div>
            """, unsafe_allow_html=True)

# ---------------- CHAT INPUT ----------------
user_input = st.chat_input("Ask anything about your document...")

# ---------------- HANDLE CHAT ----------------
if user_input:

    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Loading animation
    with st.spinner("AI is thinking..."):

        try:
            response = requests.post(
                f"{API_URL}/chat",
                params={"query": user_input}
            )

            if response.status_code == 200:
                answer = response.json()["answer"]

            else:
                answer = "❌ Error: Unable to get response"

        except:
            answer = "⚠️ Backend connection failed"

    # Store assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    st.rerun()