🎙️ Voice AI Detector — Human vs AI Speech Detection API

A production-ready REST API that detects whether an audio sample is AI-generated (TTS / synthetic) or human speech using machine learning–based audio feature analysis.

Built with an ML pipeline + FastAPI backend + secure API access, this system is designed for AI safety, scam detection, deepfake voice screening, and voice authenticity verification.

🚀 Features

✅ Human vs AI voice classification

✅ Audio feature extraction (MFCC + spectral features)

✅ Trained ML model (RandomForest)

✅ FastAPI REST endpoints

✅ API key authentication

✅ JSON prediction response with confidence score

✅ Production deployment ready

✅ Lightweight and fast inference

✅ Easily extensible to deepfake detection

🧠 ML Pipeline Overview

Input: Audio file (WAV/MP3)

Processing Pipeline:

Audio → Feature Extraction → Feature Vector → ML Model → Prediction → Confidence Score


Extracted Features include:

MFCCs

Spectral centroid

Spectral rolloff

Zero crossing rate

Chroma features

Energy features

Model Used: RandomForest Classifier
(Replace with your exact model details if different)

🏗️ Tech Stack

Python

FastAPI

Scikit-learn

Librosa

NumPy / Pandas

Uvicorn

Render (deployment)

📡 API Endpoints
Health Check
GET /


Response

{
  "status": "ok",
  "service": "voice-ai-detector"
}

Predict Voice Type
POST /predict


Headers

x-api-key: ********
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

Add header:

x-api-key: ********


Keys are validated server-side before inference.

⚙️ Local Setup
1️⃣ Clone Repo
git clone https://github.com/Shivang1109/voice-ai-detector.git
cd voice-ai-detector

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # mac/linux
venv\Scripts\activate      # windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Server
uvicorn app.main:app --reload

☁️ Deployment

The API is deployed on Render (or your platform).

Example:

https://your-deployment-url.onrender.com/docs


Interactive Swagger docs available at /docs.

📊 Model Training (Summary)

Dataset: (add your dataset name)

Classes: Human / AI speech

Training method: Supervised classification

Evaluation metric: Accuracy / F1 Score

Feature engineering: Audio signal processing features

(Add your real numbers here for credibility.)

🧪 Example Use Cases

Voice deepfake detection

Scam call screening

AI voice misuse prevention

Media authenticity verification

Voice KYC validation

AI safety tooling

🔮 Future Improvements

Real-time streaming detection

Deepfake voice fingerprinting

Transformer / CNN audio models

Model explainability layer

Web dashboard UI

Multi-language voice robustness

Adversarial audio testing

👨‍💻 Author

Shivang Pathak
B.Tech — Backend + AI Systems Developer
Focused on AI Security, Agentic Systems, and Public-Impact AI
