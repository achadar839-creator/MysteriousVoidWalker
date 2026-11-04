import os
import json
import threading
import requests
import socket

API_KEY = "AIzaSyB_l4UUMWVTJiQArdGYN8WqwOdeCc01y2o"
CLONE_PROFILE_FILE = "digital_clone_profile.json"

class GodCore:
    def __init__(self):
        self.clone_data = self.load_clone_data()
        self.server_running = False

    def load_clone_data(self):
        if os.path.exists(CLONE_PROFILE_FILE):
            try:
                with open(CLONE_PROFILE_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {
            "persona_name": "The Commander",
            "voice_pitch": "deep_cinematic",
            "talking_speed": 1.1,
            "facial_vectors": "calibrated"
        }

    # 1. On-Demand Zero-Prompt Creator (Sirf User Command par)
    def create_on_demand_video(self, optional_niche="viral tech and sci-fi", log_callback=print):
        log_callback(f"🎬 [Zero-Prompt Engine] '{optional_niche}' par autonomous script & concept taiyar ho raha hai...")
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent?key={API_KEY}"
        prompt = f"""
Tum Zaifer AI ke God-Tier Creator ho.
Niche: "{optional_niche}".
User ne ek command di hai. Ek high-retention 30-second YouTube Short ka complete blueprint do:
1. HOOK (0-3 sec): High dopamine punchline
2. CORE STORY (3-25 sec): Rapid fire facts / thrilling insight
3. OUTRO & CTA (25-30 sec)
4. Exact FFmpeg audio & visual layering cues (B-Roll, SFX, Subtitle Glow)

Format: Pure ready-to-render structured screenplay in Hinglish.
"""
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        try:
            res = requests.post(url, headers={"Content-Type": "application/json"}, json=payload, timeout=25)
            if res.status_code == 200:
                script = res.json()['candidates'][0]['content']['parts'][0]['text'].strip()
                log_callback("⚡ [Video Blueprint Ready] Script, SFX aur B-Roll cues generate ho gaye!")
                return script
            return "Video generation connect nahi ho saki."
        except Exception as e:
            return f"Generation Error: {str(e)}"

    # 2. Digital Persona & Neural Voice Mimic
    def generate_avatar_speech(self, text_to_speak, log_callback=print):
        log_callback(f"👤 [Digital Avatar] '{text_to_speak[:40]}...' ko user ke persona me synthesize kiya ja raha hai...")
        p = self.clone_data
        # FFmpeg filter profile matching calibrated persona vectors
        filter_spec = f"atempo={p['talking_speed']},bass=g=6:f=100,treble=g=3:f=3000"
        return {
            "status": "ready",
            "text": text_to_speak,
            "filter": filter_spec,
            "persona": p["persona_name"]
        }

    # 3. Cross-Device Ghost Node (On-Demand WebSocket / TCP Bridge)
    def start_cross_device_bridge(self, port=8888, log_callback=print):
        if self.server_running:
            return f"Ghost Node pehle se live hai port {port} par!"

        def run_server():
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.bind(("0.0.0.0", port))
                s.listen(1)
                self.server_running = True
                log_callback(f"🌐 [Ghost Bridge] PC Terminal link open ho gaya! Port: {port}")
                while self.server_running:
                    conn, addr = s.accept()
                    data = conn.recv(1024).decode("utf-8")
                    if data:
                        conn.send(b"ZAIFER_NODE_ACK: Command received on mobile device\n")
                    conn.close()
            except Exception:
                self.server_running = False

        threading.Thread(target=run_server, daemon=True).start()
        return f"🚀 Ghost Bridge active! PC se phone ko connect karein IP par on port {port}."

god_engine = GodCore()
