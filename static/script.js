let mediaRecorder;
let audioChunks = [];
let recordedBlob;
let startTime;
let timerInterval;
let profileId = null;

// DOM Elements
const recordBtn = document.getElementById('recordBtn');
const stopBtn = document.getElementById('stopBtn');
const playBtn = document.getElementById('playBtn');
const uploadBtn = document.getElementById('uploadBtn');
const audioPlayback = document.getElementById('audioPlayback');
const timer = document.getElementById('timer');
const uploadStatus = document.getElementById('uploadStatus');
const generateBtn = document.getElementById('generateBtn');
const messageInput = document.getElementById('messageInput');
const loading = document.getElementById('loading');
const generateStatus = document.getElementById('generateStatus');
const recordSection = document.getElementById('record-section');
const generateSection = document.getElementById('generate-section');
const resultSection = document.getElementById('result-section');
const resultAudio = document.getElementById('resultAudio');
const downloadBtn = document.getElementById('downloadBtn');
const newCalloutBtn = document.getElementById('newCalloutBtn');

// Recording functionality
recordBtn.addEventListener('click', async () => {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);
        audioChunks = [];

        mediaRecorder.ondataavailable = (event) => {
            audioChunks.push(event.data);
        };

        mediaRecorder.onstop = () => {
            recordedBlob = new Blob(audioChunks, { type: 'audio/wav' });
            const audioUrl = URL.createObjectURL(recordedBlob);
            audioPlayback.src = audioUrl;
            audioPlayback.style.display = 'block';
            playBtn.disabled = false;
            uploadBtn.disabled = false;
            
            // Stop all tracks
            stream.getTracks().forEach(track => track.stop());
        };

        mediaRecorder.start();
        recordBtn.disabled = true;
        stopBtn.disabled = false;
        playBtn.disabled = true;
        uploadBtn.disabled = true;
        
        // Start timer
        startTime = Date.now();
        timer.classList.add('recording');
        timerInterval = setInterval(updateTimer, 100);
        
        showStatus(uploadStatus, 'Recording... Speak naturally and clearly.', 'info');
    } catch (error) {
        console.error('Error accessing microphone:', error);
        showStatus(uploadStatus, 'Error: Could not access microphone. Please grant permission.', 'error');
    }
});

stopBtn.addEventListener('click', () => {
    if (mediaRecorder && mediaRecorder.state === 'recording') {
        mediaRecorder.stop();
        recordBtn.disabled = false;
        stopBtn.disabled = true;
        timer.classList.remove('recording');
        clearInterval(timerInterval);
        showStatus(uploadStatus, 'Recording complete! Review and upload your sample.', 'success');
    }
});

playBtn.addEventListener('click', () => {
    audioPlayback.play();
});

function updateTimer() {
    const elapsed = Date.now() - startTime;
    const seconds = Math.floor(elapsed / 1000);
    const milliseconds = Math.floor((elapsed % 1000) / 100);
    timer.textContent = `${String(seconds).padStart(2, '0')}:${milliseconds}`;
}

// Upload voice sample
uploadBtn.addEventListener('click', async () => {
    if (!recordedBlob) {
        showStatus(uploadStatus, 'No recording found. Please record your voice first.', 'error');
        return;
    }

    const formData = new FormData();
    formData.append('audio', recordedBlob, 'voice_sample.wav');

    uploadBtn.disabled = true;
    uploadBtn.innerHTML = '<span class="btn-icon">⏳</span> Uploading...';

    try {
        const response = await fetch('/api/upload-voice', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (response.ok) {
            profileId = data.profile_id;
            showStatus(uploadStatus, '✅ Voice sample uploaded successfully!', 'success');
            
            // Show generate section
            setTimeout(() => {
                generateSection.style.display = 'block';
                generateSection.scrollIntoView({ behavior: 'smooth' });
            }, 1000);
        } else {
            showStatus(uploadStatus, `Error: ${data.error}`, 'error');
            uploadBtn.disabled = false;
            uploadBtn.innerHTML = '<span class="btn-icon">⬆️</span> Upload Voice Sample';
        }
    } catch (error) {
        console.error('Upload error:', error);
        showStatus(uploadStatus, 'Error uploading file. Please try again.', 'error');
        uploadBtn.disabled = false;
        uploadBtn.innerHTML = '<span class="btn-icon">⬆️</span> Upload Voice Sample';
    }
});

// Generate callout
generateBtn.addEventListener('click', async () => {
    if (!profileId) {
        showStatus(generateStatus, 'Please upload a voice sample first.', 'error');
        return;
    }

    const message = messageInput.value.trim();
    if (!message) {
        showStatus(generateStatus, 'Please enter a callout message.', 'error');
        return;
    }

    generateBtn.disabled = true;
    loading.style.display = 'block';
    generateStatus.style.display = 'none';

    try {
        const response = await fetch('/api/generate-callout', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                profile_id: profileId,
                message: message
            })
        });

        const data = await response.json();
        loading.style.display = 'none';

        if (response.ok) {
            showStatus(generateStatus, '✅ Callout generated successfully!', 'success');
            
            // Set up result audio
            resultAudio.src = data.audio_url;
            downloadBtn.onclick = () => {
                window.open(data.audio_url, '_blank');
            };
            
            // Show result section
            setTimeout(() => {
                resultSection.style.display = 'block';
                resultSection.scrollIntoView({ behavior: 'smooth' });
            }, 1000);
        } else {
            showStatus(generateStatus, `Error: ${data.error}`, 'error');
            generateBtn.disabled = false;
        }
    } catch (error) {
        console.error('Generation error:', error);
        loading.style.display = 'none';
        showStatus(generateStatus, 'Error generating callout. Please try again.', 'error');
        generateBtn.disabled = false;
    }
});

// New callout button
newCalloutBtn.addEventListener('click', () => {
    // Reset form
    messageInput.value = "Hi, this is calling to let you know I'm not feeling well today and won't be able to come in to work. I'll keep you updated. Thanks for understanding.";
    generateBtn.disabled = false;
    resultSection.style.display = 'none';
    generateStatus.style.display = 'none';
    generateSection.scrollIntoView({ behavior: 'smooth' });
});

function showStatus(element, message, type) {
    element.textContent = message;
    element.className = `status ${type}`;
    element.style.display = 'block';
}


