import requests
import json

print("=== Void Walker: AI Brain (Gemini REST API) Online ===")

# Aapki API Key
API_KEY = "AIzaSyB_l4UUMWVTJiQArdGYN8WqwOdeCc01y2o"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

def create_effect_code(tutorial_description):
    print("\n[AI Brain] Tutorial samajh raha hoon... Auto-coding start...")
    prompt = f"""
    Tum ek expert Python Video Editor ho. MoviePy aur FFmpeg ka use karke is effect ke liye Python code likho:
    
    TUTORIAL/EFFECT: {tutorial_description}
    
    Sirf aur sirf Python code output karo, koi extra explanation nahi. Code aisa hona chahiye jo 'input.mp4' aur 'audio.wav.srt' ki timings ka use karke effect apply kare aur 'final_output.mp4' banaye.
    """
    
    headers = {'Content-Type': 'application/json'}
    data = {"contents": [{"parts":[{"text": prompt}]}]}
    
    try:
        response = requests.post(URL, headers=headers, json=data)
        if response.status_code == 200:
            result = response.json()
            text = result['candidates'][0]['content']['parts'][0]['text']
            print("[SUCCESS] Master Effect Code Generate ho gaya!")
            return text
        else:
            print(f"[ERROR] API Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"[ERROR] Internet ya API connect nahi ho paya: {e}")
        return None

if __name__ == "__main__":
    print("[READY] System ka 'Dimag' activate ho chuka hai!")
