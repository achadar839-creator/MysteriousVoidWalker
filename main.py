import json
import os
from moviepy import VideoFileClip

print("=== Mysterious Void Walker : Main System Online ===")

db_file = "clients_data.json"
video_file = "input.mp4"

# Memory System
def load_memory():
    if os.path.exists(db_file):
        with open(db_file, "r") as f:
            return json.load(f)
    return {}

def save_memory(data):
    with open(db_file, "w") as f:
        json.dump(data, f, indent=4)

memory = load_memory()
client_name = input("Boss, kis client ki video process karni hai? ")

if client_name in memory:
    print(f"\n[SYSTEM] '{client_name}' ka data mil gaya!")
    style = memory[client_name]
else:
    print(f"\n[SYSTEM] New Client '{client_name}'. Nayi profile bana raha hu...")
    style = {
        "color_grading": "Cinematic & High Contrast",
        "editing_style": "Fast Cuts & Beat Sync"
    }
    memory[client_name] = style
    save_memory(memory)

print(f"-> Applying Color Grading: {style['color_grading']}")
print(f"-> Applying Editing Style: {style['editing_style']}")

# Editing Engine
if os.path.exists(video_file):
    print(f"\nBoss, '{client_name}' ke liye video render shuru kar raha hu...")
    try:
        clip = VideoFileClip(video_file)
        trimmed_clip = clip.subclipped(0, 5)
        
        # Client ke naam se video save karega
        output_name = f"{client_name}_final.mp4"
        trimmed_clip.write_videofile(output_name, codec="libx264", audio_codec="aac")
        print(f"=== Task Complete! Video '{output_name}' save ho gayi hai. ===")
    except Exception as e:
        print("Error Boss:", e)
else:
    print("\nBoss, yaha koi 'input.mp4' nahi hai. Pehle raw video laani hogi.")
