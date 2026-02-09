🎙️ Voice AI Detector — Human vs AI Speech Detection API

A production-ready REST API that detects whether an audio sample is AI-generated (TTS / synthetic) or human speech using machine-learning–based audio feature analysis.

Built with a complete ML pipeline + FastAPI backend + secure API access, this system is designed for AI safety, scam detection, deepfake voice screening, and voice authenticity verification.

🚀 Features

✅ Human vs AI voice classification

✅ Audio feature extraction (MFCC + spectral features)

✅ Trained ML model (RandomForest Classifier)

✅ FastAPI REST endpoints

✅ API key authentication

✅ JSON prediction response with confidence score

✅ Production deployment ready

✅ Lightweight and fast inference

✅ Modular ML pipeline

✅ Easily extensible to deepfake detection

🧠 ML Pipeline Overview

Input: Audio file (WAV / MP3)

Processing Flow:

Audio File
   ↓
Feature Extraction
   ↓
Feature Vector
   ↓
ML Model
   ↓
Prediction + Confidence Score

Extracted Audio Features

MFCCs (Mel-Frequency Cepstral Coefficients)

Spectral centroid

Spectral rolloff

Zero crossing rate

Chroma features

Energy features

Model Used: RandomForest Classifier
(Replace with your exact model details if updated.)

🏗️ Tech Stack

Python

FastAPI

Scikit-learn

Librosa

NumPy

Pandas

Uvicorn

Render (Deployment)

📡 API Endpoints
✅ Health Check

GET /

{
  "status": "ok",
  "service": "voice-ai-detector"
}

🎯 Predict Voice Type

POST /predict

Headers

x-api-key: YOUR_API_KEY
Content-Type: multipart/form-data


Body

audio_file: <upload file>


Response

{
  "prediction": "AI",
  "confidence": 0.91,
  "label_id": 1
}

🔐 Authentication

This API uses API Key authentication.

Include header in every prediction request:

x-api-key: YOUR_API_KEY


Requests without valid keys are rejected before model inference.

⚙️ Local Setup
1️⃣ Clone Repository
git clone https://github.com/Shivang1109/voice-ai-detector.git
cd voice-ai-detector

2️⃣ Create Virtual Environment

Mac / Linux

python -m venv venv
source venv/bin/activate


Windows

venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Server
uvicorn app.main:app --reload


Server runs at:

http://127.0.0.1:8000


Swagger Docs:

http://127.0.0.1:8000/docs

☁️ Deployment

The API is production deployed on Render.

Live API Docs:

https://voice-ai-detector-lh2e.onrender.com/docs


Interactive Swagger UI available for live testing.

📊 Model Training Summary

Dataset: (add dataset name here)

Classes: Human vs AI speech

Training Type: Supervised classification

Feature Engineering: Audio signal processing features

Metrics: (add accuracy / F1 / precision / recall)

Add your real evaluation numbers here for technical credibility.

🧪 Example Use Cases

Deepfake voice detection

Scam & fraud call screening

AI voice misuse prevention

Media authenticity verification

Voice-based KYC validation

AI safety tooling

Forensics & investigation support

🔮 Future Improvements

Real-time streaming detection

Deepfake voice fingerprinting

CNN / Transformer audio models

Model explainability layer

Web dashboard UI

Multi-language robustness

Adversarial audio testing

Batch audio analysis endpoint

👨‍💻 Author

Shivang Pathak
B.Tech — Backend + AI Systems Developer
Focused on AI Security, Agentic Systems, and Public-Impact AI
