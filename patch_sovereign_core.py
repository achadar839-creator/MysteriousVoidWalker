with open("zaifer_app.py", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Import sovereign_engine
if "from sovereign_core import sovereign_engine" not in text:
    text = "from sovereign_core import sovereign_engine\n" + text

# 2. Add Sovereign Triggers in process_general_chat
sovereign_router = """
        # Sovereign Core Syndicate & Subliminal Triggers
        if any(w in q_lower for w in ["syndicate", "multiplatform", "4 video", "variation", "साम्राज्य"]):
            self.add_msg("🔱 [Sovereign Syndicate] 4-Platform content empire generate ho raha hai...", is_user=False)
            empire = sovereign_engine.multiply_into_syndicate(user_query, log_callback=lambda m: self.add_msg(m, is_user=False))
            self.add_msg(f"👑 [color=#ff0055]Syndicate Matrix Blueprint:[/color]\\n{empire[:450]}...", is_user=False)
            return

        if any(w in q_lower for w in ["neuro sonic", "frequency", "hypnotic", "वेव"]):
            filt = sovereign_engine.get_neuro_audio_filter()
            self.add_msg(f"🌊 [Neuro-Sonic Lock] Retention wave generator locked: [{filt}]", is_user=False)
            return
"""

if "sovereign_engine.multiply_into_syndicate" not in text:
    target_str = "    def process_general_chat(self, user_query):\n        q_lower = user_query.lower()"
    text = text.replace(target_str, target_str + sovereign_router)

with open("zaifer_app.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Sovereign Core successfully integrated into ZaiferApp!")
