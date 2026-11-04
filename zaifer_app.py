from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, BooleanProperty
from kivy.core.window import Window

# Dark Cinematic Background (ChatGPT / Gemini Dark Mode Mix)
Window.clearcolor = (0.06, 0.10, 0.14, 1)

KV = '''
<ChatBubble>:
    size_hint_y: None
    height: self.minimum_height
    padding: "10dp"
    
    BoxLayout:
        # User ka bubble right mein, Bot ka left mein
        size_hint_x: 0.85
        pos_hint: {'right': 1} if root.is_user else {'x': 0}
        canvas.before:
            # Liquid Glass Background Colors
            Color:
                rgba: (0, 0.6, 1, 0.15) if root.is_user else (1, 1, 1, 0.08)
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [20, 20, 2dp, 20] if root.is_user else [20, 20, 20, 2dp]
            # Glowing Glass Borders
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
            halign: 'left'
            valign: 'middle'
            color: (1, 1, 1, 1)
            padding: ("15dp", "15dp")
            markup: True

BoxLayout:
    orientation: 'vertical'
    
    # 1. Header (Zaifer)
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
            
    # 2. Chat Area
    ScrollView:
        id: scroll_view
        do_scroll_x: False
        BoxLayout:
            id: chat_list
            orientation: 'vertical'
            size_hint_y: None
            height: self.minimum_height
            padding: "15dp"
            spacing: "15dp"

    # 3. Input Area (Bottom)
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

        TextInput:
            id: user_input
            hint_text: "Video link ya command dein..."
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
            text: "SEND"
            size_hint_x: None
            width: "80dp"
            background_color: (0,0,0,0)
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
'''

class ChatBubble(BoxLayout):
    text = StringProperty("")
    is_user = BooleanProperty(False)

class ZaiferApp(App):
    def build(self):
        return Builder.load_string(KV)
        
    def on_start(self):
        # Startup Message
        welcome_msg = "Hello Chandan! Main Zaifer hoon.\nMujhe YouTube Shorts/Reels ka link do, main uska Subtitle Style aur Animation copy karke Master Code bana dunga."
        self.add_msg(welcome_msg, is_user=False)

    def send_message(self):
        input_box = self.root.ids.user_input
        text = input_box.text.strip()
        if text:
            # User ka message print karo
            self.add_msg(text, is_user=True)
            input_box.text = ""
            
            # AI (Bot) ka temporary response (Baad me yaha learner.py judega)
            self.add_msg("[color=#00ccff]⏳ Process kar raha hoon... Gemini Vision Engine active...[/color]", is_user=False)

    def add_msg(self, text, is_user):
        chat_list = self.root.ids.chat_list
        chat_list.add_widget(ChatBubble(text=text, is_user=is_user))
        # Auto scroll to bottom
        self.root.ids.scroll_view.scroll_y = 0

if __name__ == "__main__":
    ZaiferApp().run()
