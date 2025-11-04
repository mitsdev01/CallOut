#!/bin/bash

echo "🚀 Setting up Callout.ai..."
echo "================================"

# Create virtual environment (optional, for local setup)
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment (if not on Replit)
if [ -z "$REPL_ID" ]; then
    echo "🔧 Activating virtual environment..."
    source venv/bin/activate
fi

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p uploads
mkdir -p generated
mkdir -p templates
mkdir -p static

# Download Coqui TTS models (this may take a while)
echo "🤖 Downloading AI models..."
python3 << EOF
try:
    from TTS.api import TTS
    print("Initializing TTS model...")
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
    print("✅ TTS model downloaded successfully!")
except Exception as e:
    print(f"⚠️  Note: TTS model will be downloaded on first use. Error: {e}")
EOF

echo ""
echo "✅ Setup complete!"
echo "================================"
echo ""
echo "🎯 Next steps:"
echo "1. (Optional) Set up ElevenLabs API:"
echo "   - Get an API key from https://elevenlabs.io"
echo "   - In Replit: Add ELEVENLABS_API_KEY to Secrets"
echo "   - Add USE_ELEVENLABS_API=true to Secrets"
echo ""
echo "2. Run the app:"
echo "   python app.py"
echo ""
echo "3. Open in browser at http://localhost:5000"
echo ""
echo "📝 Note: Using Coqui TTS (open source) by default."
echo "   For better quality, use ElevenLabs API (requires subscription)"
echo ""


