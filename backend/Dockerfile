# Transcripto Backend - Whisper/Flask
# Containerized for Render/Fly/Railway

FROM python:3.11-slim

# System deps
RUN apt-get update \ 
    && apt-get install -y --no-install-recommends ffmpeg \ 
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Default configuration
ENV PORT=5000 \
    WHISPER_MODEL=tiny

EXPOSE 5000

CMD ["python", "app.py"]
