with open("zaifer_app.py", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Import pro_editor
if "from pro_editor_engine import pro_editor" not in text:
    text = "from pro_editor_engine import pro_editor\n" + text

# 2. Inject Pro-Editing rules into process_user_raw_edit
smart_router = """        q_lower = instruction.lower()
        if any(w in q_lower for w in ["cut", "silent", "dead air", "pause", "सन्नाटा", "कट"]):
            log_to_ui("⚡ [Smart Cut] Silence & dead-air detect karke trim kiya ja raha hai...")
            ok, res_vid = pro_editor.remove_dead_air(self.selected_raw_video)
            if ok:
                self.add_msg(f"✅ [color=#00ff88]Dead air removed! Processed video: {os.path.basename(res_vid)}[/color]", is_user=False)
                return

        if any(w in q_lower for w in ["b-roll", "broll", "stock", "footage", "overlay", "सीन"]):
            log_to_ui("🎬 [Auto B-Roll] Speech se visual keywords extract kiye ja rahe hain...")
            keywords = pro_editor.extract_broll_keywords(instruction)
            log_to_ui(f"📌 B-Roll Targets: {', '.join(keywords)}")
"""

if "extract_broll_keywords" not in text:
    text = text.replace(
        'log_to_ui(f"🤖 [Zaifer Brain] Autonomous execution triggered for: {video_name}")',
        'log_to_ui(f"🤖 [Zaifer Brain] Autonomous execution triggered for: {video_name}")\n' + smart_router
    )

with open("zaifer_app.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Pro-Editor Trio integrated cleanly into ZaiferApp!")
