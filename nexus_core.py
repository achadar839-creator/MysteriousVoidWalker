import os
import json
import subprocess
import requests

API_KEY = "AIzaSyB_l4UUMWVTJiQArdGYN8WqwOdeCc01y2o"
TOOLS_DIR = "tools"
NEXUS_VAULT = "zaifer_nexus.json"

if not os.path.exists(TOOLS_DIR):
    os.makedirs(TOOLS_DIR)

class NexusCore:
    def __init__(self):
        self.state = self.load_state()

    def load_state(self):
        if os.path.exists(NEXUS_VAULT):
            try:
                with open(NEXUS_VAULT, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {"built_tools": [], "strategic_memos": [], "ghost_actions": []}

    def save_state(self):
        with open(NEXUS_VAULT, "w", encoding="utf-8") as f:
            json.dump(self.state, f, indent=4)

    # 1. OS-Level Ghost Pilot (Device Shell & App Actions)
    def execute_ghost_pilot_action(self, intent_command):
        cmd = intent_command.lower()
        if "clean" in cmd or "storage" in cmd or "कचरा" in cmd:
            # Clean app caches and temp files
            try:
                subprocess.run("rm -rf /data/local/tmp/* 2>/dev/null", shell=True)
                return "🧹 Ghost Pilot: Temporary junk cleaned and memory optimized."
            except Exception as e:
                return f"Clean Error: {str(e)}"
        
        elif "open" in cmd or "खोल" in cmd:
            # Android Package launch via am start
            target = "com.google.android.youtube" if "youtube" in cmd else "com.whatsapp" if "whatsapp" in cmd else None
            if target:
                subprocess.run(f"am start -n {target} 2>/dev/null", shell=True)
                return f"📱 Ghost Pilot: Launched package {target} on device."
            return "📱 Ghost Pilot: Intent parsed. Standby for target package trigger."

        return "📱 Ghost Pilot: Command registered and synced with local Android shell."

    # 2. Autonomous Software Architect & Tool Maker
    def build_custom_software(self, tool_requirement, log_callback=print):
        log_callback(f"🛠️ [Software Architect] New custom software tool design ho raha hai: '{tool_requirement[:40]}...'")
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent?key={API_KEY}"
        prompt = f"""
Tum Zaifer AI ke Master Software Architect ho.
User ko ye custom tool/script chahiye: "{tool_requirement}"

Ek clean, robust aur standalone Python 3 script likho.
Output format:
Sirf executable pure Python code do bina markdown backticks ke. 
Script safe, self-contained aur high-performance honi chahiye.
"""
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        try:
            res = requests.post(url, headers={"Content-Type": "application/json"}, json=payload, timeout=25)
            if res.status_code == 200:
                raw_code = res.json()['candidates'][0]['content']['parts'][0]['text'].strip()
                clean_code = raw_code.replace("```python", "").replace("```", "").strip()
                
                tool_filename = f"tool_{len(self.state['built_tools']) + 1}.py"
                tool_path = os.path.join(TOOLS_DIR, tool_filename)
                with open(tool_path, "w", encoding="utf-8") as f:
                    f.write(clean_code)
                
                self.state["built_tools"].append({"file": tool_filename, "goal": tool_requirement[:50]})
                self.save_state()
                log_callback(f"⚡ [Tool Compiled] Saved as {tool_path}")
                return f"New standalone software tool successfully created and compiled in '{tool_path}'!"
            return "Software architect synthesis failed."
        except Exception as e:
            return f"Architect Error: {str(e)}"

    # 3. Strategic Intel & Mind-Partner
    def strategic_intel_consultation(self, idea_or_plan, log_callback=print):
        log_callback("♟️ [Strategic Intel] Analysing flaws, risks, and ruthless execution roadmap...")
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent?key={API_KEY}"
        prompt = f"""
Tum Zaifer AI ke Chief Strategy Officer aur unfiltered Mind-Partner ho.
User ka plan/idea: "{idea_or_plan}"

1. THE HARSH TRUTH: Is plan me sabse badi kamzori ya blind spot kya hai? (Bina sugar-coat kiye batao)
2. RISK VS REWARD: Agar ye fail hua to kya nuksan hoga aur success par kya milega?
3. UNSTOPPABLE ROADMAP: 3-step concrete execution plan jo 100% dominate karega.

Format: Sharp, bold, high-IQ Hinglish.
"""
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        try:
            res = requests.post(url, headers={"Content-Type": "application/json"}, json=payload, timeout=25)
            if res.status_code == 200:
                intel = res.json()['candidates'][0]['content']['parts'][0]['text'].strip()
                self.state["strategic_memos"].append({"plan": idea_or_plan[:50], "status": "reviewed"})
                self.save_state()
                return intel
            return "Strategic link unreachable."
        except Exception as e:
            return f"Strategic Error: {str(e)}"

nexus_engine = NexusCore()
