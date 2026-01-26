# Transcripto Backend - Flask + Whisper API

## 🚀 Overview

Production-ready Flask backend for audio transcription using OpenAI Whisper. Integrates seamlessly with the Transcripto Vue.js frontend.

## 📋 Features

- ✅ Audio file upload via multipart/form-data
- ✅ OpenAI Whisper transcription (multiple models supported)
- ✅ Support for all major audio formats (MP3, WAV, M4A, FLAC, OGG, AAC)
- ✅ CORS enabled for frontend integration
- ✅ Secure file handling with temporary storage
- ✅ Comprehensive error handling and logging
- ✅ Health check endpoint
- ✅ File size validation (25MB limit)
- ✅ Production-ready architecture

## 🛠️ Tech Stack

- **Flask** - Web framework
- **OpenAI Whisper** - AI transcription model
- **Flask-CORS** - Cross-origin support
- **PyTorch** - ML backend (installed with Whisper)

## 📦 Prerequisites

Before running the backend, ensure you have:

1. **Python 3.8+** installed
2. **FFmpeg** installed (required by Whisper for audio processing)

### Installing FFmpeg

**Windows:**
```powershell
# Using Chocolatey
choco install ffmpeg

# Or download from: https://ffmpeg.org/download.html
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt update
sudo apt install ffmpeg
```

Verify installation:
```bash
ffmpeg -version
```

## 🚀 Quick Start

### 1. Navigate to backend directory

```bash
cd backend
```

### 2. Create virtual environment

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

**Note:** First installation will download PyTorch (~2GB) and Whisper model weights (~150MB for base model). This may take 5-10 minutes.

### 4. Configure environment (optional)

```bash
# Copy example config
cp .env.example .env

# Edit .env to customize settings
```

**Available Models:**
- `tiny` - Fastest, least accurate (~40MB)
- `base` - Good balance (default, ~150MB)
- `small` - Better accuracy (~500MB)
- `medium` - High accuracy (~1.5GB)
- `large` - Best accuracy (~3GB)

### 5. Run the server

```bash
python app.py
```

The backend will start on **http://localhost:5000**

You should see:
```
Loading Whisper model: base
Whisper model loaded successfully!
Starting Transcripto Backend on port 5000
```

## 🧪 Testing the API

### Health Check

```bash
curl http://localhost:5000/api/health
```

Response:
```json
{
  "status": "healthy",
  "service": "Transcripto Backend",
  "model": "base",
  "version": "1.0.0"
}
```

### Test Transcription

```bash
curl -X POST http://localhost:5000/api/transcribe \
  -F "audio=@path/to/your/audio.mp3"
```

Response:
```json
{
  "success": true,
  "transcription": "Your transcribed text here...",
  "language": "en",
  "filename": "audio.mp3"
}
```

## 🔌 API Endpoints

### `GET /api/health`

Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "service": "Transcripto Backend",
  "model": "base",
  "version": "1.0.0"
}
```

### `POST /api/transcribe`

Transcribe audio file to text.

**Request:**
- Method: `POST`
- Content-Type: `multipart/form-data`
- Body: `audio` file field

**Success Response (200):**
```json
{
  "success": true,
  "transcription": "Transcribed text content...",
  "language": "en",
  "filename": "audio.mp3"
}
```

**Error Response (400/500):**
```json
{
  "error": "Error message",
  "details": "Detailed error information"
}
```

**Supported formats:** MP3, WAV, M4A, FLAC, OGG, AAC, WMA, OPUS

## 🔧 Configuration

Environment variables (`.env` file):

```bash
# Flask Configuration
FLASK_APP=app.py
FLASK_DEBUG=True
PORT=5000

# Whisper Model (tiny, base, small, medium, large)
WHISPER_MODEL=base
```

## 🔒 Security Features

- ✅ File extension validation
- ✅ Secure filename handling
- ✅ Temporary file cleanup
- ✅ File size limits (25MB)
- ✅ CORS restrictions
- ✅ Input sanitization

## 📊 Performance

**Transcription times (base model, ~1 min audio):**
- Tiny model: ~5-10 seconds
- Base model: ~10-20 seconds
- Small model: ~20-40 seconds
- Medium model: ~40-80 seconds

**Note:** First transcription may be slower as the model initializes.

## 🐛 Troubleshooting

### Issue: "No module named 'whisper'"

**Solution:**
```bash
pip install openai-whisper
```

### Issue: "FFmpeg not found"

**Solution:** Install FFmpeg (see Prerequisites section)

### Issue: CORS errors in browser

**Solution:** Check that frontend URL is in CORS origins list in `app.py`:
```python
CORS(app, resources={r"/api/*": {"origins": ["http://localhost:5173", "http://localhost:5174"]}})
```

### Issue: "Port 5000 already in use"

**Solution:** Change port in `.env` or run with custom port:
```bash
PORT=5001 python app.py
```

### Issue: Slow transcription

**Solution:** Use a smaller model (tiny or base) for faster results:
```bash
WHISPER_MODEL=tiny python app.py
```

## 📁 Project Structure

```
backend/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment config template
├── README.md             # This file
└── venv/                 # Virtual environment (created)
```

## 🚀 Production Deployment

For production, consider:

1. **Use gunicorn** instead of Flask dev server:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

2. **Set up reverse proxy** (nginx/Apache)

3. **Use environment variables** for sensitive config

4. **Add rate limiting** for API endpoints

5. **Implement authentication** if needed

6. **Use production Whisper server** or cloud service

## 📝 License

Portfolio project - Use freely for demonstration purposes.

## 🤝 Contributing

This is a portfolio project. Feedback and suggestions welcome!

## 📧 Support

For issues or questions, check the troubleshooting section or create an issue.

---

**Made with ❤️ for portfolio demonstration**
