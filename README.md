# 🎤 Callout.ai

An AI-powered voice cloning application that records your voice and generates authentic-sounding callout messages for sick days.

## ✨ Features

- 🎙️ **Voice Recording**: Record a short sample of your voice directly in the browser
- 🤖 **AI Voice Cloning**: Uses advanced AI models to replicate your voice
- 📝 **Custom Messages**: Write your own callout message or use the default
- 💾 **Download Audio**: Get a .wav file ready to use
- 🎨 **Modern UI**: Beautiful, responsive interface with smooth animations
- 🚀 **Replit Ready**: Optimized for easy deployment on Replit

## 🚀 Quick Start on Replit

1. **Fork/Import this project to Replit**

2. **Click the "Run" button** - Replit will automatically:
   - Install all dependencies
   - Set up the environment
   - Start the Flask server

3. **Use the app**:
   - Record a 10-15 second voice sample
   - Upload the sample
   - Generate your callout message
   - Download the audio file

## 🛠️ Local Setup

### Prerequisites

- Python 3.10 or higher
- FFmpeg (for audio processing)
- espeak-ng (for text-to-speech)

### Installation

#### On Linux/Mac:

```bash
# Clone the repository
git clone <your-repo-url>
cd CallOut

# Run setup script
chmod +x setup.sh
./setup.sh

# Start the application
python app.py
```

#### On Windows:

```powershell
# Clone the repository
git clone <your-repo-url>
cd CallOut

# Run setup script
.\setup.ps1

# Start the application
python app.py
```

#### Manual Installation:

```bash
# Install dependencies
pip install -r requirements.txt

# Create necessary directories
mkdir uploads generated templates static

# Run the app
python app.py
```

## 🔧 Configuration

### Voice Cloning Options

The app supports two voice cloning methods:

#### 1. Coqui TTS (Default - Open Source)

- ✅ Free and open source
- ✅ Runs locally
- ✅ No API key required
- ⚠️ Slower processing
- ⚠️ May require more system resources

No configuration needed - works out of the box!

#### 2. ElevenLabs API (Optional - Better Quality)

- ✅ High-quality voice cloning
- ✅ Fast processing
- ⚠️ Requires paid subscription
- ⚠️ API key needed

**To enable ElevenLabs:**

1. Sign up at [ElevenLabs](https://elevenlabs.io)
2. Get your API key
3. In Replit:
   - Go to "Secrets" (🔒 icon in left sidebar)
   - Add secret: `ELEVENLABS_API_KEY` = `your-api-key`
   - Add secret: `USE_ELEVENLABS_API` = `true`

4. For local development:
```bash
export ELEVENLABS_API_KEY="your-api-key"
export USE_ELEVENLABS_API="true"
```

Or on Windows PowerShell:
```powershell
$env:ELEVENLABS_API_KEY="your-api-key"
$env:USE_ELEVENLABS_API="true"
```

## 📁 Project Structure

```
CallOut/
├── app.py                 # Flask backend application
├── requirements.txt       # Python dependencies
├── setup.sh              # Linux/Mac setup script
├── setup.ps1             # Windows PowerShell setup script
├── .replit               # Replit configuration
├── replit.nix            # Replit Nix environment
├── templates/
│   └── index.html        # Main HTML interface
├── static/
│   ├── style.css         # Styling
│   └── script.js         # Frontend JavaScript
├── uploads/              # Uploaded voice samples (created automatically)
└── generated/            # Generated audio files (created automatically)
```

## 🎯 How to Use

### Step 1: Record Your Voice

1. Click "Start Recording"
2. Speak naturally for 10-15 seconds
3. Say something like: "Hi, this is [your name]. I'm calling to let you know about my schedule today."
4. Click "Stop Recording"
5. Listen to your recording to verify quality
6. Click "Upload Voice Sample"

### Step 2: Generate Callout

1. Review or customize the default callout message
2. Click "Generate Callout Voice"
3. Wait for the AI to process (may take 30-60 seconds)

### Step 3: Download and Use

1. Listen to the generated audio
2. Click "Download Audio File"
3. Use the audio file for your callout

## 🔒 Privacy & Security

- All voice samples are stored temporarily on the server
- Files are not shared with third parties (except when using ElevenLabs API)
- Voice samples are associated with random UUIDs, not personal information
- Consider clearing the `uploads/` and `generated/` directories periodically

## ⚠️ Disclaimer

This application is for **entertainment and educational purposes only**. 

- Use responsibly and ethically
- Follow your employer's policies
- Be honest with your employer
- Misrepresenting your identity may have legal consequences
- The creators are not responsible for misuse of this application

## 🐛 Troubleshooting

### "Could not access microphone"
- Grant microphone permissions in your browser
- Use HTTPS (required for microphone access in most browsers)
- On Replit, the app should automatically use HTTPS

### "Error generating voice clone"
- First generation may be slow as models download
- Check that all dependencies are installed
- Try using ElevenLabs API for more reliable results
- Check server logs for detailed error messages

### Slow Performance
- Coqui TTS requires significant CPU/RAM
- Consider using ElevenLabs API for faster results
- Close other applications to free up resources

### Audio Quality Issues
- Record in a quiet environment
- Speak clearly and at a normal pace
- Use a good quality microphone
- Try the ElevenLabs API for better output quality

## 🛠️ Technical Details

### Backend
- **Framework**: Flask 3.0
- **Voice Cloning**: Coqui TTS (XTTS v2) or ElevenLabs API
- **Audio Processing**: PyDub, SoundFile
- **ML Framework**: PyTorch

### Frontend
- **Pure JavaScript** (no frameworks)
- **MediaRecorder API** for audio recording
- **Fetch API** for backend communication
- **Responsive CSS** with modern design

### AI Models
- **Coqui TTS XTTS v2**: Multilingual text-to-speech with voice cloning
- **ElevenLabs**: State-of-the-art voice cloning API

## 📝 License

This project is provided as-is for educational purposes. Please use responsibly.

## 🤝 Contributing

This is a demonstration project. Feel free to fork and modify for your own use.

## 📧 Support

For issues or questions:
1. Check the troubleshooting section
2. Review error messages in the browser console
3. Check server logs in the Replit console

## 🎉 Credits

- Built with Flask, Coqui TTS, and modern web technologies
- Designed for Replit hosting
- Created as an educational demonstration of voice cloning technology

---

**Remember**: Use this technology ethically and responsibly! 🙏


