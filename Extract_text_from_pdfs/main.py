from fastapi import FastAPI, HTTPException, Request, Depends, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Optional, List
import uvicorn
import uuid
from dotenv import load_dotenv
import os
import fitz
import concurrent.futures

from controllers.using_cloud_vision import upload_to_gcs, async_detect_document
from controllers.using_fitz import extract_text_pagewise

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, limit to specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.post("/api/extract_text_using_fitz")
async def extract_text(file: UploadFile = File(...)):
    """API endpoint to extract text from a PDF file, page by page."""
    try:
        pdf_bytes = await file.read()  # Read PDF file as bytes
        extracted_text = extract_text_pagewise(pdf_bytes)
        return {"filename": file.filename, "pages": extracted_text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/extract_text_using_cloud_vision")
async def upload_file(file: UploadFile = File(...)):
    try:
        bucket_name = os.environ["BUCKET_NAME"]
        folder_name = os.environ["FOLDER_NAME"]
        output_folder = os.environ["TRAIN_FOLDER"]
        if file.filename.endswith(".pdf"):
            gcs_uri = upload_to_gcs(bucket_name, folder_name, file)
            gcs_destination_uri = f"gs://{bucket_name}/{output_folder}/"
            blob_list = async_detect_document(gcs_uri, gcs_destination_uri)
            with concurrent.futures.ThreadPoolExecutor() as executor:
                pages_text = list(executor.map(extract_text, blob_list))
        return pages_text
    except:
        pass


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
