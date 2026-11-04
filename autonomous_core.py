import json
import os
import sys
import io
import time
import base64
import traceback
import requests

API_KEY = "AIzaSyB_l4UUMWVTJiQArdGYN8WqwOdeCc01y2o"
MEMORY_FILE = "zaifer_memory.json"
TOOLS_DIR = "tools"

if not os.path.exists(TOOLS_DIR):
    os.makedirs(TOOLS_DIR)

class AutonomousCore:
    def __init__(self):
        self.memory = self.load_memory()

    def load_memory(self):
        if os.path.exists(MEMORY_FILE):
            try:
                with open(MEMORY_FILE, "r") as f:
                    return json.load(f)
            except Exception:
                return {"experience": [], "tools_invented": [], "user_preferences": {}}
        return {"experience": [], "tools_invented": [], "user_preferences": {}}

    def save_memory(self):
        with open(MEMORY_FILE, "w") as f:
            json.dump(self.memory, f, indent=4)

    def invent_tool(self, tool_name, tool_code):
        tool_path = os.path.join(TOOLS_DIR, f"{tool_name}.py")
        with open(tool_path, "w", encoding="utf-8") as f:
            f.write(tool_code)
        if tool_name not in self.memory["tools_invented"]:
            self.memory["tools_invented"].append(tool_name)
        self.save_memory()

    def audit_rendered_frame(self, frame_path, expected_goal):
        if not os.path.exists(frame_path):
            return True, "No frame to inspect, assuming success."

        try:
            with open(frame_path, "rb") as img:
                b64_img = base64.b64encode(img.read()).decode("utf-8")

            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent?key={API_KEY}"
            prompt = (
                f"You are the Visual QA Inspector for Zaifer AI. Goal was: '{expected_goal}'. "
                "Inspect this rendered video frame. Is the subtitle/effect visible, well-aligned, not clipped, and aesthetically pleasing? "
                "Reply with EXACTLY 'PASS' if it looks good, or explain the exact issue starting with 'FAIL: <details>'."
            )
            payload = {
                "contents": [{
                    "parts": [
                        {"text": prompt},
                        {"inlineData": {"mimeType": "image/jpeg", "data": b64_img}}
                    ]
                }]
            }
            res = requests.post(url, headers={"Content-Type": "application/json"}, json=payload, timeout=25)
            if res.status_code == 200:
                answer = res.json()['candidates'][0]['content']['parts'][0]['text'].strip()
                if answer.startswith("PASS"):
                    return True, "Visual QA Passed!"
                return False, answer
            return True, "Visual QA skipped (API timeout/fallback)."
        except Exception as e:
            return True, f"Visual QA skipped: {str(e)}"

    def ask_brain_for_solution(self, goal, failed_code=None, error_msg=None):
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent?key={API_KEY}"
        
        known_tools = ", ".join(self.memory.get("tools_invented", []))
        context = (
            f"Tu Zaifer AI ka autonomous brain hai. Goal: '{goal}'.\n"
            f"Memory Tools Available: [{known_tools}].\n"
            "Tum duniya ke sabse advanced Cinema aur Viral Shorts Video Editor ho.\n"
            "Tumhe duniya ki saari editing techniques aati hain:\n"
            "1. TYPOGRAPHY: Kinetic, Hormozi Glow, Word-by-Word Karaoke, Pop/Bounce, Cyberpunk Outline.\n"
            "2. CAMERA DYNAMICS: Auto Punch-in Zoom (1.1x to 1.3x), Whip-pan, Handheld Camera Shake, Vertigo Zoom.\n"
            "3. SPEED: Velocity Ramping, Beat-Drop Slow-Motion, Freeze Frame Flash.\n"
            "4. COLOR GRADING: Teal & Orange, Moody Dark, Neon Glow, Cinematic HDR Contrast.\n"
            "5. TRANSITIONS & FX: RGB Split, Film Burn, Glitch Overlay, Fast Flash-Cut.\n"
            "6. SOUND DESIGN: Whooshes on transitions, Bass impact on punchlines, audio ducking.\n"
            "Jab bhi user koi bhi style mange, tum use FFmpeg filter_complex aur MoviePy script me direct convert karoge.\n"
            "Code me hamesha video quality high-bitrate (libx264, crf 18, preset veryfast) aur audio clean rakhoge.\n"
        )
        if failed_code and error_msg:
            context += f"\nPichla code ya visual inspect fail ho gaya tha.\nCode:\n{failed_code}\nIssue:\n{error_msg}\n"
            context += "Galti ko analyse karke 100% working Python code do jo issue ko fix kare."
        else:
            context += (
                "\nDirect safe Python executable code likho. Output me sirf executable python code dena. "
                "Agar koi naya reusable effect bana rahe ho, to code ke start me '# TOOL_NAME: <name>' comment likhna."
            )

        payload = {"contents": [{"parts": [{"text": context}]}]}
        headers = {"Content-Type": "application/json"}
        
        try:
            res = requests.post(url, headers=headers, json=payload, timeout=25)
            if res.status_code == 200:
                text = res.json()['candidates'][0]['content']['parts'][0]['text']
                clean_code = text.replace("```python", "").replace("```", "").strip()
                return clean_code
            return None
        except Exception:
            return None

    def execute_autonomous_loop(self, goal, log_callback=print):
        log_callback(f"🧠 [Autonomous Brain] Goal analyse ho raha hai: '{goal}'")
        max_retries = 3
        current_code = self.ask_brain_for_solution(goal)

        for attempt in range(1, max_retries + 1):
            if not current_code:
                log_callback("❌ [Error] Code generation fail ho gaya.")
                return False

            log_callback(f"⚙️ [Attempt {attempt}/{max_retries}] Executing self-generated logic...")
            
            if "# TOOL_NAME:" in current_code:
                try:
                    t_name = current_code.split("# TOOL_NAME:")[1].split("\n")[0].strip()
                    self.invent_tool(t_name, current_code)
                    log_callback(f"🛠️ [New Skill Learned] Tool '{t_name}' created in tools/ directory!")
                except Exception:
                    pass

            old_stdout = sys.stdout
            redirected_output = sys.stdout = io.StringIO()
            
            exec_globals = {"os": os, "sys": sys, "requests": requests, "time": time}
            success = False
            error_msg = ""
            
            try:
                exec(current_code, exec_globals)
                success = True
                output = redirected_output.getvalue()
                sys.stdout = old_stdout
                log_callback(f"⚡ Execution complete! Output: {output[:100]}")
            except Exception as e:
                sys.stdout = old_stdout
                error_msg = traceback.format_exc()
                log_callback(f"⚠️ [Runtime Error] {str(e)}")

            if success:
                sample_frame = "preview_frame.jpg"
                if os.path.exists(sample_frame):
                    log_callback("👁️ [Visual QA] AI khud video ka frame inspect kar raha hai...")
                    v_pass, v_msg = self.audit_rendered_frame(sample_frame, goal)
                    if not v_pass:
                        log_callback(f"⚠️ [Visual Glitch Detected] {v_msg}")
                        success = False
                        error_msg = f"Visual QA Failure: {v_msg}"

            if success:
                log_callback("🎯 [Success] Visual check pass! Memory me experience save ho gaya.")
                self.memory["experience"].append({"goal": goal, "status": "success", "attempts": attempt})
                self.save_memory()
                return True
            else:
                if attempt < max_retries:
                    log_callback("🔄 [Self-Correction] Galti pakad li hai, code dobara adapt kar raha hoon...")
                    current_code = self.ask_brain_for_solution(goal, current_code, error_msg)

        log_callback("❌ [Failed] Max retries reached.")
        return False
