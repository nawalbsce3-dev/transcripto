# 🚀 Quick Start Guide - Transcripto

## Get Up and Running in 5 Minutes

### Step 1: Install FFmpeg (One-time setup)

**Windows:**
```powershell
choco install ffmpeg
# Or download from: https://ffmpeg.org/download.html
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt install ffmpeg
```

### Step 2: Start Backend

```bash
# Navigate to backend
cd backend

# Create virtual environment (Windows)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Or on macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Install dependencies (takes 5-10 min first time)
pip install -r requirements.txt

# Run Flask server
python app.py
```

✅ Backend should now be running at **http://localhost:5000**

### Step 3: Start Frontend (New Terminal)

```bash
# From project root
npm install

# Start Vite dev server
npm run dev
```

✅ Frontend should open at **http://localhost:5173**

### Step 4: Test It!

1. Open browser to `http://localhost:5173`
2. Drag/drop an audio file (or click to browse)
3. Click "Convert to Text"
4. Watch the real AI transcription happen!
5. Copy or download your transcription

---

## Common Issues

**"FFmpeg not found"**
→ Install FFmpeg (see Step 1)

**"Port already in use"**
→ Backend: `PORT=5001 python app.py`
→ Frontend: Edit `vite.config.js` to change port

**Slow transcription**
→ Use faster model: `WHISPER_MODEL=tiny python app.py`

**CORS errors**
→ Make sure both servers are running
→ Check backend console for errors

---

## Architecture Overview

```
Frontend (Vue.js)          Backend (Flask + Whisper)
http://localhost:5173  →   http://localhost:5000
     │                           │
     └─── POST /api/transcribe ──┤
                                  ├─ Save audio temp file
                                  ├─ Run Whisper AI
                                  ├─ Return transcription JSON
                                  └─ Delete temp file
```

---

## Next Steps

- Read [README.md](README.md) for full documentation
- Check [backend/README.md](backend/README.md) for API details
- Customize Whisper model in `backend/.env`
- Deploy to production servers

**Happy transcribing! 🎉**
