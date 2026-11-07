import requests
import json

API_KEY = ""  # Cloud API key disabled
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"

print("Google के सर्वर से API Key चेक कर रहे हैं...\n")
res = requests.get(url)

try:
    data = res.json()
    if "error" in data:
        print("❌ Google ने एरर दिया:")
        print(json.dumps(data["error"], indent=2))
    else:
        print("✅ Key सही है! ये रहे मौजूद मॉडल्स:")
        for model in data.get("models", [])[:5]:
            print("-", model["name"])
except:
    print(res.text)
