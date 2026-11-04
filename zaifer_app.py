import os
import time
import threading
import requests
import yt_dlp
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, BooleanProperty
from kivy.core.window import Window
from kivy.clock import mainthread
try:
    from plyer import filechooser, stt
    HAS_PLYER = True
except ImportError:
    HAS_PLYER = False

Window.clearcolor = (0.06, 0.10, 0.14, 1)

API_KEY = "AIzaSyB_l4UUMWVTJiQArdGYN8WqwOdeCc01y2o"
TUTORIAL_VIDEO = "tutorial.mp4"

KV = """
<ChatBubble>:
    size_hint_y: None
    height: self.minimum_height
    padding: "10dp"
    
    BoxLayout:
        size_hint_x: 0.85
        pos_hint: {"right": 1} if root.is_user else {"x": 0}
        canvas.before:
            Color:
                rgba: (0, 0.6, 1, 0.15) if root.is_user else (1, 1, 1, 0.08)
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [20, 20, dp(2), 20] if root.is_user else [20, 20, 20, dp(2)]
            Color:
                rgba: (0, 0.8, 1, 0.4) if root.is_user else (1, 1, 1, 0.2)
            Line:
                rounded_rectangle: (self.x, self.y, self.width, self.height, 20, 20, 2 if root.is_user else 20, 20 if root.is_user else 2, 100)
                width: 1.2
                
        Label:
            text: root.text
            size_hint_y: None
            height: self.texture_size[1] + dp(20)
            text_size: self.width - dp(30), None
            halign: "left"
            valign: "middle"
            color: (1, 1, 1, 1)
            padding: ("15dp", "15dp")
            markup: True

BoxLayout:
    orientation: "vertical"
    
    BoxLayout:
        size_hint_y: None
        height: "65dp"
        canvas.before:
            Color:
                rgba: (1, 1, 1, 0.03)
            Rectangle:
                pos: self.pos
                size: self.size
            Color:
                rgba: (1, 1, 1, 0.1)
            Line:
                points: [self.x, self.y, self.right, self.y]
                width: 1
        Label:
            text: "✨ [b]ZAIFER AI[/b] ✨"
            markup: True
            font_size: "22sp"
            color: (0.4, 0.9, 1, 1)
            
    ScrollView:
        id: scroll_view
        do_scroll_x: False
        BoxLayout:
            id: chat_list
            orientation: "vertical"
            size_hint_y: None
            height: self.minimum_height
            padding: "15dp"
            spacing: "15dp"

    BoxLayout:
        size_hint_y: None
        height: "80dp"
        padding: "15dp"
        spacing: "15dp"
        canvas.before:
            Color:
                rgba: (0, 0, 0, 0.2)
            Rectangle:
                pos: self.pos
                size: self.size

        Button:
            text: "📁"
            size_hint_x: None
            width: "50dp"
            background_color: (0,0,0,0)
            on_release: app.pick_gallery_video()

        TextInput:
            id: user_input
            hint_text: "YouTube Shorts ka link dalein..."
            multiline: False
            background_color: (0, 0, 0, 0)
            foreground_color: (1, 1, 1, 1)
            hint_text_color: (1, 1, 1, 0.5)
            cursor_color: (0, 0.8, 1, 1)
            padding: ["20dp", "15dp"]
            canvas.before:
                Color:
                    rgba: (1, 1, 1, 0.05)
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [25]
                Color:
                    rgba: (1, 1, 1, 0.2)
                Line:
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 25)
                    width: 1.2

        Button:
            text: "🎙️"
            size_hint_x: None
            width: "50dp"
            background_color: (0,0,0,0)
            on_release: app.toggle_voice_record()

        Button:
            text: "SEND"
            size_hint_x: None
            width: "80dp"
            background_color: (0, 0, 0, 0)
            color: (1, 1, 1, 1)
            bold: True
            on_release: app.send_message()
            canvas.before:
                Color:
                    rgba: (0, 0.6, 1, 0.8)
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [25]
"""

class ChatBubble(BoxLayout):
    text = StringProperty("")
    is_user = BooleanProperty(False)

class ZaiferApp(App):

    selected_raw_video = StringProperty("")

    def pick_gallery_video(self):
        if HAS_PLYER:
            filechooser.open_file(on_selection=self.on_video_selected)
        else:
            self.add_msg("📁 Gallery Picker active: Select video.", is_user=False)

    
    def toggle_voice_record(self):
        if HAS_PLYER:
            try:
                stt.start()
                self.add_msg("🎙️ Sun raha hoon... Boliye!", is_user=False)
            except Exception as e:
                self.add_msg(f"Mic error: {str(e)}", is_user=False)
        else:
            self.add_msg("🎙️ Voice Engine active: Keyboard mic se bol kar type kar sakte hain.", is_user=False)

    def on_video_selected(self, selection):
        if selection:
            self.selected_raw_video = selection[0]
            self.add_msg(f"🎬 Video Selected: {selection[0]}", is_user=False)

    def build(self):
        return Builder.load_string(KV)
        
    def on_start(self):
        welcome_msg = "Mysterious Void Walker Engine Online.\nYouTube Shorts ka link paste karein, AI uske subtitles aur animations clone karega."
        self.add_msg(welcome_msg, is_user=False)

    def send_message(self):
        input_box = self.root.ids.user_input
        text = input_box.text.strip()
        if text:
            self.add_msg(text, is_user=True)
            input_box.text = ""
            if "youtube.com" in text or "youtu.be" in text:
                threading.Thread(target=self.process_video_ai, args=(text,), daemon=True).start()
            else:
                self.add_msg("[color=#ff6666]Kripya sahi YouTube/Shorts ka link paste karein.[/color]", is_user=False)

    @mainthread
    def add_msg(self, text, is_user):
        chat_list = self.root.ids.chat_list
        chat_list.add_widget(ChatBubble(text=text, is_user=is_user))
        self.root.ids.scroll_view.scroll_y = 0

    def download_video_native(self, link):
        ydl_opts = {
            "format": "best[ext=mp4]/best",
            "outtmpl": TUTORIAL_VIDEO,
            "quiet": True,
            "no_warnings": True
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

    def process_video_ai(self, link):
        self.add_msg("⏳ [color=#00ccff][1/4] Video download ho rahi hai...[/color]", is_user=False)
        if os.path.exists(TUTORIAL_VIDEO):
            os.remove(TUTORIAL_VIDEO)
        
        try:
            self.download_video_native(link)
        except Exception as e:
            self.add_msg(f"[color=#ff4444]❌ Download Error: {str(e)}[/color]", is_user=False)
            return

        if not os.path.exists(TUTORIAL_VIDEO):
            self.add_msg("[color=#ff4444]❌ Video download fail ho gayi.[/color]", is_user=False)
            return

        self.add_msg("⏳ [color=#00ccff][2/4] AI Engine me upload ho rahi hai...[/color]", is_user=False)
        upload_url = f"https://generativelanguage.googleapis.com/upload/v1beta/files?uploadType=media&key={API_KEY}"
        headers = {"Content-Type": "video/mp4"}
        
        try:
            with open(TUTORIAL_VIDEO, "rb") as f:
                upload_res = requests.post(upload_url, headers=headers, data=f.read())
            
            if upload_res.status_code != 200:
                self.add_msg(f"[color=#ff4444]Upload Error: {upload_res.status_code}[/color]", is_user=False)
                return
                
            file_info = upload_res.json()["file"]
            file_uri = file_info["uri"]
            file_name = file_info["name"]

            self.add_msg("⏳ [color=#00ccff][3/4] AI video ko analyze kar raha hai...[/color]", is_user=False)
            while True:
                check_url = f"https://generativelanguage.googleapis.com/v1beta/{file_name}?key={API_KEY}"
                check_res = requests.get(check_url)
                state = check_res.json().get("state", "")
                if state == "ACTIVE":
                    break
                elif state == "FAILED":
                    self.add_msg("[color=#ff4444]Video Analysis Failed.[/color]", is_user=False)
                    return
                time.sleep(4)

            self.add_msg("⏳ [color=#00ccff][4/4] Subtitle Animation & Code generate ho raha hai...[/color]", is_user=False)
            generate_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent?key={API_KEY}"
            prompt = "Tum ek expert Python Video Editor ho. Is video tutorial ko dekho. Isme subtitle ka jo EXACT font style, color, outline, aur animation (zoom/shake/pop) bataya gaya hai, usko huba-hu copy karne ke liye Python (MoviePy aur FFmpeg) ka code likho. Output short aur point to point python code me do."

            payload = {
                "contents": [{
                    "parts": [
                        {"text": prompt},
                        {"fileData": {"mimeType": "video/mp4", "fileUri": file_uri}}
                    ]
                }]
            }
            res = requests.post(generate_url, headers={"Content-Type": "application/json"}, json=payload)
            if res.status_code == 200:
                cloned_code = res.json()["candidates"][0]["content"]["parts"][0]["text"]
                self.add_msg(f"✅ [b][color=#00ff88]Cloned Effect Code:[/color][/b]\n\n{cloned_code[:800]}...", is_user=False)
            else:
                self.add_msg(f"[color=#ff4444]AI Error: {res.status_code}[/color]", is_user=False)

        except Exception as e:
            self.add_msg(f"[color=#ff4444]System Error: {str(e)}[/color]", is_user=False)
        finally:
            if os.path.exists(TUTORIAL_VIDEO):
                os.remove(TUTORIAL_VIDEO)

if __name__ == "__main__":
    ZaiferApp().run()
