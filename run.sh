#!/bin/bash
# Quick run script for Callout.ai

echo "🎤 Starting Callout.ai..."

# Check if setup has been run
if [ ! -d "uploads" ] || [ ! -d "generated" ]; then
    echo "⚠️  First time setup detected. Running setup..."
    ./setup.sh
fi

# Start the application
echo "🚀 Starting Flask server..."
python app.py


