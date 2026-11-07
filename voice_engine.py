import os
import threading
import urllib.parse
import subprocess
import requests

from kivy.utils import platform

VOICE_CACHE = "zaifer_voice.mp3"


class VoiceEngine:
    def __init__(self):
        self.is_speaking = False
        self.lock = threading.Lock()

    def _clean_text(self, text):
        clean_text = str(text or "")

        tags = [
            "[b]", "[/b]",
            "[color=#00ccff]", "[/color]",
            "[color=#ff6666]",
            "[color=#00ff88]",
            "[color=#ff4444]"
        ]

        for tag in tags:
            clean_text = clean_text.replace(tag, "")

        for emoji in ["✨", "🤖", "🎬", "🚨", "⚙️", "✅", "❌"]:
            clean_text = clean_text.replace(emoji, "")

        return clean_text.strip()[:150]

    def speak(self, text):
        clean_text = self._clean_text(text)

        if not clean_text:
            return

        if platform == "android":
            try:
                from plyer import tts
                tts.speak(clean_text)
            except Exception as error:
                print("Android TTS error:", error)
            return

        threading.Thread(
            target=self._generate_and_play,
            args=(clean_text,),
            daemon=True
        ).start()

    def _generate_and_play(self, clean_text):
        with self.lock:
            raw_audio = "temp_voice.mp3"

            try:
                encoded = urllib.parse.quote(clean_text)

                url = (
                    "https://translate.google.com/translate_tts"
                    f"?ie=UTF-8&q={encoded}&tl=en&client=tw-ob"
                )

                response = requests.get(
                    url,
                    headers={"User-Agent": "Mozilla/5.0"},
                    timeout=10
                )
                response.raise_for_status()

                with open(raw_audio, "wb") as audio_file:
                    audio_file.write(response.content)

                result = subprocess.run(
                    [
                        "ffmpeg", "-y",
                        "-i", raw_audio,
                        "-af",
                        "asetrate=44100*0.78,atempo=1.15,"
                        "bass=g=12:f=70,aecho=0.8:0.88:70:0.4",
                        VOICE_CACHE
                    ],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )

                target = (
                    VOICE_CACHE
                    if result.returncode == 0
                    and os.path.exists(VOICE_CACHE)
                    else raw_audio
                )

                player = subprocess.run(
                    ["mpv", "--no-video", target],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )

                if player.returncode != 0:
                    subprocess.run(
                        ["play-audio", target],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL
                    )

            except Exception as error:
                print("Voice engine error:", error)

            finally:
                for path in (raw_audio, VOICE_CACHE):
                    if os.path.exists(path):
                        try:
                            os.remove(path)
                        except OSError:
                            pass

    def process_incoming_voice_command(self, recognized_text):
        normalized = recognized_text.lower()

        if "अल्ट्रॉन अपडेट" in normalized or "सिस्टम अपडेट" in normalized:
            message = (
                "Update command detected. "
                "Approval is required before changing project files."
            )
            self.speak(message)

            return {
                "status": "approval_required",
                "message": message
            }

        return {
            "status": "recognized",
            "message": recognized_text
        }


voice = VoiceEngine()


def speak_zaifer(text):
    voice.speak(text)
