import importlib

# आपके पूरे सिस्टम को चलाने वाले अहम पैकेजेस की लिस्ट
dependencies = [
    "requests", 
    "google.generativeai", 
    "google.genai",
    "kivy", 
    "plyer", 
    "yt_dlp", 
    "numpy"
]

print("\n🔍 [SYSTEM SCAN] Checking all Titanium Modules...\n")
missing_modules = []

for lib in dependencies:
    try:
        importlib.import_module(lib)
        print(f"  [ACTIVE] 🟢 {lib}")
    except ImportError:
        print(f"  [MISSING] 🔴 {lib}")
        missing_modules.append(lib)

print("\n" + "="*50)
if not missing_modules:
    print("✅ All modules are perfectly installed and linked!")
else:
    print(f"⚠️ Warning: {len(missing_modules)} modules are missing or unlinked.")
    print(f"🛠️ Fix command: pip install {' '.join(missing_modules)}")
print("="*50 + "\n")
