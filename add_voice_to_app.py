with open("zaifer_app.py", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Voice Engine Import जोड़ना
if "from voice_engine import speak_zaifer" not in text:
    text = "from voice_engine import speak_zaifer\n" + text

# 2. add_msg में ऑटो-वॉयस रिप्लाई जोड़ना (सिर्फ AI के मैसेजेस के लिए)
if "speak_zaifer" not in text.split("def add_msg")[1]:
    old_add_msg = """    def add_msg(self, text, is_user):
        chat_list = self.root.ids.chat_list
        chat_list.add_widget(ChatBubble(text=text, is_user=is_user))
        self.root.ids.scroll_view.scroll_y = 0"""

    new_add_msg = """    def add_msg(self, text, is_user):
        chat_list = self.root.ids.chat_list
        chat_list.add_widget(ChatBubble(text=text, is_user=is_user))
        self.root.ids.scroll_view.scroll_y = 0
        if not is_user:
            speak_zaifer(text)"""

    text = text.replace(old_add_msg, new_add_msg)

with open("zaifer_app.py", "w", encoding="utf-8") as f:
    f.write(text)

print("3D HD Voice successfully linked to Zaifer UI!")
