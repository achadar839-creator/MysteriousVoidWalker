import os
import threading
import urllib.parse
import requests

VOICE_CACHE = "zaifer_voice.mp3"

class VoiceEngine:
    def __init__(self):
        self.is_speaking = False

    def speak(self, text):
        threading.Thread(target=self._generate_and_play, args=(text,), daemon=True).start()

    def _generate_and_play(self, text):
        if not text:
            return
        
        # Clean markdown tags
        clean_text = text.replace("[b]", "").replace("[/b]", "")
        clean_text = clean_text.replace("[color=#00ff88]", "").replace("[/color]", "")
        clean_text = clean_text.replace("✨", "").replace("🤖", "").replace("🎬", "").strip()
        
        if len(clean_text) > 150:
            clean_text = clean_text[:150]

        try:
            # 1. Fetch HD Neural Audio Stream
            encoded_text = urllib.parse.quote(clean_text)
            # HD Hindi Neural voice endpoint
            tts_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={encoded_text}&tl=hi&client=tw-ob"
            
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            }
            res = requests.get(tts_url, headers=headers, timeout=10)
            
            if res.status_code == 200:
                raw_audio = "temp_voice.mp3"
                with open(raw_audio, "wb") as f:
                    f.write(res.content)

                # 2. Apply 3D Spatial Reverb & HD Bass Filter (FFmpeg if available, else direct play)
                # aecho creates 3D depth, bass boost warms up the frequency
                out_audio = VOICE_CACHE
                cmd_3d = f'ffmpeg -y -i {raw_audio} -af "bass=g=5:f=110,aecho=0.8:0.88:40:0.4" {out_audio} > /dev/null 2>&1'
                ret = os.system(cmd_3d)
                
                play_target = out_audio if (ret == 0 and os.path.exists(out_audio)) else raw_audio

                # 3. Native Android Audio Playback
                # Plays via Termux audio or Android system player
                os.system(f"mpv --no-video {play_target} > /dev/null 2>&1 || play-audio {play_target} > /dev/null 2>&1")
                
                # Cleanup
                if os.path.exists(raw_audio):
                    os.remove(raw_audio)
        except Exception:
            pass

voice = VoiceEngine()

def speak_zaifer(text):
    voice.speak(text)
