with open("zaifer_app.py", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Import nexus_engine
if "from nexus_core import nexus_engine" not in text:
    text = "from nexus_core import nexus_engine\n" + text

# 2. Add Nexus Core Triggers in process_general_chat
nexus_router = """
        # Nexus Core Ghost Pilot, Software Architect & Strategic Intel
        if any(w in q_lower for w in ["phone", "clean", "launch", "open", "कचरा", "चला", "खोल"]):
            res = nexus_engine.execute_ghost_pilot_action(user_query)
            self.add_msg(f"📱 [Ghost Pilot] {res}", is_user=False)
            return

        if any(w in q_lower for w in ["tool bana", "software bana", "script bana", "टूल", "सॉफ्टवेयर"]):
            self.add_msg("🛠️ [Software Architect] New standalone software code likha aur compile ho raha hai...", is_user=False)
            res = nexus_engine.build_custom_software(user_query, log_callback=lambda m: self.add_msg(m, is_user=False))
            self.add_msg(f"⚡ [Architect Result] {res}", is_user=False)
            return

        if any(w in q_lower for w in ["strategy", "plan", "review", "soch", "रणनीति", "प्लान"]):
            self.add_msg("♟️ [Strategic Intel] Unfiltered risk & domination blueprint taiyar ho raha hai...", is_user=False)
            intel = nexus_engine.strategic_intel_consultation(user_query, log_callback=lambda m: self.add_msg(m, is_user=False))
            self.add_msg(f"🧠 [color=#00e5ff]Strategic Intel Breakdown:[/color]\\n{intel[:450]}...", is_user=False)
            return
"""

if "nexus_engine.execute_ghost_pilot_action" not in text:
    target_str = "    def process_general_chat(self, user_query):\n        q_lower = user_query.lower()"
    text = text.replace(target_str, target_str + nexus_router)

with open("zaifer_app.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Nexus Core successfully wired into ZaiferApp!")
