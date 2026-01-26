"""
Transcripto Backend - Flask API with OpenAI Whisper
Audio-to-Text transcription service using Whisper AI
"""

import os
import sys
import tempfile
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import logging

# Suppress numpy warnings
import warnings
warnings.filterwarnings('ignore')

# Import whisper after Flask to avoid initialization issues
import whisper

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for frontend communication
CORS(app, resources={r"/api/*": {"origins": ["http://localhost:5173", "http://localhost:5174"]}})

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration
ALLOWED_EXTENSIONS = {'mp3', 'wav', 'm4a', 'flac', 'ogg', 'aac', 'wma', 'opus'}
MAX_FILE_SIZE = 25 * 1024 * 1024  # 25MB limit

# Load Whisper model (using 'tiny' by default for fast startup)
# Options: tiny, base, small, medium, large
MODEL_NAME = os.getenv('WHISPER_MODEL', 'base')
logger.info(f"Loading Whisper model: {MODEL_NAME}")
model = whisper.load_model(MODEL_NAME)
logger.info("Whisper model loaded successfully!")


def allowed_file(filename):
    """Check if uploaded file has allowed extension"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint to verify backend is running"""
    return jsonify({
        'status': 'healthy',
        'service': 'Transcripto Backend',
        'model': MODEL_NAME,
        'version': '1.0.0'
    }), 200


@app.route('/api/transcribe', methods=['POST'])
def transcribe_audio():
    """
    Transcribe audio file to text using Whisper
    
    Accepts: multipart/form-data with 'audio' file
    Returns: JSON with transcribed text
    """
    try:
        # Validate request has file
        if 'audio' not in request.files:
            logger.warning("No audio file in request")
            return jsonify({'error': 'No audio file provided'}), 400
        
        file = request.files['audio']
        
        # Validate file was selected
        if file.filename == '':
            logger.warning("Empty filename")
            return jsonify({'error': 'No file selected'}), 400
        
        # Validate file extension
        if not allowed_file(file.filename):
            logger.warning(f"Invalid file type: {file.filename}")
            return jsonify({'error': f'File type not supported. Allowed: {", ".join(ALLOWED_EXTENSIONS)}'}), 400
        
        # Secure the filename
        filename = secure_filename(file.filename)
        logger.info(f"Processing file: {filename}")
        
        # Create temporary file to store upload
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(filename)[1]) as temp_file:
            temp_path = temp_file.name
            file.save(temp_path)
            logger.info(f"File saved to temporary location: {temp_path}")
        
        try:
            # Transcribe audio using Whisper
            logger.info("Starting transcription...")
            result = model.transcribe(temp_path, fp16=False)
            transcription = result.get('text', '').strip()
            
            # Extract basic segments (start/end/text)
            raw_segments = result.get('segments', []) or []
            segments = []
            for seg in raw_segments:
                start = float(seg.get('start', 0.0))
                end = float(seg.get('end', 0.0))
                text = (seg.get('text') or '').strip()
                if not text:
                    continue
                segments.append({
                    'start': start,
                    'end': end,
                    'text': text
                })

            language = result.get('language', 'unknown')
            logger.info(f"Transcription completed. Length: {len(transcription)} characters")

            return jsonify({
                'success': True,
                'transcription': transcription,
                'language': language,
                'filename': filename,
                'segments': segments
            }), 200
            
        finally:
            # Clean up temporary file if it still exists
            if os.path.exists(temp_path):
                os.remove(temp_path)
                logger.info(f"Temporary file deleted: {temp_path}")
    
    except Exception as e:
        logger.error(f"Transcription error: {str(e)}", exc_info=True)
        return jsonify({
            'error': 'Failed to transcribe audio',
            'details': str(e)
        }), 500


@app.errorhandler(413)
def request_entity_too_large(error):
    """Handle file too large error"""
    return jsonify({'error': 'File too large. Maximum size is 25MB'}), 413


@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors"""
    logger.error(f"Internal server error: {str(error)}")
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    # Run Flask development server
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    
    logger.info(f"Starting Transcripto Backend on port {port}")
    logger.info(f"Debug mode: {debug}")
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    )
