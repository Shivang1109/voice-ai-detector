import joblib
from features import extract_features

model = joblib.load("voice_model.pkl")

file = "harvard.wav"   # change this to any voice file
feat = extract_features(file).reshape(1, -1)

prob = model.predict_proba(feat)[0][1]

print("AI Probability:", prob)
print("Prediction:", "AI_GENERATED" if prob > 0.5 else "HUMAN")
