import base64
import requests

url = "https://voice-ai-detector-lh2e.onrender.com/detect-voice"
api_key = "SHIVANG123"   # must match main.py

with open("sample.mp3", "rb") as f:
    b64 = base64.b64encode(f.read()).decode()

payload = {
    "language": "English",      # because your audio is English
    "audioFormat": "mp3",
    "audioBase64": b64
}

headers = {
    "x-api-key": api_key
}

r = requests.post(url, json=payload, headers=headers)
print(r.status_code)
print(r.text)
