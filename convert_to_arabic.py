import json
import os

# Latin'den Arap alfabesine çeviri kuralları
def latin_to_arabic(word):
    mapping = {
        'a': 'ا', 'b': 'ب', 'c': 'ج', 'ç': 'چ', 'd': 'د', 'e': 'ه', 'f': 'ف',
        'g': 'گ', 'ğ': 'غ', 'h': 'ح', 'ı': 'ی', 'i': 'ی', 'j': 'ج', 'k': 'ک',
        'l': 'ل', 'm': 'م', 'n': 'ن', 'o': 'و', 'ö': 'و', 'p': 'پ', 'r': 'ر',
        's': 'س', 'ş': 'ش', 't': 'ت', 'u': 'و', 'ü': 'و', 'v': 'و', 'y': 'ی',
        'z': 'ز',
        'â': 'آ', 'î': 'ی', 'û': 'و', 'â': 'ا', 'î': 'ی', 'û': 'و',
        ' ': ' ', '-': '-', '.': '.', ',': '،', '?': '؟', '!': '!'
    }
    
    result = ''
    for char in word.lower():
        result += mapping.get(char, char)
    return result

def process_json_file(file_path):
    try:
        # JSON dosyasını oku
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Her kelimeyi çevir
        for item in data:
            if 'kelime' in item:
                item['arabic'] = latin_to_arabic(item['kelime'])
            elif 'masdar' in item:
                item['arabic'] = latin_to_arabic(item['masdar'])
            elif 'isim' in item:
                item['arabic'] = latin_to_arabic(item['isim'])
            elif 'tekil' in item:
                item['arabic'] = latin_to_arabic(item['tekil'])
            elif 'çoğul' in item:
                item['arabic'] = latin_to_arabic(item['çoğul'])
        
        # Yeni dosya adı oluştur
        file_name, file_ext = os.path.splitext(file_path)
        new_file_path = f"{file_name}_arabic{file_ext}"
        
        # Yeni JSON dosyası oluştur
        with open(new_file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"Başarıyla dönüştürüldü: {new_file_path}")
        return True
    except Exception as e:
        print(f"Hata oluştu ({file_path}): {str(e)}")
        return False

# Tüm JSON dosyalarını işle
json_files = [
    'osmanlica_kelimeler.json',
    'arapca_cogul_tekil_kelimeler.json',
    'İSM-İ fail_meful.json',
    'arapca_mezid_masdarlar.json',
    'farsca_osmanlica_kelimeler.json',
    'Arapça ve Farsça Çoğul Kelimeler ve Tekilleri.json'
]

success_count = 0
for file in json_files:
    if process_json_file(file):
        success_count += 1

print(f"\nToplam {success_count} dosya başarıyla dönüştürüldü.") 