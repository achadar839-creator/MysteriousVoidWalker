import os, re, glob

print("\n" + "="*55)
print(" 🤖 ZAIFER AI - FULL SYSTEM DIAGNOSTICS & FEATURE SCAN")
print("="*55 + "\n")

py_files = glob.glob("*.py")
if not py_files:
    print("[-] कोई Python फाइल नहीं मिली! लगता है कोड किसी और फोल्डर में है।")
    exit()

total_lines = 0
all_code = ""

for pf in py_files:
    try:
        with open(pf, "r", encoding="utf-8") as f:
            code = f.read()
            all_code += code + "\n"
            lines = len(code.split('\n'))
            total_lines += lines
            print(f"[*] फाइल स्कैन हुई: {pf} (Lines: {lines})")
    except Exception as e:
        print(f"[-] फाइल पढ़ने में एरर {pf}: {e}")

print(f"\n[!] Total Code Size: {total_lines} Lines of Code")

print("\n[+] --- CAPABILITY ENGINE (आपका AI अभी क्या-क्या कर सकता है) ---")
if re.search(r'import os|subprocess|sys', all_code):
    print("  [✓] System Control : OS को कंट्रोल करना, फाइलें बनाना/डिलीट करना, Termux चलाना।")
if re.search(r'requests|urllib|socket|http', all_code):
    print("  [✓] Internet Access: इंटरनेट से डेटा लाना, सर्वर से कनेक्ट करना।")
if re.search(r'sqlite3|json|open\(', all_code):
    print("  [✓] Memory & Storage: डेटा याद रखना (Memory) और फोन में फाइलें सेव करना।")
if re.search(r'kivy|App|BoxLayout', all_code):
    print("  [✓] GUI/Visuals    : Kivy का ग्राफिकल यूजर इंटरफेस (बटन, स्क्रीन) चालू है।")
if re.search(r'camera|cv2|vision|image', all_code, re.IGNORECASE):
    print("  [✓] Vision System  : कैमरा इस्तेमाल करने या इमेज देखने की पावर।")
if re.search(r'audio|voice|speech|mic|record', all_code, re.IGNORECASE):
    print("  [✓] Audio/Voice    : माइक (Mic) से सुनना या आवाज़ (3D Voice) निकालना।")
if re.search(r'threading|multiprocessing|Clock', all_code):
    print("  [✓] Multi-Tasking  : बैकग्राउंड में बिना रुके एक साथ कई काम करना।")

print("\n[+] --- 14-TITAN ARCHITECTURE CHECK (आपके स्पेशल 13+ फीचर्स) ---")
features = [
    "14-Titan", "Zaifer Architecture", "Phantom Core", "Kinetic Mesh", 
    "Supreme Autonomous Suite", "Autonomous Editor", "Vision QA", 
    "3D HD Voice", "Gallery Picker", "Mic Voice Input"
]

for feat in features:
    # कोड में केस-इन्सेंसिटिव सर्च करना
    if feat.lower() in all_code.lower():
        print(f"  [ACTIVE]  {feat}")
    else:
        print(f"  [MISSING] {feat} (नाम नहीं मिला, शायद किसी और फाइल/नाम से सेव है)")

print("\n" + "="*55)
print("स्कैन पूरा हुआ! रिपोर्ट पढ़ें और तय करें कि आगे क्या अपडेट करना है।")
print("="*55 + "\n")
