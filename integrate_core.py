with open("zaifer_app.py", "r", encoding="utf-8") as f:
    text = f.read()

# 1. AutonomousCore import जोड़ना
if "from autonomous_core import AutonomousCore" not in text:
    text = "from autonomous_core import AutonomousCore\n" + text

# 2. ZaiferApp में कोर का ऑब्जेक्ट इनिशियलाइज़ करना
if "self.auto_core = AutonomousCore()" not in text:
    text = text.replace(
        "class ZaiferApp(App):",
        "class ZaiferApp(App):\n    auto_core = None"
    )
    text = text.replace(
        "def on_start(self):",
        "def on_start(self):\n        self.auto_core = AutonomousCore()"
    )

# 3. process_user_raw_edit को पूरी तरह ऑटोनॉमस लूप से बदलना
old_process = """    def process_user_raw_edit(self, instruction):
        self.add_msg(f"⏳ [color=#00ccff]Editor Brain thinking... Instruction: \\"{instruction}\\"[/color]", is_user=False)
        time.sleep(2)
        self.add_msg(f"✅ [color=#00ff88]Effect Applied to {os.path.basename(self.selected_raw_video)}! Render pipeline ready.[/color]", is_user=False)"""

new_process = """    def process_user_raw_edit(self, instruction):
        video_name = os.path.basename(self.selected_raw_video)
        goal = f"Video: {video_name}, Path: {self.selected_raw_video}. Task: {instruction}"
        
        def log_to_ui(msg):
            self.add_msg(f"[color=#00ffff]{msg}[/color]", is_user=False)

        log_to_ui(f"🤖 [Zaifer Brain] Autonomous execution triggered for: {video_name}")
        success = self.auto_core.execute_autonomous_loop(goal, log_callback=log_to_ui)
        
        if success:
            self.add_msg("✨ [b][color=#00ff88]Goal achieved autonomously & saved to memory![/color][/b]", is_user=False)
        else:
            self.add_msg("⚠️ [color=#ff6666]Autonomous resolution attempted but needs new input.[/color]", is_user=False)"""

if old_process in text:
    text = text.replace(old_process, new_process)

with open("zaifer_app.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Autonomous Core successfully integrated into ZaiferApp!")
