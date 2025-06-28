import os
import requests
import time
import base64  

# === 1. Ayarlar ===
webui_url = "http://127.0.0.1:7860"
output_dir = "outputs_flashcards"
os.makedirs(output_dir, exist_ok=True)

# === 2. Kelime Listesi ===
words = [
    "apple", "giraffe", "sock", "plate", "armchair", "box", "toy car", "bicycle"
]

# === 3. Prompt Şablonları ===
def create_prompts(word):
    object_prompt = f"A colorful cartoon-style image of a {word}, on a clean white background, simple and centered, designed for kids."
    scene_prompt = f"A cheerful cartoon illustration of a child using or interacting with a {word}, in a playful and educational context, for a children's flashcard."
    return object_prompt, scene_prompt

# === 4. Stable Diffusion'e POST İsteği ===
def generate_image(prompt, output_path):
    payload = {
        "prompt": prompt,
        "steps": 20,
        "cfg_scale": 7,
        "width": 512,
        "height": 512,
    }
    response = requests.post(url=f"{webui_url}/sdapi/v1/txt2img", json=payload)
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

# === 5. Tüm Kelimeler İçin Üretim Döngüsü ===
for word in words:
    object_prompt, scene_prompt = create_prompts(word)

    # Dosya adlarını oluştur
    object_path = os.path.join(output_dir, f"{word.replace(' ', '_')}_object.png")
    scene_path = os.path.join(output_dir, f"{word.replace(' ', '_')}_scene.png")

    # Görselleri üret
    generate_image(object_prompt, object_path)
    time.sleep(1)  # sistem zorlanmasın diye
    generate_image(scene_prompt, scene_path)
    time.sleep(1)
