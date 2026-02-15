# English FlashCard Project

Bu proje, İngilizce kelimeler için AI tabanlı flash kartlar oluşturan bir Python uygulamasıdır. Stable Diffusion WebUI kullanarak kelime listesindeki her kelime için yüksek kaliteli, çocuklara uygun illüstrasyon görselleri üretir.

This project is a Python application that creates AI-powered flashcards for English vocabulary learning. It uses Stable Diffusion WebUI to generate high-quality, child-friendly illustration images for each word in the word list.

---

## Bu Proje ile Ne Yapabilirsiniz? / What Can You Do with This Project?

- 📚 **Kelime kartları oluşturma / Create vocabulary flashcards**: İngilizce kelimeler için otomatik olarak renkli, eğitici görseller üretin. Automatically generate colorful, educational images for English words.
- 🎨 **AI destekli görsel üretimi / AI-powered image generation**: Stable Diffusion ile yüksek kaliteli illüstrasyonlar. High-quality illustrations powered by Stable Diffusion.
- 👶 **Çocuklar için uygun / Kid-friendly**: Çocuk eğitimine yönelik tasarlanmış görsel stili. Visual style designed for children's education.
- 🌍 **İngilizce-Türkçe kelime listesi / English-Turkish word list**: Hazır kelime listesi ile hemen başlayın. Get started immediately with the ready-made word list.
- ✏️ **Özelleştirilebilir / Customizable**: Kendi kelime listenizi ekleyerek özel kartlar oluşturun. Create custom cards by adding your own word list.

---

## Özellikler / Features

- Kelime listesinden otomatik görsel üretimi / Automatic image generation from word list
- Stable Diffusion WebUI entegrasyonu / Stable Diffusion WebUI integration
- Yüksek kaliteli, renkli ve gerçekçi görsel çıktıları / High-quality, colorful, and realistic visual outputs
- Çocuklar için uygun illüstrasyon stili / Child-friendly illustration style
- İki versiyon: basit nesne görseli (v1) ve geliştirilmiş detaylı görsel (v2) / Two versions: simple object visual (v1) and improved detailed visual (v2)

## Gereksinimler / Prerequisites

- **Python 3.7+**
- **Stable Diffusion WebUI** — Yerel makinenizde kurulu ve çalışır durumda olmalıdır. Must be installed and running on your local machine.
  - Kurulum rehberi / Installation guide: [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
  - API modunda başlatılmalıdır / Must be started with API mode enabled: `--api` flag

## Kurulum / Installation

1. Depoyu klonlayın / Clone the repository:
```bash
git clone https://github.com/hobibilgisi/EnglishFlashCard_project.git
cd EnglishFlashCard_project
```

2. Gerekli Python paketlerini yükleyin / Install the required Python packages:
```bash
pip install -r requirements.txt
```

## Kullanım / Usage

### Adım 1: Stable Diffusion WebUI'yi Başlatın / Start Stable Diffusion WebUI

Stable Diffusion WebUI'yi `--api` bayrağı ile başlatın. Bu, uygulamanın `http://127.0.0.1:7860` adresinde API erişimine sahip olmasını sağlar.

Start Stable Diffusion WebUI with the `--api` flag. This allows the application to access the API at `http://127.0.0.1:7860`.

```bash
# Stable Diffusion WebUI dizininde / In the Stable Diffusion WebUI directory:
./webui.sh --api    # Linux/Mac
webui-user.bat      # Windows (--api bayrağını .bat dosyasına ekleyin / add --api flag to .bat file)
```

### Adım 2: Kelime Listesini Düzenleyin (İsteğe Bağlı) / Edit the Word List (Optional)

Kelime listesi `wordLists/word_list.json` dosyasındadır. JSON formatında her kelime için İngilizce kelime ve Türkçe anlamı bulunur:

The word list is in the `wordLists/word_list.json` file. Each entry contains an English word and its Turkish meaning in JSON format:

```json
[
    {
        "word": "apple",
        "meaning": "elma"
    },
    {
        "word": "book",
        "meaning": "kitap"
    }
]
```

Kendi kelimelerinizi ekleyebilir veya mevcut listeyi düzenleyebilirsiniz. You can add your own words or edit the existing list.

### Adım 3: Görselleri Üretin / Generate the Images

```bash
# Geliştirilmiş versiyon (önerilen) / Improved version (recommended):
python generate_flashcards_v2.py

# İlk versiyon (nesne + sahne görselleri) / First version (object + scene images):
python generate_flashcards.py
```

Üretilen görseller aşağıdaki klasörlerde saklanacaktır / Generated images will be saved in these directories:
- `outputs_flashcards_v2/` — v2 görselleri / v2 images
- `outputs_flashcards/` — v1 görselleri / v1 images

## Dosya Yapısı / File Structure

```
EnglishFlashCard_project/
├── README.md                       # Bu dosya / This file
├── requirements.txt                # Python bağımlılıkları / Python dependencies
├── generate_flashcards.py          # v1: Nesne + sahne görseli üretici / Object + scene image generator
├── generate_flashcards_v2.py       # v2: Geliştirilmiş görsel üretici / Improved image generator
├── wordLists/
│   ├── word_list.json              # Kelime listesi (JSON) / Word list (JSON)
│   ├── word_list.txt               # Kelime listesi (TXT) / Word list (TXT)
│   └── json_olustur.py             # TXT → JSON dönüştürücü / TXT to JSON converter
├── Visuals/                        # Tasarım dosyaları ve logolar / Design files and logos
├── outputs_flashcards/             # v1 üretilen görseller / v1 generated images
└── outputs_flashcards_v2/          # v2 üretilen görseller / v2 generated images
```

## v1 vs v2 Farkları / v1 vs v2 Differences

| Özellik / Feature | v1 (`generate_flashcards.py`) | v2 (`generate_flashcards_v2.py`) |
|---|---|---|
| Görsel sayısı / Images per word | 2 (nesne + sahne / object + scene) | 1 (detaylı / detailed) |
| Stil / Style | Karikatür / Cartoon | Gerçekçi / Realistic |
| Kalite ayarları / Quality settings | steps: 20, cfg: 7 | steps: 30, cfg: 9 |
| Kelime kaynağı / Word source | Script içi liste / Inline list | JSON dosyası / JSON file |

## Katkıda Bulunma / Contributing

1. Bu depoyu fork edin / Fork this repository
2. Yeni bir branch oluşturun / Create a new branch
3. Değişikliklerinizi commit edin / Commit your changes
4. Branch'inizi push edin / Push your branch
5. Pull request oluşturun / Create a pull request

## Lisans / License

Bu proje MIT lisansı altında yayınlanmıştır. / This project is licensed under the MIT License.
