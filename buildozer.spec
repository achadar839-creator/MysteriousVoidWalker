[app]
title = Zaifer AI
package.name = zaifer
package.domain = org.chandan.zaifer
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt
version = 1.0

# Dependencies (Kivy aur requests chahiye)
requirements = python3,kivy,requests,yt-dlp,plyer

# Android Settings
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,RECORD_AUDIO,READ_MEDIA_VIDEO,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21

[buildozer]
log_level = 2
warn_on_root = 1
