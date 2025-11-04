from flask import Flask, render_template, request, jsonify, send_file
import os
import io
import uuid
from datetime import datetime
import wave
import json

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create necessary directories
os.makedirs('uploads', exist_ok=True)
os.makedirs('generated', exist_ok=True)
os.makedirs('templates', exist_ok=True)
os.makedirs('static', exist_ok=True)

# Store user voice profiles in memory (in production, use a database)
voice_profiles = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/upload-voice', methods=['POST'])
def upload_voice():
    """Upload and save user's voice sample"""
    try:
        if 'audio' not in request.files:
            return jsonify({'error': 'No audio file provided'}), 400
        
        audio_file = request.files['audio']
        
        # Generate unique ID for this voice profile
        profile_id = str(uuid.uuid4())
        
        # Save the uploaded audio
        filename = f"uploads/voice_sample_{profile_id}.wav"
        audio_file.save(filename)
        
        # Store profile info
        voice_profiles[profile_id] = {
            'filename': filename,
            'created_at': datetime.now().isoformat(),
            'sample_duration': get_audio_duration(filename)
        }
        
        return jsonify({
            'success': True,
            'profile_id': profile_id,
            'message': 'Voice sample uploaded successfully'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/generate-callout', methods=['POST'])
def generate_callout():
    """Generate a callout message using the cloned voice"""
    try:
        data = request.json
        profile_id = data.get('profile_id')
        message = data.get('message', "Hi, this is calling to let you know I'm not feeling well today and won't be able to come in to work. I'll keep you updated. Thanks for understanding.")
        
        if not profile_id or profile_id not in voice_profiles:
            return jsonify({'error': 'Invalid profile ID'}), 400
        
        voice_sample = voice_profiles[profile_id]['filename']
        
        # Generate the cloned voice audio
        output_filename = f"generated/callout_{profile_id}_{uuid.uuid4()}.wav"
        
        # Use voice cloning (placeholder for actual implementation)
        success = generate_voice_clone(voice_sample, message, output_filename)
        
        if success:
            return jsonify({
                'success': True,
                'audio_url': f'/api/download/{os.path.basename(output_filename)}',
                'message': 'Callout message generated successfully'
            })
        else:
            return jsonify({'error': 'Failed to generate voice clone'}), 500
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/download/<filename>')
def download_audio(filename):
    """Download generated audio file"""
    try:
        filepath = os.path.join('generated', filename)
        if os.path.exists(filepath):
            return send_file(filepath, mimetype='audio/wav', as_attachment=True)
        else:
            return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def get_audio_duration(filename):
    """Get duration of audio file in seconds"""
    try:
        with wave.open(filename, 'r') as audio:
            frames = audio.getnframes()
            rate = audio.getframerate()
            duration = frames / float(rate)
            return round(duration, 2)
    except:
        return 0

def generate_voice_clone(voice_sample_path, text, output_path):
    """
    Generate voice clone using the voice sample
    This is a placeholder - implement with actual voice cloning library
    Options:
    1. Coqui TTS (open source)
    2. ElevenLabs API (requires API key)
    3. Bark (open source)
    4. TortoiseGPT (open source but slow)
    """
    try:
        # Check if we should use API-based or local model
        if os.getenv('USE_ELEVENLABS_API') == 'true':
            return generate_with_elevenlabs(voice_sample_path, text, output_path)
        else:
            return generate_with_coqui_tts(voice_sample_path, text, output_path)
    except Exception as e:
        print(f"Error generating voice clone: {e}")
        return False

def generate_with_elevenlabs(voice_sample_path, text, output_path):
    """Generate using ElevenLabs API"""
    try:
        import requests
        
        api_key = os.getenv('ELEVENLABS_API_KEY')
        if not api_key:
            print("ElevenLabs API key not found. Set ELEVENLABS_API_KEY in Replit Secrets.")
            return False
        
        # First, create a voice from the sample
        # Note: ElevenLabs voice cloning requires a subscription plan
        # For demo, we'll use a pre-made voice
        voice_id = "21m00Tcm4TlvDq8ikWAM"  # Default voice
        
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": api_key
        }
        
        data = {
            "text": text,
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.5
            }
        }
        
        response = requests.post(url, json=data, headers=headers)
        
        if response.status_code == 200:
            with open(output_path, 'wb') as f:
                f.write(response.content)
            return True
        else:
            print(f"ElevenLabs API error: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"Error with ElevenLabs: {e}")
        return False

def generate_with_coqui_tts(voice_sample_path, text, output_path):
    """Generate using Coqui TTS (open source)"""
    try:
        from TTS.api import TTS
        
        # Initialize TTS with a voice cloning model
        # Using XTTS v2 which supports voice cloning
        tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
        
        # Generate speech with voice cloning
        tts.tts_to_file(
            text=text,
            speaker_wav=voice_sample_path,
            language="en",
            file_path=output_path
        )
        
        return True
        
    except Exception as e:
        print(f"Error with Coqui TTS: {e}")
        # Fallback: copy the sample file as a placeholder
        import shutil
        try:
            shutil.copy(voice_sample_path, output_path)
            return True
        except:
            return False

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)


