"""
Transcripto Backend - Simple Mock for Testing
"""

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import logging

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for frontend communication
CORS(app, resources={r"/api/*": {"origins": ["http://localhost:5173", "http://localhost:5174", "http://localhost:5000"]}})

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration
ALLOWED_EXTENSIONS = {'mp3', 'wav', 'm4a', 'flac', 'ogg', 'aac', 'wma', 'opus'}
MAX_FILE_SIZE = 25 * 1024 * 1024  # 25MB limit


def allowed_file(filename):
    """Check if uploaded file has allowed extension"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Transcripto Backend',
        'version': '1.0.0',
        'note': 'Demo Mode - Mock Transcription'
    }), 200


@app.route('/api/transcribe', methods=['POST'])
def transcribe_audio():
    """
    Demo transcription endpoint - returns sample data
    """
    try:
        if 'audio' not in request.files:
            return jsonify({'error': 'No audio file provided'}), 400
        
        file = request.files['audio']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': f'File type not supported. Allowed: {", ".join(ALLOWED_EXTENSIONS)}'}), 400
        
        filename = secure_filename(file.filename)
        logger.info(f"Processing file: {filename}")
        
        # Demo response - replace with real Whisper when Python compatibility is fixed
        return jsonify({
            'success': True,
            'transcription': 'This is a demo transcription. To enable real transcription, upgrade to Python 3.11 or install a PyTorch-compatible version.',
            'language': 'en',
            'filename': filename,
            'segments': [
                {
                    'start': 0.0,
                    'end': 2.5,
                    'text': 'This is a demo transcription.'
                },
                {
                    'start': 2.5,
                    'end': 5.0,
                    'text': 'To enable real transcription,'
                },
                {
                    'start': 5.0,
                    'end': 7.5,
                    'text': 'upgrade to Python 3.11'
                }
            ]
        }), 200
            
    except Exception as e:
        logger.error(f"Transcription error: {str(e)}", exc_info=True)
        return jsonify({
            'error': 'Failed to process audio',
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
    port = int(os.getenv('PORT', 5000))
    logger.info(f"Starting Transcripto Backend (Demo Mode) on port {port}")
    app.run(host='0.0.0.0', port=port, debug=True)
