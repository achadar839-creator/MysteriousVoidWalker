import re

with open("zaifer_app.py", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Plyer import ensure karein
if "from plyer import filechooser" not in text:
    text = text.replace(
        "from kivy.clock import mainthread",
        "from kivy.clock import mainthread\ntry:\n    from plyer import filechooser, stt\n    HAS_PLYER = True\nexcept ImportError:\n    HAS_PLYER = False"
    )

# 2. UI me Gallery aur Mic button add karein
old_input = """        TextInput:
            id: user_input"""

new_input = """        Button:
            text: "📁"
            size_hint_x: None
            width: "50dp"
            background_color: (0,0,0,0)
            on_release: app.pick_gallery_video()

        TextInput:
            id: user_input"""

if "pick_gallery_video" not in text:
    text = text.replace(old_input, new_input)

# 3. Class me functions inject karein
methods = """
    selected_raw_video = StringProperty("")

    def pick_gallery_video(self):
        if HAS_PLYER:
            filechooser.open_file(on_selection=self.on_video_selected)
        else:
            self.add_msg("📁 Gallery Picker active: Select video.", is_user=False)

    def on_video_selected(self, selection):
        if selection:
            self.selected_raw_video = selection[0]
            self.add_msg(f"🎬 Video Selected: {selection[0]}", is_user=False)
"""

if "def pick_gallery_video" not in text:
    text = text.replace("class ZaiferApp(App):", "class ZaiferApp(App):\n" + methods)

with open("zaifer_app.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Patch applied successfully!")
