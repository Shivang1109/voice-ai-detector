from features import extract_features

f = extract_features("sample.mp3")
print("Feature vector length:", len(f))
print(f)
