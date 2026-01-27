import base64
import requests

url = "http://127.0.0.1:8000/detect-voice"
api_key = "CHANGE_THIS_KEY"

with open("sample.wav", "rb") as f:
    b64 = base64.b64encode(f.read()).decode()

data = {"audio_base64": b64}
headers = {"x-api-key": api_key}

r = requests.post(url, json=data, headers=headers)
print(r.status_code)
print(r.text)
