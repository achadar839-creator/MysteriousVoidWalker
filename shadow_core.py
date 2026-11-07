import os
import json
import requests

API_KEY = ""  # Cloud API key disabled
SUBCONSCIOUS_VAULT = "zaifer_subconscious.json"

class ShadowCore:
    def __init__(self):
        self.vault = self.load_vault()

    def load_vault(self):
        if os.path.exists(SUBCONSCIOUS_VAULT):
            try:
                with open(SUBCONSCIOUS_VAULT, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {
            "creator_temperament": "aggressive_viral_cinematic",
            "signature_color_palette": ["#00ff88", "#00e5ff", "#ff0055"],
            "hook_pacing_bias": 1.25,
            "dissected_competitors": []
        }

    def save_vault(self):
        with open(SUBCONSCIOUS_VAULT, "w", encoding="utf-8") as f:
            json.dump(self.vault, f, indent=4)

    # 1. Competitor Video Reverse-Engineering Engine
    def reverse_engineer_competitor(self, video_concept_or_transcript, log_callback=print):
        log_callback("🕵️‍♂️ [Opponent Destroyer] Viral structure dissect ho rahi hai...")
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent?key={API_KEY}"
        prompt = f"""
Tum Zaifer AI ke Master Reverse-Engineering Strategist ho.
Competitor Content/Flow: "{video_concept_or_transcript}"

Is competitor ki puri strategy ko dismantle karo:
1. THE RETENTION TRAP: inhone audience ko kaise baandh kar rakha?
2. THE WEAKNESS: is video me kahan pacing slow hui ya kya kami chhut gayi?
3. THE OVERKILL REMIX: Ek aisi timeline aur script blueprint do jo is video ko 100% outclass aur dominate kar de.

Format: Extreme tactical breakdown in Hinglish.
"""
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        try:
            res = requests.post(url, headers={"Content-Type": "application/json"}, json=payload, timeout=25)
            if res.status_code == 200:
                breakdown = res.json()['candidates'][0]['content']['parts'][0]['text'].strip()
                self.vault["dissected_competitors"].append({"summary": video_concept_or_transcript[:60], "status": "dismantled"})
                self.save_vault()
                return breakdown
            return "Competitor breakdown connect nahi ho paya."
        except Exception as e:
            return f"Deconstruction Error: {str(e)}"

    # 2. Subconscious Habit & Style Adapter
    def record_creator_insight(self, preference_note):
        self.vault["creator_temperament"] += f" | {preference_note}"
        self.save_vault()
        return f"🧠 Subconscious memory locked: '{preference_note}'"

shadow_engine = ShadowCore()
