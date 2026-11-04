with open("zaifer_app.py", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Import kinetic_mesh_engine
if "from kinetic_mesh_core import kinetic_mesh_engine" not in text:
    text = "from kinetic_mesh_core import kinetic_mesh_engine\n" + text

# 2. Add Kinetic Mesh Triggers in process_general_chat
kinetic_router = """
        # Kinetic Mesh & Hardware Telemetry Triggers
        if any(w in q_lower for w in ["mesh", "offgrid", "bina net", "बिना इंटरनेट", "मेश"]):
            self.add_msg("📡 [Off-Grid Mesh] Initializing local RF broadcast beacon...", is_user=False)
            res = kinetic_mesh_engine.start_mesh_beacon(log_callback=lambda m: self.add_msg(m, is_user=False))
            self.add_msg(f"📶 {res}", is_user=False)
            return

        if any(w in q_lower for w in ["motor", "relay", "machine", "हार्डवेयर", "चालू कर", "बंद कर"]):
            self.add_msg("🔌 [Hardware Telemetry] Machine relay dispatch ho raha hai...", is_user=False)
            status = kinetic_mesh_engine.trigger_hardware_relay(target_ip="192.168.1.50", action="TRIGGER")
            self.add_msg(f"⚡ {status}", is_user=False)
            return

        if any(w in q_lower for w in ["sentry", "chaukanna", "listen", "आवाज़", "माहौल", "पहरेदार"]):
            res = kinetic_mesh_engine.start_ambient_sound_sentry(alert_callback=lambda m: self.add_msg(m, is_user=False))
            self.add_msg(f"🛡️ {res}", is_user=False)
            return
"""

if "kinetic_mesh_engine.start_mesh_beacon" not in text:
    target_str = "    def process_general_chat(self, user_query):\n        q_lower = user_query.lower()"
    text = text.replace(target_str, target_str + kinetic_router)

with open("zaifer_app.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Kinetic Mesh Core successfully injected into ZaiferApp!")
