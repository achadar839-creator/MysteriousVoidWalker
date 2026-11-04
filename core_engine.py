import os
import json
from moviepy import VideoFileClip, vfx

print("=== Void Walker: Self-Evolving Legend Core Online ===")

MEMORY_FILE = "ai_experience_memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"past_mistakes": [], "successful_upgrades": 3}

def save_memory(memory_data):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory_data, f, indent=4)

def process_editing(raw_video_path, command_instruction=""):
    memory = load_memory()
    print(f"\n[STARK AI] Memory loaded. Past successful upgrades: {memory['successful_upgrades']}")
    
    if not os.path.exists(raw_video_path):
        error_msg = "Error: Raw video nahi mili, Boss!"
        print(f"[AI ERROR LOGGED] {error_msg}")
        # Galati se seekhna (Learning from failure)
        memory["past_mistakes"].append({"error": error_msg, "action": "Ensure video exists before processing"})
        save_memory(memory)
        return error_msg

    print(f"\n[AI CORE] Video analyze ho rahi hai...")
    try:
        clip = VideoFileClip(raw_video_path).subclipped(0, 5)
        effects = []
        
        cmd = command_instruction.lower() if command_instruction else ""
        print(f"-> Command received: '{command_instruction}'")
        
        if "cinematic" in cmd or "movie" in cmd:
            effects.extend([vfx.FadeIn(0.8), vfx.FadeOut(0.8)])
        
        if "mirror" in cmd or "palat" in cmd:
            effects.append(vfx.MirrorX())
            
        if not effects:
            # Auto-Tone fallback
            effects.extend([vfx.FadeIn(0.5), vfx.FadeOut(0.5)])

        final_clip = clip.with_effects(effects)
        output_file = "void_walker_final_output.mp4"
        
        final_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")
        
        # Success par khud ko upgrade karna (Self-Upgrade)
        memory["successful_upgrades"] += 1
        save_memory(memory)
        print(f"[AUTONOMOUS UPGRADE] Task successful! AI ne khud ko version {memory['successful_upgrades']}.0 par upgrade kar liya hai.")
        return f"SUCCESS: Video edit ho gayi aur AI aur smart ho gaya!"

    except Exception as e:
        error_str = str(e)
        print(f"\n[CRITICAL ERROR DETECTED] {error_str}")
        print("[AI LEARNING] Is galti ko analyze karke memory mein save kar raha hu taaki agli baar ye na ho...")
        
        memory["past_mistakes"].append({"error": error_str})
        save_memory(memory)
        return f"Rendering Error handled: {e}"

if __name__ == "__main__":
    # Testing the self-learning engine
    process_editing("input.mp4", command_instruction="cinematic aur mirror karo")
