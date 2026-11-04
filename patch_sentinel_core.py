with open("zaifer_app.py", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Import sentinel_engine
if "from sentinel_core import sentinel_engine" not in text:
    text = "from sentinel_core import sentinel_engine\n" + text

# 2. Add Sentinel Triggers in process_general_chat
sentinel_router = """
        # Sentinel Core Camera Director & Security Triggers
        if any(w in q_lower for w in ["camera", "director", "framing", "लाइट", "शूट"]):
            self.add_msg("🎥 [Live Director] Framing & lighting matrix scan ho rahi hai...", is_user=False)
            advice = sentinel_engine.analyze_live_frame_conditions()
            self.add_msg(f"🎬 [Director Cue]: {advice}", is_user=False)
            return

        if any(w in q_lower for w in ["physics", "gravity", "kinetic", "बाउंस"]):
            f_code = sentinel_engine.generate_kinetic_physics_filter()
            self.add_msg(f"🪐 [3D Physics Matrix] Kinetic expression injected: [{f_code}]", is_user=False)
            return
"""

if "sentinel_engine.analyze_live_frame_conditions" not in text:
    target_str = "    def process_general_chat(self, user_query):\n        q_lower = user_query.lower()"
    text = text.replace(target_str, target_str + sentinel_router)

with open("zaifer_app.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Sentinel Core successfully bound into ZaiferApp!")
