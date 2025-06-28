# English FlashCard Project

Bu proje, İngilizce kelimeler için AI tabanlı flash kartlar oluşturan bir Python uygulamasıdır.

## Özellikler

- Kelime listesinden otomatik görsel üretimi
- Stable Diffusion WebUI entegrasyonu
- Yüksek kaliteli, renkli ve gerçekçi görsel çıktıları
- Çocuklar için uygun illüstrasyon stili

## Kurulum

1. Depoyu klonlayın:
```bash
git clone https://github.com/YOUR_USERNAME/EnglishFlashCard_project.git
cd EnglishFlashCard_project
```

2. Gerekli Python paketlerini yükleyin:
```bash
pip install -r requirements.txt
```

## Kullanım

1. Stable Diffusion WebUI'yi başlatın (http://127.0.0.1:7860)
2. Kelime listenizi `wordLists/word_list.json` dosyasına ekleyin
3. Görsel üretimi için scripti çalıştırın:

```python
python generate_flashcards_v2.py
```

Üretilen görseller `outputs_flashcards_v2/` klasöründe saklanacaktır.

## Dosya Yapısı

- `generate_flashcards.py` - İlk versiyon görsel üretici
- `generate_flashcards_v2.py` - Geliştirilmiş versiyon
- `wordLists/` - Kelime listeleri ve veri dosyaları
- `outputs_flashcards/` - Üretilen görseller (v1)
- `outputs_flashcards_v2/` - Üretilen görseller (v2)
- `Visuals/` - Tasarım dosyaları ve logolar

## Gereksinimler

- Python 3.7+
- Stable Diffusion WebUI
- İnternet bağlantısı (görsel üretimi için)

## Katkıda Bulunma

1. Bu depoyu fork edin
2. Yeni bir branch oluşturun
3. Değişikliklerinizi commit edin
4. Branch'inizi push edin
5. Pull request oluşturun

## Lisans

Bu proje MIT lisansı altında yayınlanmıştır.
