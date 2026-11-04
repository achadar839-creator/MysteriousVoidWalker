import json
import os

print("=== Mysterious Void Walker : Memory System Online ===")

db_file = "clients_data.json"

def load_memory():
    if os.path.exists(db_file):
        with open(db_file, "r") as f:
            return json.load(f)
    return {}

def save_memory(data):
    with open(db_file, "w") as f:
        json.dump(data, f, indent=4)

memory = load_memory()

print("Boss, kis client ki video process karni hai?")
client_name = input("Client Name: ")

if client_name in memory:
    print(f"\n[SYSTEM] Boss, mujhe yaad hai! '{client_name}' ka data load kar raha hu...")
    style = memory[client_name]
    print(f"-> Color Grading: {style['color_grading']}")
    print(f"-> Editing Style: {style['editing_style']}")
    print("Isi style mein video render karunga.\n")
else:
    print(f"\n[SYSTEM] New Client Detected: '{client_name}'. Nayi profile bana raha hu...")
    memory[client_name] = {
        "color_grading": "Cinematic & High Contrast",
        "editing_style": "Fast Cuts & Beat Sync"
    }
    save_memory(memory)
    print(f"Profile Save ho gayi Boss! Agli baar se main '{client_name}' ka style khud yaad rakhunga.\n")
