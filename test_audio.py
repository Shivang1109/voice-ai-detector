import librosa
import numpy as np

file = "harvard.wav"   # put any small mp3 here

y, sr = librosa.load(file, sr=None)

print("Sample rate:", sr)
print("Wave shape:", y.shape)
print("First 10 samples:", y[:10])
