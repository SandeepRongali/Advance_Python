from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Optional, List
import uvicorn
import uuid
from dotenv import load_dotenv
import os
from vertexai.generative_models import (
    GenerationConfig,
    GenerativeModel,
    Part,
    Content,
    ChatSession
)

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, limit to specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store chat sessions per session ID
chat_sessions: Dict[str, ChatSession] = {}

gemini_model = GenerativeModel(
    "gemini-1.5-pro-002",
    generation_config=GenerationConfig(temperature=0),
)

class ChatRequest(BaseModel):
    session_id: str
    query: str

def get_chat_session(session_id: str) -> ChatSession:
    """Retrieve or create a chat session."""
    if session_id not in chat_sessions:
        chat_sessions[session_id] = ChatSession(model=gemini_model, history=[])
    return chat_sessions[session_id]

@app.post("/api/create_session")
def create_session():
    """Generates a new session ID."""
    session_id = str(uuid.uuid4())
    chat_sessions[session_id] = ChatSession(model=gemini_model, history=[])
    return {"session_id": session_id}

@app.post("/api/chat_bot")
def chat_with_model(user_data: ChatRequest):
    session_id = user_data.session_id
    question = user_data.query

    chat_session = get_chat_session(session_id)
    response = chat_session.send_message(question)
    return {"session_id": session_id, "response": response.text}

@app.post("/api/clear_chat")
def clear_chat(session_id: str):
    """Clears chat history for a specific session ID but retains the session."""
    if session_id in chat_sessions:
        chat_sessions[session_id].history = []
        return {"message": "Chat history cleared", "session_id": session_id}
    raise HTTPException(status_code=404, detail="Session ID not found")

@app.delete("/api/delete_session")
def delete_session(session_id: str):
    """Deletes a chat session completely."""
    if session_id in chat_sessions:
        del chat_sessions[session_id]
        return {"message": "Session deleted", "session_id": session_id}
    raise HTTPException(status_code=404, detail="Session ID not found")

@app.get("/api/get_sessions")
def get_sessions() -> List[str]:
    """Retrieves all active session IDs."""
    return list(chat_sessions.keys())


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
