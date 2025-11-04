# PowerShell setup script for Windows
Write-Host "🚀 Setting up Callout.ai..." -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan

# Create virtual environment (optional, for local setup)
if (-not (Test-Path "venv")) {
    Write-Host "📦 Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
}

# Activate virtual environment
Write-Host "🔧 Activating virtual environment..." -ForegroundColor Yellow
.\venv\Scripts\Activate.ps1

# Upgrade pip
Write-Host "⬆️  Upgrading pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip

# Install dependencies
Write-Host "📥 Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

# Create necessary directories
Write-Host "📁 Creating directories..." -ForegroundColor Yellow
New-Item -ItemType Directory -Force -Path uploads | Out-Null
New-Item -ItemType Directory -Force -Path generated | Out-Null
New-Item -ItemType Directory -Force -Path templates | Out-Null
New-Item -ItemType Directory -Force -Path static | Out-Null

# Download Coqui TTS models
Write-Host "🤖 Downloading AI models..." -ForegroundColor Yellow
python -c @"
try:
    from TTS.api import TTS
    print('Initializing TTS model...')
    tts = TTS('tts_models/multilingual/multi-dataset/xtts_v2')
    print('✅ TTS model downloaded successfully!')
except Exception as e:
    print(f'⚠️  Note: TTS model will be downloaded on first use. Error: {e}')
"@

Write-Host ""
Write-Host "✅ Setup complete!" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "🎯 Next steps:" -ForegroundColor Yellow
Write-Host "1. (Optional) Set up ElevenLabs API:"
Write-Host "   - Get an API key from https://elevenlabs.io"
Write-Host "   - Set environment variables:"
Write-Host "     `$env:ELEVENLABS_API_KEY='your-api-key'"
Write-Host "     `$env:USE_ELEVENLABS_API='true'"
Write-Host ""
Write-Host "2. Run the app:"
Write-Host "   python app.py"
Write-Host ""
Write-Host "3. Open in browser at http://localhost:5000"
Write-Host ""
Write-Host "📝 Note: Using Coqui TTS (open source) by default." -ForegroundColor Gray
Write-Host "   For better quality, use ElevenLabs API (requires subscription)" -ForegroundColor Gray
Write-Host ""


