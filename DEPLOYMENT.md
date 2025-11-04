# 🚀 Deployment Guide

## Deploying to Replit (Recommended)

### Why Replit?
- ✅ Free hosting tier available
- ✅ Automatic HTTPS (required for microphone access)
- ✅ Easy setup and deployment
- ✅ Built-in secrets management
- ✅ No server configuration needed

### Steps:

1. **Create a Replit Account**
   - Go to [replit.com](https://replit.com)
   - Sign up (free)

2. **Import Project**
   - Click "Create Repl"
   - Select "Import from GitHub" or upload files
   - Choose Python template

3. **Configure** (Optional)
   - Add secrets for ElevenLabs API if desired
   - Secrets: 🔒 icon → Add ELEVENLABS_API_KEY

4. **Deploy**
   - Click "Run"
   - Share the URL with users
   - For always-on hosting, upgrade to Replit Hacker plan

---

## Alternative Deployment Options

### Option 1: Heroku

1. Install Heroku CLI
2. Create `Procfile`:
   ```
   web: python app.py
   ```
3. Deploy:
   ```bash
   heroku create callout-ai
   heroku config:set USE_ELEVENLABS_API=false
   git push heroku main
   ```

**Note**: Heroku no longer has a free tier.

### Option 2: Railway.app

1. Connect GitHub repo to Railway
2. Set environment variables in Railway dashboard
3. Deploy automatically on push

**Note**: Free tier available with limitations.

### Option 3: Render.com

1. Create new Web Service
2. Connect GitHub repo
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `python app.py`
5. Add environment variables

**Note**: Free tier spins down after inactivity.

### Option 4: Docker

1. Create `Dockerfile`:
   ```dockerfile
   FROM python:3.10-slim
   
   WORKDIR /app
   
   # Install system dependencies
   RUN apt-get update && apt-get install -y \
       ffmpeg \
       espeak-ng \
       portaudio19-dev \
       && rm -rf /var/lib/apt/lists/*
   
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   
   COPY . .
   
   RUN mkdir -p uploads generated
   
   EXPOSE 5000
   
   CMD ["python", "app.py"]
   ```

2. Build and run:
   ```bash
   docker build -t callout-ai .
   docker run -p 5000:5000 callout-ai
   ```

### Option 5: VPS (DigitalOcean, Linode, etc.)

1. Create Ubuntu 22.04 server
2. Install dependencies:
   ```bash
   sudo apt update
   sudo apt install python3.10 python3-pip ffmpeg espeak-ng
   ```
3. Clone project
4. Run setup script
5. Use systemd or supervisor to keep running
6. Set up Nginx as reverse proxy
7. Get SSL certificate with Let's Encrypt

---

## Production Considerations

### Performance
- Coqui TTS requires significant CPU/RAM
- Recommend at least 2GB RAM
- Consider using ElevenLabs API for better performance

### Security
- Set `FLASK_ENV=production`
- Set `FLASK_DEBUG=false`
- Implement rate limiting
- Add authentication if making public
- Use HTTPS (required for microphone access)

### Scaling
- Voice generation is CPU-intensive
- Consider job queue (Celery, RQ) for async processing
- Use ElevenLabs API to offload AI processing
- Cache generated voices if same message is common

### Storage
- Implement cleanup of old files
- Set file size limits
- Consider cloud storage (S3, Google Cloud Storage)

### Monitoring
- Add logging (e.g., LogTail, Papertrail)
- Monitor server resources
- Track API usage if using ElevenLabs
- Set up error alerts

---

## Environment Variables

Required for production:

```bash
# Flask
PORT=5000
FLASK_ENV=production
FLASK_DEBUG=false

# Voice Cloning
USE_ELEVENLABS_API=true  # Recommended for production
ELEVENLABS_API_KEY=your_key_here

# Security (add these)
SECRET_KEY=your_secret_key_here
MAX_CONTENT_LENGTH=16777216  # 16MB
```

---

## Cost Estimates

### Replit
- Free tier: Limited resources, spins down
- Hacker ($7/mo): Always on, more resources
- Pro ($20/mo): Priority resources

### ElevenLabs API
- Free tier: 10,000 characters/month
- Starter ($5/mo): 30,000 characters/month
- Creator ($11/mo): 100,000 characters/month

### Alternatives
- Railway: Free tier + pay-as-you-go
- Render: Free tier (spins down)
- VPS: $5-10/month (DigitalOcean, Linode)

---

## Recommended Setup for Production

**Best Balance of Cost/Performance:**

1. **Hosting**: Replit Hacker plan ($7/mo)
2. **Voice AI**: ElevenLabs Starter ($5/mo)
3. **Total**: ~$12/month

**Benefits:**
- Always online
- Fast voice generation
- Easy maintenance
- Automatic HTTPS
- No server management

**Cheapest Option:**
- Replit free tier + Coqui TTS (local)
- Total: $0/month
- Trade-off: Slower, may spin down, less reliable

---

## Support

For deployment issues:
1. Check Replit status page
2. Review server logs
3. Check API quotas/limits
4. Verify environment variables
5. Test locally first

Good luck with your deployment! 🚀


