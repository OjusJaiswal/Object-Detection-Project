from fastapi import FastAPI, File, UploadFile
import requests

app = FastAPI()

AI_BACKEND_URL = "http://ai-backend:8000/process-image"

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    # Forward the image to the AI backend
    response = requests.post(
        AI_BACKEND_URL,
        files={"file": (file.filename, file.file, file.content_type)},
    )
    return response.json()