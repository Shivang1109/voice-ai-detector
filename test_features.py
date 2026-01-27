from features import extract_features

f = extract_features("sample.wav")
print("Feature vector length:", len(f))
print(f)
