from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from dotenv import load_dotenv
import os

from controllers.invoke_vertexAI_model import generate_answer, generate_image

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, limit to specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    query: str

@app.post("/api/chat_bot")
async def chat_with_model(user_data: Item):
    question = user_data.query
    result = generate_answer(question)
    return result
@app.post("/api/image_chat_bot")
async def image_chat_bot(user_data: Item):
    question = user_data.query
    result = generate_image(question)
    return result


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
