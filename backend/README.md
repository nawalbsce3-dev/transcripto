# Transcripto Backend

Flask backend for audio transcription using OpenAI Whisper.

## Prerequisites

- Python 3.8+
- FFmpeg (required by Whisper)

Install FFmpeg:

```bash
# Windows (Chocolatey)
choco install ffmpeg

# macOS
brew install ffmpeg

# Linux
sudo apt update && sudo apt install ffmpeg
```

Verify with `ffmpeg -version`.

## Run the Backend

### 1. Go to the backend folder

```bash
cd backend
```

### 2. Create and activate a virtual environment

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

The first install downloads PyTorch (~2GB) and the Whisper model, so it can take 5-10 minutes.

### 4. Start the server

```bash
python app.py
```

The backend runs on **http://localhost:5000**.

## Optional Configuration

Copy `.env.example` to `.env` to change settings:

```bash
WHISPER_MODEL=base   # tiny, base, small, medium, large
PORT=5000
```

To use a different port without editing `.env`:

```bash
PORT=5001 python app.py
```