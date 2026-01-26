# Transcripto - Complete Setup Script (Windows PowerShell)
# Run this script to set up both frontend and backend

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Transcripto Full-Stack Setup" -ForegroundColor Cyan
Write-Host "  Audio to Text AI Application" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check prerequisites
Write-Host "Checking prerequisites..." -ForegroundColor Yellow

# Check Node.js
try {
    $nodeVersion = node --version
    Write-Host "✓ Node.js found: $nodeVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Node.js not found. Please install from https://nodejs.org" -ForegroundColor Red
    exit 1
}

# Check Python
try {
    $pythonVersion = python --version
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Python not found. Please install from https://python.org" -ForegroundColor Red
    exit 1
}

# Check FFmpeg
try {
    $ffmpegVersion = ffmpeg -version 2>$null | Select-Object -First 1
    Write-Host "✓ FFmpeg found" -ForegroundColor Green
} catch {
    Write-Host "✗ FFmpeg not found." -ForegroundColor Red
    Write-Host "  Install with: choco install ffmpeg" -ForegroundColor Yellow
    Write-Host "  Or download from: https://ffmpeg.org/download.html" -ForegroundColor Yellow
    $continue = Read-Host "Continue anyway? (y/n)"
    if ($continue -ne 'y') { exit 1 }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Setting up Backend (Python + Flask)" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Backend setup
Set-Location backend

Write-Host "Creating Python virtual environment..." -ForegroundColor Yellow
python -m venv venv

Write-Host "Activating virtual environment..." -ForegroundColor Yellow
.\venv\Scripts\Activate.ps1

Write-Host "Installing Python dependencies (this may take 5-10 minutes)..." -ForegroundColor Yellow
pip install -r requirements.txt

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Backend dependencies installed successfully!" -ForegroundColor Green
} else {
    Write-Host "✗ Failed to install backend dependencies" -ForegroundColor Red
    exit 1
}

# Copy .env if needed
if (!(Test-Path .env)) {
    Copy-Item .env.example .env
    Write-Host "✓ Created backend .env file" -ForegroundColor Green
}

Set-Location ..

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Setting up Frontend (Vue.js + Vite)" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Installing Node.js dependencies..." -ForegroundColor Yellow
npm install

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Frontend dependencies installed successfully!" -ForegroundColor Green
} else {
    Write-Host "✗ Failed to install frontend dependencies" -ForegroundColor Red
    exit 1
}

# Copy .env if needed
if (!(Test-Path .env)) {
    Copy-Item .env.example .env
    Write-Host "✓ Created frontend .env file" -ForegroundColor Green
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "  ✓ Setup Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

Write-Host "To start the application:" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Start Backend (Terminal 1):" -ForegroundColor Yellow
Write-Host "   cd backend" -ForegroundColor White
Write-Host "   .\venv\Scripts\Activate.ps1" -ForegroundColor White
Write-Host "   python app.py" -ForegroundColor White
Write-Host ""
Write-Host "2. Start Frontend (Terminal 2):" -ForegroundColor Yellow
Write-Host "   npm run dev" -ForegroundColor White
Write-Host ""
Write-Host "3. Open browser:" -ForegroundColor Yellow
Write-Host "   http://localhost:5173" -ForegroundColor White
Write-Host ""
Write-Host "For detailed instructions, see:" -ForegroundColor Cyan
Write-Host "  - QUICKSTART.md (5-minute guide)" -ForegroundColor White
Write-Host "  - README.md (full documentation)" -ForegroundColor White
Write-Host "  - backend/README.md (API docs)" -ForegroundColor White
Write-Host ""
Write-Host "Happy transcribing! 🎉" -ForegroundColor Green
