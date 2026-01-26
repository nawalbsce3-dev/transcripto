"""
Transcripto Backend - Lightweight Demo Version
Demo API without Whisper for quick testing
Real Whisper integration in app_full.py
"""

import os
import tempfile
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import logging

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

logger.info("Transcripto Backend (Demo Mode) initialized")
logger.info("Real Whisper integration available in app_full.py")


def allowed_file(filename):
    """Check if uploaded file has allowed extension"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint to verify backend is running"""
    return jsonify({
        'status': 'healthy',
        'service': 'Transcripto Backend (Demo)',
        'mode': 'demo',
        'version': '1.0.0'
    }), 200


@app.route('/api/transcribe', methods=['POST'])
def transcribe_audio():
    """
    Demo transcription endpoint - returns dummy text
    
    Accepts: multipart/form-data with 'audio' file
    Returns: JSON with demo transcription
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
            # Demo: Return sample transcription (no real AI processing)
            logger.info("Generating demo transcription...")
            
            demo_transcription = f"""
            This is a demo transcription of {filename}. 
            
            In production, this would contain the actual AI-powered transcription 
            from OpenAI Whisper. 
            
            To use the real Whisper integration:
            1. Ensure you have FFmpeg installed
            2. Install openai-whisper: pip install openai-whisper
            3. Run: python app_full.py instead of python app.py
            
            The real version will transcribe your audio file with high accuracy
            using the Whisper AI model. This demo version allows you to test
            the frontend UI and API integration immediately.
            """.strip()
            
            logger.info(f"Demo transcription generated. Length: {len(demo_transcription)} characters")
            
            # Return successful response
            return jsonify({
                'success': True,
                'transcription': demo_transcription,
                'language': 'en',
                'filename': filename,
                'mode': 'demo'
            }), 200
            
        finally:
            # Clean up temporary file
            if os.path.exists(temp_path):
                os.remove(temp_path)
                logger.info(f"Temporary file deleted: {temp_path}")
    
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
    # Run Flask development server
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    
    logger.info(f"Starting Transcripto Backend (DEMO MODE) on port {port}")
    logger.info(f"Debug mode: {debug}")
    logger.info("Frontend available at: http://localhost:5173")
    logger.info("API Health Check: http://localhost:5000/api/health")
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    )
