# Use a Python image with PyTorch support
FROM pytorch/pytorch:1.12.1-cuda11.3-cudnn8-runtime

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# Copy application code
COPY . .

# Expose the port and define the command
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]