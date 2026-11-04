with open("zaifer_app.py", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Import god_engine
if "from god_core import god_engine" not in text:
    text = "from god_core import god_engine\n" + text

# 2. Add On-Demand God Core Triggers in process_general_chat
god_router = """
        # God-Tier On-Demand Triggers
        if any(w in q_lower for w in ["zero prompt", "khud video bana", "auto video", "reel bana", "शॉर्ट बना"]):
            self.add_msg("⚡ [God Mode] Aapke aadesh par complete viral video script & render plan taiyar ho raha hai...", is_user=False)
            blueprint = god_engine.create_on_demand_video(user_query, log_callback=lambda m: self.add_msg(m, is_user=False))
            self.add_msg(f"🎬 [color=#00ff88]Master Video Blueprint Ready:[/color]\\n{blueprint[:400]}...", is_user=False)
            return

        if any(w in q_lower for w in ["avatar", "clone", "humshakal", "अवतार", "क्लोन"]):
            self.add_msg("👤 [Digital Clone] Digital persona profile load ho rahi hai...", is_user=False)
            res = god_engine.generate_avatar_speech(user_query)
            self.add_msg(f"✅ Digital Persona Synced: {res['persona']} with audio filter [{res['filter']}]", is_user=False)
            return

        if any(w in q_lower for w in ["pc connect", "ghost", "bridge", "कंप्यूटर", "पीसी"]):
            msg = god_engine.start_cross_device_bridge(port=8888, log_callback=lambda m: self.add_msg(m, is_user=False))
            self.add_msg(f"🌐 [Ghost Node] {msg}", is_user=False)
            return
"""

if "god_engine.create_on_demand_video" not in text:
    target_str = "    def process_general_chat(self, user_query):\n        q_lower = user_query.lower()"
    text = text.replace(target_str, target_str + god_router)

with open("zaifer_app.py", "w", encoding="utf-8") as f:
    f.write(text)

print("God Core triggers cleanly injected into ZaiferApp!")
