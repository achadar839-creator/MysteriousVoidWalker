with open("zaifer_app.py", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Import shadow_engine
if "from shadow_core import shadow_engine" not in text:
    text = "from shadow_core import shadow_engine\n" + text

# 2. Add Shadow Triggers
shadow_router = """
        # Shadow Core Opponent Destroyer & Subconscious Triggers
        if any(w in q_lower for w in ["roast", "competitor", "dismantle", "nakal", "rival", "उड़ा दे", "तोड़"]):
            self.add_msg("🕵️‍♂️ [Opponent Destroyer] Competitor video blueprint reverse-engineer ho raha hai...", is_user=False)
            analysis = shadow_engine.reverse_engineer_competitor(user_query, log_callback=lambda m: self.add_msg(m, is_user=False))
            self.add_msg(f"💥 [color=#00e5ff]Competitor Deconstruction Blueprint:[/color]\\n{analysis[:450]}...", is_user=False)
            return

        if any(w in q_lower for w in ["yaad rakh", "mera style", "memory lock", "पसंद"]):
            reply = shadow_engine.record_creator_insight(user_query)
            self.add_msg(f"🧬 [Subconscious Vault] {reply}", is_user=False)
            return
"""

if "shadow_engine.reverse_engineer_competitor" not in text:
    target_str = "    def process_general_chat(self, user_query):\n        q_lower = user_query.lower()"
    text = text.replace(target_str, target_str + shadow_router)

with open("zaifer_app.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Shadow Core successfully integrated into ZaiferApp!")
