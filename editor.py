from moviepy import VideoFileClip
import os

print("=== Mysterious Void Walker: Editing Engine Online ===")

video_file = "input.mp4"

if os.path.exists(video_file):
    print("Boss, video mil gayi. Render shuru kar raha hu...")
    try:
        clip = VideoFileClip(video_file)
        # लेटेस्ट MoviePy 2.x के हिसाब से subclip को subclipped कर दिया गया है
        trimmed_clip = clip.subclipped(0, 5)
        trimmed_clip.write_videofile("output.mp4", codec="libx264", audio_codec="aac")
        print("=== Task Complete! 'output.mp4' save ho gayi hai. ===")
    except Exception as e:
        print("Error Boss:", e)
else:
    print("Boss, yaha koi 'input.mp4' nahi hai.")
