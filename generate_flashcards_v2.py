import os
import requests

import base64
import time
import json
from tqdm import tqdm

# === 1. Ayarlar ===
webui_url = "http://127.0.0.1:7860" 
output_dir = "outputs_flashcards_v2"
os.makedirs(output_dir, exist_ok=True)

# === 2. Kelime Listesi ===
word_list_path = r"C:\Users\ilker\Desktop\python\python_projects\EnglishFlashCard_project\wordLists\word_list.json"

with open(word_list_path, "r", encoding="utf-8") as file:
    words = json.load(file)

# === 3. Prompt Şablonu ===
def create_prompt(word):
    return f"A colorful and detailed realistic-style image of a {word}, centered on white background, in high quality, vivid, clean, kids illustration."

# === 4. Görsel Üretim Fonksiyonu ===
def generate_image(prompt, output_path):
    payload = {
        "prompt": prompt,
        "steps": 30,
        "cfg_scale": 9,
        "width": 512,
        "height": 512,
    }

    try:
        response = requests.post(f"{webui_url}/sdapi/v1/txt2img", json=payload)
        r = response.json()

        if "images" in r:
            image_data = r["images"][0]
            image_bytes = base64.b64decode(image_data)
            with open(output_path, "wb") as f:
                f.write(image_bytes)
            print(f"[✓] Kayıt edildi: {output_path}")
        else:
            print(f"[!] Görsel üretilemedi: {prompt}")
            print(f"    Sunucu cevabı: {r}")
    except Exception as e:
        print(f"[HATA] {prompt} → {e}")

# === 5. Üretim Döngüsü ===
for word in words:
    prompt = create_prompt(word)
    filename = f"{word.replace(' ', '_')}.png"
    path = os.path.join(output_dir, filename)
    generate_image(prompt, path)
    time.sleep(1)  # sistem yüklenmesin diye küçük bekleme
