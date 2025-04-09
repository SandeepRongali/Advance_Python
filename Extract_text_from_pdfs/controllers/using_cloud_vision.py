from fastapi import FastAPI, File, UploadFile, HTTPException,Query
from google.cloud import storage, vision, bigquery
import re
def upload_to_gcs(bucket_name: str, folder_name: str, file: UploadFile) -> str:
    """Uploads a file to Google Cloud Storage and returns its URI."""
    try:
        destination_blob_name = f"{folder_name}/{file.filename}"
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_file(file.file, rewind=True)
        return f"gs://{bucket_name}/{destination_blob_name}"
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File upload failed: {str(e)}")


def async_detect_document(gcs_source_uri: str, gcs_destination_uri: str) -> list:
    """Performs asynchronous OCR on a document stored in GCS (PDF only)."""
    client = vision.ImageAnnotatorClient()
    feature = vision.Feature(type_=vision.Feature.Type.DOCUMENT_TEXT_DETECTION)
    async_request = vision.AsyncAnnotateFileRequest(
        features=[feature],
        input_config=vision.InputConfig(gcs_source=vision.GcsSource(uri=gcs_source_uri), mime_type="application/pdf"),
        output_config=vision.OutputConfig(gcs_destination=vision.GcsDestination(uri=gcs_destination_uri), batch_size=30),
    )
    operation = client.async_batch_annotate_files(requests=[async_request])
    operation.result(timeout=420)
    storage_client = storage.Client()
    match = re.match(r"gs://([^/]+)/(.+)", gcs_destination_uri)
    bucket = storage_client.get_bucket(match.group(1))
    return [blob for blob in list(bucket.list_blobs(prefix=match.group(2))) if not blob.name.endswith("/")]