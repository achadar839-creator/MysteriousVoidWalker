import os
import json
import requests
import urllib.parse

API_KEY = "AIzaSyB_l4UUMWVTJiQArdGYN8WqwOdeCc01y2o"
JARVIS_MEMORY_FILE = "jarvis_data.json"

class JarvisCore:
    def __init__(self):
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(JARVIS_MEMORY_FILE):
            try:
                with open(JARVIS_MEMORY_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {"tasks": [], "scheduled_videos": [], "lore_notes": []}

    def save_data(self):
        with open(JARVIS_MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)

    # 1. सोशल मीडिया ऑटोपायलट (Metadata & Viral Hooks)
    def generate_social_autopilot(self, video_summary_or_script):
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent?key={API_KEY}"
        prompt = f"""
Tum Zaifer AI ke Social Media Director ho.
Topic/Script: "{video_summary_or_script}"

Is video ke liye generate karo:
1. 3 High-CTR Viral Titles (Shorts/Reels ke liye best)
2. 1 Compelling SEO Description (with Call to Action)
3. Top 15 Trending Hashtags/Tags
4. 1 Thumbnail Concept & Recommended Freeze-Frame visual

Format bilkul clean aur Hinglish me do.
"""
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        try:
            res = requests.post(url, headers={"Content-Type": "application/json"}, json=payload, timeout=20)
            if res.status_code == 200:
                return res.json()['candidates'][0]['content']['parts'][0]['text'].strip()
            return "Autopilot metadata generate karne me dikkat aayi."
        except Exception as e:
            return f"Autopilot Error: {str(e)}"

    # 2. लाइव वेब व ट्रेंड रिसर्च (Live Web / Trends)
    def live_trend_research(self, query):
        try:
            # DuckDuckGo Instant Answer / Live Query
            clean_q = urllib.parse.quote(query)
            ddg_url = f"https://api.duckduckgo.com/?q={clean_q}&format=json&no_html=1&skip_disambig=1"
            res = requests.get(ddg_url, timeout=10).json()
            abstract = res.get("AbstractText", "")
            
            # Gemini Synthesis
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent?key={API_KEY}"
            prompt = f"""
User query: "{query}"
Web Context: "{abstract}"

Zaifer AI ban kar live trends, viral topics ya facts ka to-the-point analysis do. Short, sharp aur actionable insight do.
"""
            payload = {"contents": [{"parts": [{"text": prompt}]}]}
            ai_res = requests.post(url, headers={"Content-Type": "application/json"}, json=payload, timeout=20)
            if ai_res.status_code == 200:
                return ai_res.json()['candidates'][0]['content']['parts'][0]['text'].strip()
            return "Live research connect nahi ho payi."
        except Exception as e:
            return f"Research Error: {str(e)}"

    # 3. सिस्टम व प्रोजेक्ट ऑटोमेशन (Task & Scheduling)
    def add_schedule_task(self, task_desc):
        self.data["tasks"].append(task_desc)
        self.save_data()
        return f"📌 Task note ho gaya: '{task_desc}'. Total pending tasks: {len(self.data['tasks'])}"

    def get_pending_tasks(self):
        if not self.data["tasks"]:
            return "Koi pending task ya schedule nahi hai, sab clear hai!"
        out = "📋 [Pending Schedules/Tasks]:\n"
        for i, t in enumerate(self.data["tasks"], 1):
            out += f"{i}. {t}\n"
        return out.strip()

jarvis = JarvisCore()
