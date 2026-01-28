from fastapi import FastAPI, Header
import base64
import joblib
from features import extract_features


app = FastAPI()


# Load trained model
model = joblib.load("voice_model.pkl")

# API key (must match send_request.py)
API_KEY = "SHIVANG123"

# Allowed languages (fixed)
ALLOWED_LANGUAGES = ["tamil", "english", "hindi", "malayalam", "telugu"]

@app.post("/api/voice-detection")
def voice_detection(data: dict, x_api_key: str = Header(None)):

    # ---------- API KEY VALIDATION ----------
    if x_api_key != API_KEY:
        return {
            "status": "error",
            "message": "Invalid API key or malformed request"
        }

    # ---------- REQUEST VALIDATION ----------
    try:
        language = data["language"].lower()
        audio_format = data["audioFormat"].lower()
        audio_base64 = data["audioBase64"]
    except:
        return {
            "status": "error",
            "message": "Invalid API key or malformed request"
        }

    if language not in ALLOWED_LANGUAGES or audio_format != "mp3":
        return {
            "status": "error",
            "message": "Invalid API key or malformed request"
        }

    # ---------- AUDIO DECODING ----------
    try:
        audio_bytes = base64.b64decode(audio_base64)
        with open("temp.mp3", "wb") as f:
            f.write(audio_bytes)
    except:
        return {
            "status": "error",
            "message": "Invalid API key or malformed request"
        }

    # ---------- PREDICTION ----------
    features = extract_features("temp.mp3").reshape(1, -1)
    prob = model.predict_proba(features)[0][1]

    classification = "AI_GENERATED" if prob > 0.5 else "HUMAN"

    # ---------- FINAL RESPONSE ----------
    return {
        "status": "success",
        "language": data["language"],
        "classification": classification,
        "confidenceScore": round(float(prob), 2),
        "explanation": (
            "Unnatural pitch consistency and robotic speech patterns detected"
            if classification == "AI_GENERATED"
            else "Natural pitch variation and human speech characteristics detected"
        )
    }
