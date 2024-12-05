from fastapi import FastAPI, File, UploadFile
import torch
from PIL import Image
import io

app = FastAPI()

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

@app.post("/process-image")
async def process_image(file: UploadFile = File(...)):
    # Load image
    image = Image.open(io.BytesIO(await file.read()))
    
    # Perform object detection
    results = model(image)
    
    # Structure results
    detections = results.pandas().xyxy[0].to_dict(orient="records")
    return {"detections": detections}