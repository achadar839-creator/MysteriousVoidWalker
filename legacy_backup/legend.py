import os
from moviepy import VideoFileClip, vfx

print("=== Void Walker: LEGEND CORE Online ===")
video_file = "input.mp4"

if not os.path.exists(video_file):
    print("Boss, yaha 'input.mp4' nahi mili. Pehle video laiye.")
    exit()

clip = VideoFileClip(video_file).subclipped(0, 5)

print("\nBoss, is video ka kya karna hai?")
print("(Hint: Type karein 'cinematic banao', 'mirror kar do', ya 'dono lagao')")
command = input("Aapka Order: ").lower()

effects = []

# AI Keyword pakad raha hai
if "cinematic" in command:
    print("-> [AI] Cinematic Fade In/Out add kar raha hu...")
    effects.extend([vfx.FadeIn(1.0), vfx.FadeOut(1.0)])

if "mirror" in command or "palat" in command or "ulta" in command:
    print("-> [AI] MirrorX effect add kar raha hu (Inception Style)...")
    effects.append(vfx.MirrorX())

if effects:
    print("\n[SYSTEM] Legend Mode Activated! Multi-effects combine ho rahe hain...")
    final_clip = clip.with_effects(effects)
else:
    print("\n[SYSTEM] Normal render kar raha hu...")
    final_clip = clip

output_name = "legend_output.mp4"
print(f"\n-> Rendering started for '{output_name}'...")
try:
    final_clip.write_videofile(output_name, codec="libx264", audio_codec="aac")
    print(f"\n=== BOOM! '{output_name}' ekdam Legend style mein save ho gayi! ===")
except Exception as e:
    print("Error Boss:", e)
