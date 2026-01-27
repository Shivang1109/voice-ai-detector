import librosa
import numpy as np

def extract_features(file):
    y, sr = librosa.load(file, sr=None)

    mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20), axis=1)
    flatness = np.mean(librosa.feature.spectral_flatness(y=y))
    centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))
    zcr = np.mean(librosa.feature.zero_crossing_rate(y))

    return np.hstack([mfcc, flatness, centroid, zcr])
