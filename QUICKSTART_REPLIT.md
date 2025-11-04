# 🚀 Replit Quick Start Guide

## Getting Started in 3 Steps

### 1️⃣ Import to Replit

1. Go to [Replit](https://replit.com)
2. Click "Create Repl"
3. Choose "Import from GitHub" (or upload these files)
4. Select Python as the language

### 2️⃣ Click "Run"

That's it! Replit will automatically:
- Install all dependencies from `requirements.txt`
- Set up the environment using `replit.nix`
- Start the Flask server
- Open the web interface

### 3️⃣ Use the App

1. Click on the webview window that opens
2. Allow microphone access when prompted
3. Record your voice sample (10-15 seconds)
4. Generate your callout message
5. Download and use!

---

## 🔧 Optional: Better Voice Quality with ElevenLabs

For production-quality voice cloning:

1. **Get ElevenLabs API Key**
   - Sign up at [elevenlabs.io](https://elevenlabs.io)
   - Go to your profile → API Keys
   - Copy your API key

2. **Add to Replit Secrets**
   - In Replit, click the 🔒 Lock icon in the left sidebar
   - Click "Secrets"
   - Add two secrets:
     ```
     ELEVENLABS_API_KEY = your_api_key_here
     USE_ELEVENLABS_API = true
     ```

3. **Restart the App**
   - Click "Stop" then "Run" again
   - Now uses ElevenLabs for better quality!

---

## 📊 Resource Usage

### Free Tier (Coqui TTS - Default)
- ✅ Works on Replit free tier
- ⚠️ First generation may take 2-3 minutes (downloading models)
- ⚠️ Subsequent generations: 30-60 seconds
- ⚠️ May timeout on very limited resources

### With ElevenLabs API
- ✅ Fast (5-10 seconds per generation)
- ✅ Better voice quality
- ✅ More reliable on free tier
- ⚠️ Requires API subscription (~$5-11/month)

---

## 🐛 Troubleshooting

### "Application Error" on start
- Wait a moment, dependencies are installing
- Check the Console tab for progress
- First run takes 3-5 minutes

### Microphone not working
- Must use HTTPS (Replit provides this automatically)
- Click "Allow" when browser asks for microphone permission
- Try refreshing the page

### Voice generation times out
- First generation downloads AI models (takes longer)
- Try again - second attempt should be faster
- Consider using ElevenLabs API for reliability

### Can't access the web interface
- Make sure the Repl is running
- Click the "Open in new tab" button
- Check that port 5000 is configured correctly

---

## 💡 Tips

1. **Recording Quality**
   - Use a quiet environment
   - Speak naturally and clearly
   - 10-15 seconds is optimal
   - Longer samples = better cloning

2. **Message Length**
   - Keep callout messages short (1-2 sentences)
   - Longer messages take more time to generate
   - Be concise and professional

3. **Saving Your Work**
   - Generated audio files are in the `generated/` folder
   - Download them before they're automatically cleaned up
   - Voice samples in `uploads/` are temporary

---

## 🎯 Next Steps

Once you have your callout audio:
1. Download the `.wav` file
2. Test it to ensure quality
3. Use it responsibly!

Remember: This is for entertainment/educational purposes. Always be honest with your employer! 🙏

---

**Need Help?** Check the main [README.md](README.md) for detailed documentation.


