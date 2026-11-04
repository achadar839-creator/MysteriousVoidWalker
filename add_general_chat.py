with open("zaifer_app.py", "r", encoding="utf-8") as f:
    text = f.read()

# General chat logic function
chat_func = """
    def process_general_chat(self, user_query):
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent?key={API_KEY}"
        system_prompt = "Tum Zaifer AI ho - ek autonomous smart personal editor aur loyal AI assistant. User ke har sawal ka seedha, to the point aur behtareen jawab Hinglish/Hindi me do."
        payload = {
            "contents": [
                {"role": "user", "parts": [{"text": f"{system_prompt}\\n\\nUser: {user_query}"}]}
            ]
        }
        try:
            res = requests.post(url, headers={"Content-Type": "application/json"}, json=payload, timeout=15)
            if res.status_code == 200:
                reply = res.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
                self.add_msg(reply, is_user=False)
            else:
                self.add_msg("Dimag me thoda network issue aa gaya, dobara boliye.", is_user=False)
        except Exception as e:
            self.add_msg(f"Chat Error: {str(e)}", is_user=False)
"""

if "def process_general_chat" not in text:
    text = text.replace("def process_user_raw_edit(self, instruction):", chat_func + "\n    def process_user_raw_edit(self, instruction):")

# Else block ko replace karna
old_else = """            else:
                self.add_msg("Mujhe YouTube link dijiye ya 📁 se apni raw video select karke instruction dijiye.", is_user=False)"""

new_else = """            else:
                threading.Thread(target=self.process_general_chat, args=(text,), daemon=True).start()"""

if old_else in text:
    text = text.replace(old_else, new_else)

with open("zaifer_app.py", "w", encoding="utf-8") as f:
    f.write(text)

print("General conversation capability unlocked!")
