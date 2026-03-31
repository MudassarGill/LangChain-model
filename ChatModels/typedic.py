from typing import TypedDict

class ChatMessage(TypedDict):
    role: str
    content: str

chat_history: list[ChatMessage] = []

chat_history.append({"role": "user", "content": "Hello"})

print(chat_history)