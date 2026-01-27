import os
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from features import extract_features

X = []
y = []

for label, folder in [(0, "human"), (1, "ai")]:
    path = os.path.join("data", folder)
    for file in os.listdir(path):
        try:
            feat = extract_features(os.path.join(path, file))
            X.append(feat)
            y.append(label)
        except:
            print("Skipped:", file)

X = np.array(X)
y = np.array(y)

print("Training samples:", len(X))

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X, y)

joblib.dump(model, "voice_model.pkl")
print("Model saved as voice_model.pkl")
