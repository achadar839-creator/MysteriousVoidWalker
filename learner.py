import requests
import json
import os
import time

print("=== Void Walker: Learner Module (Latest Engine) Online ===")

API_KEY = "AIzaSyB_l4UUMWVTJiQArdGYN8WqwOdeCc01y2o"
TUTORIAL_VIDEO = "tutorial.mp4"

video_link = input("\n👉 YouTube ya Shorts ka link paste karein: ")

if os.path.exists(TUTORIAL_VIDEO):
    os.remove(TUTORIAL_VIDEO)

print("\n[0] Link se video download ho rahi hai... Wait kijiye...")
os.system(f'yt-dlp -f "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]/best" -o "{TUTORIAL_VIDEO}" "{video_link}" --quiet --no-warnings')

if not os.path.exists(TUTORIAL_VIDEO):
    print(f"\n[ERROR] Video download nahi ho payi. Link check karein.")
    exit()

print("\n[1] Video aa gayi! Ab Gemini ke dimag mein upload ho rahi hai...")
upload_url = f"https://generativelanguage.googleapis.com/upload/v1beta/files?uploadType=media&key={API_KEY}"
headers = {"Content-Type": "video/mp4"}

with open(TUTORIAL_VIDEO, "rb") as f:
    upload_res = requests.post(upload_url, headers=headers, data=f.read())

if upload_res.status_code == 200:
    file_info = upload_res.json()["file"]
    file_uri = file_info["uri"]
    file_name = file_info["name"]
    print(f"[SUCCESS] Video upload ho gayi. (URI: {file_uri})")
    
    print("\n[2] Video processing ho rahi hai...")
    while True:
        check_url = f"https://generativelanguage.googleapis.com/v1beta/{file_name}?key={API_KEY}"
        check_res = requests.get(check_url)
        state = check_res.json().get("state", "")
        if state == "ACTIVE":
            print("[SUCCESS] AI ne video dekh li hai!")
            break
        elif state == "FAILED":
            print("[ERROR] Video processing fail ho gayi.")
            exit()
        time.sleep(5)
else:
    print(f"[ERROR] Upload fail: {upload_res.text}")
    exit()

# Google ka bataya hua sabse latest 2026 Engine
best_model = "models/gemini-3.1-pro-preview"
print(f"\n[3] Model Lock ho gaya: {best_model}")

print("\n[4] Exact style, font aur animation copy kiya ja raha hai...")
generate_url = f"https://generativelanguage.googleapis.com/v1beta/{best_model}:generateContent?key={API_KEY}"
prompt = "Tum ek expert Python Video Editor ho. Is video tutorial ko dekho. Isme subtitle ka jo EXACT font style, color, outline, aur animation (zoom/shake/pop) bataya gaya hai, usko huba-hu copy karne ke liye Python (MoviePy aur FFmpeg) ka code likho. Koi extra formatting nahi, sirf python code output karo jo 'input.mp4' aur 'audio.wav.srt' ki timings par ye exact effect apply kare aur 'final_output.mp4' banaye."

payload = {
    "contents": [{
        "parts": [
            {"text": prompt},
            {"fileData": {"mimeType": "video/mp4", "fileUri": file_uri}}
        ]
    }]
}
headers = {'Content-Type': 'application/json'}

try:
    response = requests.post(generate_url, headers=headers, json=payload)
    if response.status_code == 200:
        result = response.json()
        cloned_code = result['candidates'][0]['content']['parts'][0]['text']
        print("\n[SUCCESS] HOO-BA-HOO CODE GENERATE HO GAYA:\n")
        print(cloned_code)
    else:
        print(f"[ERROR] API Error: {response.text}")
except Exception as e:
    print(f"[ERROR] Connection fail: {e}")
