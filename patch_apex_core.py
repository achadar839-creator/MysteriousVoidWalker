with open("zaifer_app.py", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Import apex_engine
if "from apex_core import apex_engine" not in text:
    text = "from apex_core import apex_engine\n" + text

# 2. Add Apex Triggers
apex_router = """
        # Apex Core Hardware, Harvester & DNA Vault Triggers
        if any(w in q_lower for w in ["boost", "hardware", "speed up", "गरम", "तेज"]):
            msg = apex_engine.optimize_device_hardware()
            self.add_msg(f"⚡ [Apex Hardware] {msg}", is_user=False)
            return

        if any(w in q_lower for w in ["harvest", "deep intel", "रिसर्च", "सीक्रेट", "जानकारी"]):
            self.add_msg("🕷️ [Deep Harvester] Worldwide intelligence harvest ho rahi hai...", is_user=False)
            report = apex_engine.harvest_web_intelligence(user_query)
            self.add_msg(f"📑 [Deep Intelligence Report]:\\n{report[:450]}...", is_user=False)
            return

        if any(w in q_lower for w in ["dna", "backup", "immortal", "सुरक्षित", "बैकअप"]):
            all_cores = [
                "zaifer_app.py", "apex_core.py", "nexus_core.py", "sentinel_core.py", 
                "sovereign_core.py", "shadow_core.py", "god_core.py", "alien_core.py", 
                "pro_editor_engine.py", "jarvis_core.py", "autonomous_core.py", "voice_engine.py"
            ]
            res = apex_engine.create_dna_backup(all_cores)
            self.add_msg(f"🧬 [Apex Singularity] {res}", is_user=False)
            return
"""

if "apex_engine.optimize_device_hardware" not in text:
    target_str = "    def process_general_chat(self, user_query):\n        q_lower = user_query.lower()"
    text = text.replace(target_str, target_str + apex_router)

with open("zaifer_app.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Apex Core successfully crowned into ZaiferApp!")
