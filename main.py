from fastapi import FastAPI, Header, HTTPException
import base64, joblib
from features import extract_features

app = FastAPI()

model = joblib.load("voice_model.pkl")
API_KEY = "CHANGE_THIS_KEY"

@app.post("/detect-voice")
def detect_voice(data: dict, x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    audio_bytes = base64.b64decode(data["audio_base64"])

    with open("temp.mp3", "wb") as f:
        f.write(audio_bytes)

    feat = extract_features("temp.mp3").reshape(1, -1)
    prob = model.predict_proba(feat)[0][1]

    return {
        "result": "AI_GENERATED" if prob > 0.5 else "HUMAN",
        "confidence": round(float(prob), 3)
    }
