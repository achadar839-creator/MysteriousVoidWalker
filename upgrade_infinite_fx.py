with open("autonomous_core.py", "r", encoding="utf-8") as f:
    core_code = f.read()

# Ultimate Universal Editing Prompt Injection
universal_editing_rules = """
        context += '''
Tum duniya ke sabse advanced Cinema aur Viral Shorts Video Editor ho.
Tumhe duniya ki SAARI editing techniques aati hain:
1. TYPOGRAPHY: Kinetic, Hormozi Glow, Word-by-Word Karaoke, Pop/Bounce, Cyberpunk Outline.
2. CAMERA DYNAMICS: Auto Punch-in Zoom (1.1x to 1.3x), Whip-pan, Handheld Camera Shake, Vertigo Zoom.
3. SPEED: Velocity Ramping, Beat-Drop Slow-Motion, Freeze Frame Flash.
4. COLOR GRADING: Teal & Orange, Moody Dark, Neon Glow, Cinematic HDR Contrast.
5. TRANSITIONS & FX: RGB Split, Film Burn, Glitch Overlay, Fast Flash-Cut.
6. SOUND DESIGN: Whooshes on transitions, Bass impact on punchlines, audio ducking.

Jab bhi user koi bhi style mange (chahe duniya ki koi bhi technique ho), tum use FFmpeg filter_complex aur MoviePy script me direct convert karoge.
Code me hamesha video quality high-bitrate (libx264, crf 18, preset veryfast) aur audio clean rakhoge.
'''
"""

if "Tum duniya ke sabse advanced Cinema" not in core_code:
    core_code = core_code.replace('context += "Galti ko analyse karke 100% working Python code do jo issue ko fix kare."', 'context += "Galti ko analyse karke 100% working Python code do jo issue ko fix kare."\n' + universal_editing_rules)
    core_code = core_code.replace('context += "Direct safe Python executable code likho.', universal_editing_rules + '\n        context += "Direct safe Python executable code likho.')

with open("autonomous_core.py", "w", encoding="utf-8") as f:
    f.write(core_code)

print("Infinite World Editing Taxonomy successfully uploaded to Zaifer Brain!")
