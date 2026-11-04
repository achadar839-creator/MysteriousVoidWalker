with open("zaifer_app.py", "r", encoding="utf-8") as f:
    text = f.read()

# Android runtime permissions request import
android_perm_code = """
from kivy.utils import platform

def request_android_permissions():
    if platform == "android":
        try:
            from android.permissions import request_permissions, Permission
            request_permissions([
                Permission.INTERNET,
                Permission.RECORD_AUDIO,
                Permission.READ_MEDIA_VIDEO,
                Permission.READ_EXTERNAL_STORAGE,
                Permission.WRITE_EXTERNAL_STORAGE
            ])
        except Exception:
            pass
"""

if "request_android_permissions" not in text:
    text = android_perm_code + "\n" + text
    text = text.replace(
        "def on_start(self):",
        "def on_start(self):\n        request_android_permissions()"
    )

with open("zaifer_app.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Runtime permissions and stability patch applied!")
