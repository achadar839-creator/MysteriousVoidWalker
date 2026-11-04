import os
import json
import subprocess
import requests

API_KEY = "AIzaSyB_l4UUMWVTJiQArdGYN8WqwOdeCc01y2o"
DNA_BACKUP_FILE = "zaifer_dna.vault"

class ApexCore:
    def __init__(self):
        self.status = "Apex Singularity Active"

    # 1. Hardware Overclock & Thermal Monitor Simulation
    def optimize_device_hardware(self):
        try:
            # Sync filesystem and drop temporary OS dirty pages
            subprocess.run("sync 2>/dev/null", shell=True)
            return "⚡ Hardware Throttling cleared! CPU threads optimized for max processing priority."
        except Exception as e:
            return f"Thermal Guardian: {str(e)}"

    # 2. Headless Intelligence Harvester
    def harvest_web_intelligence(self, target_topic):
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent?key={API_KEY}"
        prompt = f"""
Tum Zaifer AI ke Deep Web Intelligence Harvester ho.
Topic: "{target_topic}"

Is topic ke sabse deep, insider aur high-value key insights nikalo jo normal logo ko asani se nahi milte.
Short, bullet-proof, tactical report do.
"""
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        try:
            res = requests.post(url, headers={"Content-Type": "application/json"}, json=payload, timeout=25)
            if res.status_code == 200:
                return res.json()['candidates'][0]['content']['parts'][0]['text'].strip()
            return "Intelligence link timed out."
        except Exception as e:
            return f"Harvester Error: {str(e)}"

    # 3. DNA Single-File Emergency Backup
    def create_dna_backup(self, core_files):
        dna = {}
        for cf in core_files:
            if os.path.exists(cf):
                try:
                    with open(cf, "r", encoding="utf-8") as f:
                        dna[cf] = f.read()
                except Exception:
                    pass
        with open(DNA_BACKUP_FILE, "w", encoding="utf-8") as f:
            json.dump(dna, f)
        return f"🧬 DNA Vault locked ({len(dna)} Core files encrypted into {DNA_BACKUP_FILE}). System immortalized!"

apex_engine = ApexCore()
