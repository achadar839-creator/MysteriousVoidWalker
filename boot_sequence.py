import threading
import time
import sys
import os

print("\n🚀 [SYSTEM BOOT] 14-Titan Architecture Initialization Started...\n")

try:
    # 1. Importing All Core Engines
    print("⏳ Loading Core Engines...")
    from kinetic_mesh_core import kinetic_mesh_engine
    from god_core import god_engine
    from jarvis_core import jarvis
    from autonomous_core import AutonomousCore
    from phantom_core import phantom_engine
    from nexus_core import nexus_engine
    from voice_engine import voice
    print("✅ All Core Engines Loaded to RAM.")

    # 2. Activating Background Services (Sensors, Servers, Mesh)
    print("⏳ Activating Background Protocols...")
    
    # स्टार्ट मेश नेटवर्क (बिना इंटरनेट कम्युनिकेशन)
    mesh_status = kinetic_mesh_engine.start_mesh_beacon(log_callback=print)
    print(f"📡 {mesh_status}")

    # स्टार्ट घोस्ट ब्रिज (PC से कनेक्ट करने के लिए)
    bridge_status = god_engine.start_cross_device_bridge(port=8888, log_callback=print)
    print(f"🌐 {bridge_status}")

    # ऑटोनॉमस ब्रेन लोड करना
    brain = AutonomousCore()
    print("🧠 Autonomous Brain & Memory Matrix Synced.")

    time.sleep(1)
    
    # 3. Launching the Main User Interface (Zaifer App)
    print("\n✨ All background systems active. Launching GUI Subsystem...\n")
    from zaifer_app import ZaiferApp
    ZaiferApp().run()

except Exception as e:
    print(f"\n❌ [CRITICAL BOOT FAILURE]: {e}")
    sys.exit()
