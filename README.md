# Transcripto - Audio to Text Web Application

A modern, production-ready full-stack application for converting audio files to text using AI.

## Overview

Transcripto is a complete SaaS-style audio transcription platform featuring:
- **Frontend:** Modern Vue 3 interface with drag-and-drop upload
- **Backend:** Flask API with OpenAI Whisper AI transcription
- **Real-time Processing:** Actual AI-powered audio-to-text conversion

## Features

✨ **Core Features**
- 🎵 Real AI-powered audio transcription with OpenAI Whisper
- 📂 Drag-and-drop file upload with format validation
- 📝 Real-time transcription processing
- 📊 Live status tracking (Idle → Processing → Completed)
- 💾 Copy-to-clipboard and download functionality
- ✅ Comprehensive error handling
- 📱 Fully responsive design
- 🔒 Secure file handling with automatic cleanup

🎨 **Design Highlights**
- Modern SaaS aesthetic with gradient backgrounds
- Glassmorphic UI cards with smooth animations
- Interactive hover states and loading indicators
- Professional color palette (tech-inspired)
- Mobile-optimized layout
- Sticky navigation header

## Tech Stack

### Frontend
- **Vue 3** - Progressive JavaScript framework with Composition API
- **Vite** - Lightning-fast build tool and dev server
- **Plain CSS** - Custom scoped styling (no frameworks)

### Backend
- **Flask** - Python web framework
- **OpenAI Whisper** - State-of-the-art AI transcription
- **PyTorch** - Machine learning backend
- **Flask-CORS** - Cross-origin resource sharing
backend/             # Flask API with Whisper
│   ├── app.py          # Main Flask application
│   ├── requirements.txt # Python dependencies
│   ├── .env.example    # Environment config template
│   └── README.md       # Backend documentation
├── src/                # Vue.js frontend
│   ├── App.vue         # Main application component
│   └── main.js         # Vue app bootstrap
├── index.html          # HTML entry point
├── package.json        # Frontend dependencies
├── vite.config.js      # Vite configuration
├── .env.example        # Frontend environment template
└─**Node.js 16+** and npm
- **Python 3.8+**
- **FFmpeg** (required for audio processing)

### Backend Setup (Flask + Whisper)

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\Activate.ps1

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *Note: First install downloads ~2GB of ML dependencies. Takes 5-10 minutes.*

4. **Run Flask server:**
   ```bash
   python app.py
   ```
   Backend starts at `http://localhost:5000`

See [backend/README.md](backend/README.md) for detailed setup and troubleshooting.

### Frontend Setup (Vue.js)

1. **Navigate to project root:**
   ```bash
   cd ..  # if you're in backend/
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Create environment file:**
   ```bash
   cp .env.example .env
   ```

4. **Start development server:**
   ```bash
   npm run dev
   ```
   Frontend opens at `http://localhost:5173` or `http://localhost:5174`

### Running the Full Stack

**Terminal 1 (Backend):**
```bash
cd backend
python app.py
```

**Terminal 2 (Frontend):**
```bash
npm run dev
```

Visit `http://localhost:5173` and upload an audio file to test real AI transcription!
   The app will open at `http://localhost:5173`

4. **Build for production:**
   ```bash
   npm run build
   ```

5. **Preview production build:**
   ```bash
   npm run preview
   ```

## How to Use

1. **Start both servers** (backend on :5000, frontend on :5173)
2. **Upload Audio**: Drag or click to upload an audio file (MP3, WAV, M4A, etc.)
3. **Select File**: The app validates the file format
4. **Convert**: Click "Convert to Text" - real AI processing begins
5. **Processing**: Watch the status indicator (~10-30 seconds depending on file)
6. **View Results**: See the AI-transcribed text in the output panel
7. **Copy/Download**: Use action buttons to copy or download the transcription

## API Integration

The frontend communicates with the backend via REST API:

**Endpoint:** `POST http://localhost:5000/api/transcribe`

**Request:**
```javascript
const formData = new FormData()
formData.append('audio', audioFile)

const response = await fetch('http://localhost:5000/api/transcribe', {
  method: 'POST',
  body: formData
})

const data = await response.json()
// data.transcription contains the text
```

**Response:**
```json
{
  "success": true,
  "transcription": "Your transcribed text...",
  "language": "en",
  "filename": "audio.mp3"
}
```

## Code Quality
Frontend (Vue 3)
- ✅ Composition API with `ref`, `computed`, and reactive state
- ✅ Clean separation of concerns
- ✅ Comprehensive error handling
- ✅ API integration with fetch
- ✅ Scoped CSS for style isolation
- ✅ Meaningful variable and method names

### Backend (Flask + Whisper)
- ✅ RESTful API design
- ✅ Proper error handling and logging
- ✅ Secure file upload handling
- ✅ CORS configuration for frontend
- ✅ Environment-based configuration
- ✅ Input validation and sanitization
- ✅ Automatic resource cleanups
- 📦 Clean, organized code structure
Architecture

### Frontend → Backend Flow

```
User uploads audio
     ↓
Vue.js validates file
     ↓
FormData sent via POST
     ↓
Flask receives file
     ↓
Saves to temp storage
     ↓
Whisper AI transcribes
     ↓
JSON response returned
     ↓
Vue displays transcription
     ↓
Temp file deleted
```

### Security Features
- ✅ File type validation (frontend + backend)
- ✅ File size limits (25MB)
- ✅ Secure filename sanitization
- ✅ Temporary file storage with auto-cleanup
- ✅ CORS restrictions
- ✅ Input validation on all endpoint
## UI/UX Details

### Responsive Breakpoints
- **Desktop**: Full-width optimized (max 800px container)
- **Tablet**: Adjusted padding and font sizes
- **Mobile**: Stacked layout, optimized touch targets

### Interactive Elements
- **File Label**: Hover effect with color change
- **Convert Button**: Gradient background, shadow on hover, loading spinner
- **Status Badge**: Animated pulsing during processing
- **Output Section**: Smooth slide-in animation
- **Copy Button**: Feedback text change on click

### Color Palette
- Primary Blue: `#4299e1` (modern, tech-inspired)
- Dark Gray: `#2d3748` (text)
- Light Gray: `#f7fafc` (backgrounds)
- Green: `#48bb78` (success state)
- Orange: `#ed8936` (processing)
- Red: `#f56565` (errors)

## Deployment

### Frontend (Production Build)

```bash
npm run build
npm run preview
```

Deploy `dist/` folder to:
- Vercel, Netlify, or GitHub Pages
- Update `VITE_API_URL` to production backend URL

### Backend (Production)

Use **gunicorn** for production:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

Deploy to:
- AWS EC2, DigitalOcean, Heroku
- Use nginx reverse proxy
- Set production environment variables
- Consider using cloud-based Whisper service for scale

## Performance

**Transcription Speed (base model):**
- Tiny model: ~5-10 seconds (1 min audio)
- Base model: ~10-20 seconds (1 min audio)
- Small model: ~20-40 seconds (1 min audio)

**Model Accuracy:**
- Tiny: Fast but less accurate
- Base: Good balance (recommended)
- Small/Medium: High accuracy, slower

## Troubleshooting

### Backend Issues

**"FFmpeg not found"**
- Install FFmpeg (see backend/README.md)

**"Port 5000 already in use"**
- Change port: `PORT=5001 python app.py`

**Slow transcription**
- Use smaller model: `WHISPER_MODEL=tiny python app.py`

### Frontend Issues

**CORS errors**
- Ensure backend is running
- Check CORS origins in `backend/app.py`

**"Failed to transcribe audio"**
- Verify backend is running on port 5000
- Check browser console for detailed errors

See [backend/README.md](backend/README.md) for more troubleshooting.

## Notes

- **Full-Stack Application**: Complete frontend + backend integration
- **Real AI Transcription**: Uses actual OpenAI Whisper models
- **Production-Ready**: Clean architecture, error handling, security
- **Portfolio Quality**: Suitable for demonstrations and interviews
- **Browser Support**: Modern browsers (Chrome, Firefox, Safari, Edge)

## What's Next?

Potential enhancements:
- [ ] User authentication and session management
- [ ] Transcription history with database storage
- [ ] Support for video file uploads
- [ ] Multi-language transcription selection
- [ ] Real-time streaming transcription
- [ ] Speaker diarization (who said what)
- [ ] Export to multiple formats (SRT, VTT, DOCX)
- [ ] Cloud storage integration (S3, Google Cloud)

## License

Portfolio project - Use freely for demonstration purposes.
