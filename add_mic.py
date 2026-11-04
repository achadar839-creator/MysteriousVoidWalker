with open("zaifer_app.py", "r", encoding="utf-8") as f:
    text = f.read()

# 1. UI me SEND button se pehle Mic button inject karna
target_ui = """        Button:
            text: "SEND" """

new_mic_ui = """        Button:
            text: "🎙️"
            size_hint_x: None
            width: "50dp"
            background_color: (0,0,0,0)
            on_release: app.toggle_voice_record()

        Button:
            text: "SEND" """

if "toggle_voice_record" not in text:
    # Text-based replacement for SEND button area
    if 'text: "SEND"' in text:
        text = text.replace(
            '        Button:\n            text: "SEND"',
            '        Button:\n            text: "🎙️"\n            size_hint_x: None\n            width: "50dp"\n            background_color: (0,0,0,0)\n            on_release: app.toggle_voice_record()\n\n        Button:\n            text: "SEND"'
        )

# 2. ZaiferApp class me toggle_voice_record method inject karna
mic_method = """
    def toggle_voice_record(self):
        if HAS_PLYER:
            try:
                stt.start()
                self.add_msg("🎙️ Sun raha hoon... Boliye!", is_user=False)
            except Exception as e:
                self.add_msg(f"Mic error: {str(e)}", is_user=False)
        else:
            self.add_msg("🎙️ Voice Engine active: Keyboard mic se bol kar type kar sakte hain.", is_user=False)
"""

if "def toggle_voice_record" not in text:
    text = text.replace("def on_video_selected(self, selection):", mic_method + "\n    def on_video_selected(self, selection):")

with open("zaifer_app.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Mic patch applied cleanly!")
