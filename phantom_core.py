import os
import json
import base64
import datetime

PHANTOM_MEMORY_VAULT = {}
REVERT_KEY = "VOID_RESURRECT_777"

class PhantomCore:
    def __init__(self):
        self.is_vanished = False

    # 1. Zero-Emission Ghost Protocol (Memory Vanish & Reconstruct)
    def trigger_ghost_vanish(self, target_files, log_callback=print):
        global PHANTOM_MEMORY_VAULT
        log_callback("⚠️ [Ghost Protocol] Compressing core files into encrypted RAM memory...")
        for fpath in target_files:
            if os.path.exists(fpath):
                try:
                    with open(fpath, "rb") as f:
                        data = f.read()
                        PHANTOM_MEMORY_VAULT[fpath] = base64.b64encode(data).decode('utf-8')
                    # Wipe file securely from disk
                    with open(fpath, "wb") as f:
                        f.write(b"")
                    os.remove(fpath)
                except Exception as e:
                    log_callback(f"Vanish file err: {str(e)}")
        
        self.is_vanished = True
        log_callback("👻 [System Invisible] Core disk footprint erased. Running purely inside volatile RAM!")
        return "GHOST_VANISH_COMPLETE"

    def resurrect_from_memory(self, input_key, log_callback=print):
        global PHANTOM_MEMORY_VAULT
        if input_key != REVERT_KEY:
            return "❌ Access Denied: Unauthorized resurrection key."
        
        log_callback("🧬 [Resurrection Matrix] Re-materializing core files onto physical storage...")
        restored_count = 0
        for fpath, b64_data in PHANTOM_MEMORY_VAULT.items():
            try:
                raw_bytes = base64.b64decode(b64_data)
                with open(fpath, "wb") as f:
                    f.write(raw_bytes)
                restored_count += 1
            except Exception as e:
                log_callback(f"Restore err: {str(e)}")
        
        self.is_vanished = False
        PHANTOM_MEMORY_VAULT.clear()
        return f"⚡ Resurrection Successful! {restored_count} Titan engines brought back to physical reality."

    # 2. Solar & Cosmic Rhythm Engine
    def calculate_cosmic_state(self):
        hour = datetime.datetime.now().hour
        if 6 <= hour < 12:
            return {
                "phase": "DAWN_SURGE",
                "ui_theme": {"bg": [0.03, 0.08, 0.05, 1], "neon": [0, 1, 0.53, 1]},
                "voice_speed": 1.15,
                "temperament": "Aggressive execution & high morning dopamine."
            }
        elif 12 <= hour < 17:
            return {
                "phase": "SOLAR_ZENITH",
                "ui_theme": {"bg": [0.02, 0.05, 0.09, 1], "neon": [0, 0.9, 1, 1]},
                "voice_speed": 1.1,
                "temperament": "Peak tactical productivity & hardware overclock."
            }
        elif 17 <= hour < 21:
            return {
                "phase": "TWILIGHT_HORIZON",
                "ui_theme": {"bg": [0.08, 0.03, 0.07, 1], "neon": [1, 0, 0.33, 1]},
                "voice_speed": 1.0,
                "temperament": "Review, reverse-engineering & syndicate alignment."
            }
        else:
            return {
                "phase": "VOID_MIDNIGHT",
                "ui_theme": {"bg": [0.01, 0.01, 0.02, 1], "neon": [1, 0.45, 0, 1]},
                "voice_speed": 0.95,
                "temperament": "Subconscious whispering, deep long-term planning & low-light sanctuary."
            }

    # 3. Dead-Drop Steganography (Hide & Extract Payload in Images)
    def inject_payload_into_image(self, source_image, secret_data_text, output_image="stealth_drop.jpg"):
        if not os.path.exists(source_image):
            return f"Source image '{source_image}' not found."
        
        # Binary EOF payload injection technique (Stealth preserved across basic decoders)
        with open(source_image, "rb") as f:
            raw_img = f.read()
        
        encoded_secret = base64.b64encode(secret_data_text.encode('utf-8'))
        carrier_marker = b"<<<ZAIFER_VOID_CARRIER>>>"
        
        with open(output_image, "wb") as f:
            f.write(raw_img + carrier_marker + encoded_secret)
            
        return f"🔒 Steganography complete! Secret data deeply woven into '{output_image}'."

    def extract_payload_from_image(self, target_image):
        if not os.path.exists(target_image):
            return "Image not found."
        
        with open(target_image, "rb") as f:
            content = f.read()
        
        carrier_marker = b"<<<ZAIFER_VOID_CARRIER>>>"
        if carrier_marker in content:
            parts = content.split(carrier_marker)
            extracted = base64.b64decode(parts[-1]).decode('utf-8', errors='ignore')
            return f"🔓 Decrypted Payload Found:\\n{extracted}"
        return "⚠️ No stealth data detected inside this image."

phantom_engine = PhantomCore()
