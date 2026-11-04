with open("zaifer_app.py", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Import phantom_engine
if "from phantom_core import phantom_engine" not in text:
    text = "from phantom_core import phantom_engine\n" + text

# 2. Add Phantom Triggers
phantom_router = """
        # Phantom Core Steganography, Solar Rhythm & Vanish Triggers
        if any(w in q_lower for w in ["vanish", "गायब", "invisible", "छुपा"]):
            self.add_msg("👻 [Ghost Protocol] Erasing disk traces into encrypted RAM...", is_user=False)
            res = phantom_engine.trigger_ghost_vanish(["zaifer_dna.vault", "zaifer_subconscious.json"], log_callback=lambda m: self.add_msg(m, is_user=False))
            self.add_msg(f"🛡️ {res}", is_user=False)
            return

        if "resurrect" in q_lower or "जिंदा कर" in q_lower:
            key = user_query.split()[-1]
            status = phantom_engine.resurrect_from_memory(key, log_callback=lambda m: self.add_msg(m, is_user=False))
            self.add_msg(f"🧬 {status}", is_user=False)
            return

        if any(w in q_lower for w in ["solar", "cosmic", "सूरज", "समय"]):
            state = phantom_engine.calculate_cosmic_state()
            self.add_msg(f"🌌 [Cosmic Rhythm] Current Phase: {state['phase']}\\nTemperament: {state['temperament']}", is_user=False)
            return

        if any(w in q_lower for w in ["stego", "hide in image", "फोटो में छुपा"]):
            res = phantom_engine.inject_payload_into_image("test_sample.jpg", user_query)
            self.add_msg(f"🖼️ [Stealth Carrier] {res}", is_user=False)
            return
"""

if "phantom_engine.trigger_ghost_vanish" not in text:
    target_str = "    def process_general_chat(self, user_query):\n        q_lower = user_query.lower()"
    text = text.replace(target_str, target_str + phantom_router)

with open("zaifer_app.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Phantom Core successfully infused into ZaiferApp!")
