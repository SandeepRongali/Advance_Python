import fitz

def extract_text_pagewise(pdf_bytes: bytes) -> dict:
    """Extract text from a PDF file page by page."""
    try:
        pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
        extracted_text = {}

        for page_num, page in enumerate(pdf_document, start=1):
            extracted_text[f"Page {page_num}"] = page.get_text("text").strip()

        return extracted_text

    except Exception as e:
        raise Exception(f"Error extracting text: {str(e)}")