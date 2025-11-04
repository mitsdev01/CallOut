# Quick run script for Callout.ai (PowerShell)

Write-Host "🎤 Starting Callout.ai..." -ForegroundColor Cyan

# Check if setup has been run
if (-not (Test-Path "uploads") -or -not (Test-Path "generated")) {
    Write-Host "⚠️  First time setup detected. Running setup..." -ForegroundColor Yellow
    .\setup.ps1
}

# Start the application
Write-Host "🚀 Starting Flask server..." -ForegroundColor Green
python app.py


