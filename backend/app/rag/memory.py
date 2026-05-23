from collections import deque

# simple in-memory chat history (for project/demo)
chat_history = deque(maxlen=10)


def add_message(role, message):
    chat_history.append({"role": role, "message": message})


def get_history():
    return list(chat_history)


def format_history():
    history_text = ""

    for msg in chat_history:
        history_text += f"{msg['role']}: {msg['message']}\n"

    return history_text