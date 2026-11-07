import os

print("=== Void Walker: Subtitle Engine Online ===")

video_file = "input.mp4"
audio_file = "audio.wav"

if not os.path.exists(video_file):
    print("Boss, yaha 'input.mp4' nahi hai. Test ke liye ek choti video yaha rakh dijiye.")
    exit()

print("\n[1] Video se Audio extract ho raha hai...")
os.system(f"ffmpeg -i {video_file} -ar 16000 -ac 1 -c:a pcm_s16le {audio_file} -y -loglevel quiet")

print("\n[2] Whisper AI (Base) timings nikal raha hai. Wait kijiye...")
os.system(f"./whisper.cpp/main -m whisper.cpp/models/ggml-base.bin -f {audio_file} -osrt -ml 1 > /dev/null 2>&1")

srt_file = f"{audio_file}.srt"

if os.path.exists(srt_file):
    print("\n[SUCCESS] Exact timings nikal aayi! SRT file ban gayi hai.\n")
    print("--- Timing Demo ---")
    os.system(f"head -n 12 {srt_file}")
    print("-------------------")
else:
    print("\n[ERROR] Timing nahi nikal payi, kuch gadbad hai.")
