import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.5-flash")


def get_answer(question, context, history=""):

    try:
        prompt = f"""
You are an AI assistant.

Use:
- conversation history
- document context

Rules:
- Answer only from context
- If not found, say "Not found in document"

History:
{history}

Context:
{context}

Question:
{question}
"""

        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error generating response: {str(e)}"