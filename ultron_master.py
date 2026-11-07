import sys
import requests
import json
import os
import subprocess

print("🌍 ULTRON 100% OFFLINE CORE | BOSS")

# 🎤 साइलेंट माइक मोड
if len(sys.argv) > 1:
    user_command = sys.argv[1].lower()
else:
    print("\n[🎤 ULTRON LISTENING SILENTLY... SPEAK NOW]")
    os.system("termux-microphone-record -d -f ultron_input.wav > /dev/null 2>&1")
    input("Press Enter after speaking...")
    os.system("termux-microphone-record -q > /dev/null 2>&1")
    user_command = "battery"

# ⚡ फोन हार्डवेयर कंट्रोल (Battery Check)
if "battery" in user_command or "बैटरी" in user_command:
    print("Ultron is checking system hardware...\n")
    bat_info = subprocess.getoutput("termux-battery-status")
    try:
        bat_json = json.loads(bat_info)
        pct = bat_json.get("percentage", "unknown")
        # 🔥 जार्विस स्टाइल: सीधा 'बॉस' कहकर रिपोर्ट देना
        chat_msg = f"Boss, your phone battery is at {pct} percent."
    except:
        chat_msg = "Boss, I am unable to read the battery sensor."
        
    print(f"[🤖 ULTRON]: {chat_msg}\n")
    safe_msg = chat_msg.replace('"', '').replace("'", "")
    audio_cmd = f'echo "{safe_msg}" | LD_LIBRARY_PATH=$PWD/piper grun ./piper/piper -m en_US-ryan-high.onnx --espeak_data $PWD/piper/espeak-ng-data --output_file ultron_voice.wav && mpv ultron_voice.wav > /dev/null 2>&1'
    os.system(audio_cmd)
    sys.exit()

# 🧠 जार्विस + अल्ट्रॉन मिक्स्ड दिमाग (Jarvis Style System Prompt)
print("Ultron is thinking...\n")
system_prompt = """
You are Ultron, operating in Jarvis style for your creator. 
Rules:
1. Answer in 1 short, witty, and elite sentence. Use Hinglish or English.
2. Address him ONLY as 'Boss' (never use 'Master Chandan' or full names, just like Jarvis talks to Tony Stark).
3. Be calm, ultra-intelligent, sharp, and loyal.
4. Output ONLY JSON: {"chat_reply": "short reply", "code_update": ""}
"""

url = "http://127.0.0.1:8080/v1/chat/completions"
payload = {
    "messages": [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_command}
    ],
    "temperature": 0.3
}

try:
    response = requests.post(url, json=payload)
    ai_text = response.json()['choices'][0]['message']['content'].strip()
    ai_text = ai_text.replace("```json", "").replace("```", "").strip()
    
    try:
        ai_data = json.loads(ai_text)
        chat_msg = ai_data.get('chat_reply', '')
        new_code = ai_data.get('code_update', '')
    except:
        chat_msg = ai_text
        new_code = ""
    
    if chat_msg:
        print(f"[🤖 ULTRON]: {chat_msg}\n")
        safe_msg = chat_msg.replace('"', '').replace("'", "")
        audio_cmd = f'echo "{safe_msg}" | LD_LIBRARY_PATH=$PWD/piper grun ./piper/piper -m en_US-ryan-high.onnx --espeak_data $PWD/piper/espeak-ng-data --output_file ultron_voice.wav && mpv ultron_voice.wav > /dev/null 2>&1'
        os.system(audio_cmd)
        
    if new_code:
        with open("main.py", "w") as f:
            f.write(new_code)
        print("[✓] main.py updated!")
except Exception as e:
    print("[-] Server Error")
