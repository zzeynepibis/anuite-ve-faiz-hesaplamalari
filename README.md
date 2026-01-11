# Anuite ve Faiz Hesaplamalari - Aktüeryal Hesaplama Kütüphanesi

[![PyPI version](https://badge.fury.io/py/anuite-ve-faiz-hesaplamalari.svg)](https://badge.fury.io/py/anuite-ve-faiz-hesaplamalari)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Türkçe aktüeryal ve finans matematiği hesaplamaları için kapsamlı Python kütüphanesi.

---

## 📦 Kurulum

### PyPI'dan Kurulum (Önerilen)
```bash
pip install anuite-ve-faiz-hesaplamalari
```

### GitHub'dan Kurulum
```bash
pip install git+https://github.com/zzeynepibis/anuite-ve-faiz-hesaplamalari.git
```


### Manuel Kurulum
```bash
git clone https://github.com/zzeynepibis/anuite-ve-faiz-hesaplamalari.git
cd anuite-ve-faiz-hesaplamalari
pip install -e .
```

---

## 🚀 Hızlı Başlangıç

```python
from anuiteler import *

# Devre sonu anüite - Bugünkü değer
bd = ds_bd_hesapla(odeme=1000, n=5, i=0.10)
print(f"Bugünkü Değer: {bd:.2f} TL")  # 3790.79 TL

# Aylık kredi taksiti hesaplama
taksit = aylik_taksit_hesapla(ana_para=100000, yillik_faiz=0.20, ay_sayisi=36)
print(f"Aylık Taksit: {taksit:.2f} TL")

# Hızlı hesaplama
sonuc = anuite_hesapla(bugunku_deger=50000, n=24, i=0.015)
print(f"Aylık Ödeme: {sonuc['odeme']:.2f} TL")
```

---

## 📚 Modüller ve Özellikler

### 1️⃣ **Tek Ödeme Modülü** (`tek_odeme`)
Tek bir ödemenin bugünkü ve gelecek değer hesaplamaları.

```python
# Gelecek değer
gd = tek_odeme_gd(bugunku_deger=1000, i=0.10, t=5)

# Bugünkü değer
bd = tek_odeme_bd(gelecek_deger=1610.51, i=0.10, t=5)

# Faiz oranı hesaplama
i = tek_odeme_faiz(bugunku_deger=1000, gelecek_deger=1610.51, t=5)

# Süre hesaplama
t = tek_odeme_sure(bugunku_deger=1000, gelecek_deger=1610.51, i=0.10)
```

**Formüller:**
- Gelecek Değer: `GD = BD × (1+i)^t`
- Bugünkü Değer: `BD = GD × v^t` (v = 1/(1+i))

---

### 2️⃣ **Devre Sonu Anüiteler** (`devre_sonu_anuite`)
Ödemeler her dönemin **SONUNDA** yapılır.

```python
# Bugünkü Değer Hesaplamaları
bd = ds_bd_hesapla(odeme=1000, n=5, i=0.10)
odeme = ds_odeme_bd(bugunku_deger=3790.79, n=5, i=0.10)
n = ds_sure_bd(bugunku_deger=3790.79, odeme=1000, i=0.10)
i = ds_faiz_bd(bugunku_deger=3790.79, odeme=1000, n=5)

# Gelecek Değer Hesaplamaları
gd = ds_gd_hesapla(odeme=1000, n=5, i=0.10)
odeme = ds_odeme_gd(gelecek_deger=6105.10, n=5, i=0.10)
n = ds_sure_gd(gelecek_deger=6105.10, odeme=1000, i=0.10)
i = ds_faiz_gd(gelecek_deger=6105.10, odeme=1000, n=5)

# Amortisman tablosu
tablo = ds_tablo(odeme=1000, n=5, i=0.10)
```

**Formüller:**
- Bugünkü Değer: `BD = a × [(1 - v^n) / i]`
- Gelecek Değer: `GD = a × [(1+i)^n - 1] / i`

---

### 3️⃣ **Devre Başı Anüiteler** (`devre_basi_anuite`)
Ödemeler her dönemin **BAŞINDA** yapılır.

```python
# Bugünkü Değer
bd = db_bd_hesapla(odeme=1000, n=5, i=0.10)

# Gelecek Değer
gd = db_gd_hesapla(odeme=1000, n=5, i=0.10)

# Ters formüller
odeme = db_odeme_bd(bugunku_deger=4169.87, n=5, i=0.10)
n = db_sure_bd(bugunku_deger=4169.87, odeme=1000, i=0.10)
i = db_faiz_bd(bugunku_deger=4169.87, odeme=1000, n=5)
```

**Formüller:**
- Bugünkü Değer: `BD = a × (1+i) × [(1 - v^n) / i]`
- Gelecek Değer: `GD = a × (1+i) × [(1+i)^n - 1] / i`
- İlişki: `ä(n,i) = a(n,i) × (1+i)`

---

### 4️⃣ **Sürekli Anüiteler** (`surekli_anuite`)
Ödemeler **sonsuza kadar** devam eder (n → ∞).

```python
# Devre sonu sürekli anüite
bd = surekli_ds_bd(odeme=1000, i=0.10)  # 10000 TL
odeme = surekli_ds_odeme(bugunku_deger=10000, i=0.10)
i = surekli_ds_faiz(bugunku_deger=10000, odeme=1000)

# Devre başı sürekli anüite
bd = surekli_db_bd(odeme=1000, i=0.10)  # 11000 TL

# Ertelenmiş sürekli anüite
bd = ertelenmis_surekli_anuite(odeme=1000, i=0.10, erteleme_suresi=3)
```

**Formüller:**
- Devre Sonu: `BD = a / i`
- Devre Başı: `BD = a × (1+i) / i`

---

### 5️⃣ **Ertelenmiş Anüiteler** (`ertekenmis_anuite`)
Ödemeler **m dönem sonra** başlar.

```python
# Devre sonu ertelenmiş
bd = ert_ds_bd(taksit=10000, i=0.30, n=8, m=4)
taksit = ert_ds_taksit_bd(bugunku_deger=32000, i=0.30, n=8, m=4)

# Devre başı ertelenmiş
bd = ert_db_bd(taksit=10000, i=0.30, n=8, m=4)

# Gecikme süresi hesaplama
m = ert_gecikme_hesapla(bugunku_deger=32000, taksit=10000, i=0.30, n=8)

# Faiz oranı hesaplama
i = ert_faiz_hesapla(bugunku_deger=32000, taksit=10000, n=8, m=4)

# Çabuklaştırılmış + Ertelenmiş
bd = ert_cabuklas_bd(taksit=10000, i=0.30, n=8, m=4, c=2)
```

**Formüller:**
- Devre Sonu: `BD = a × [(1+i)^n - 1] / [(1+i)^(n+m) × i]`
- Devre Başı: `BD = a × (1+i) × [(1+i)^n - 1] / [(1+i)^(n+m) × i]`

---

### 6️⃣ **Geometrik Anüiteler** (`geometrik_anuite`)
Taksitler **geometrik dizi** şeklinde değişir: a, a(1+r), a(1+r)², ...

```python
# Devre sonu
bd = geo_ds_bd(ilk_taksit=5000, i=0.05, r=0.20, n=6)
gd = geo_ds_gd(ilk_taksit=5000, i=0.05, r=0.20, n=6)

# Devre başı
bd = geo_db_bd(ilk_taksit=5000, i=0.05, r=0.20, n=6)

# İlk taksit hesaplama
ilk_taksit = geo_ilk_taksit_bd(bugunku_deger=40000, i=0.05, r=0.20, n=6)

# i = r özel durumu
bd = geo_ds_bd(ilk_taksit=5000, i=0.10, r=0.10, n=6)  # n × a × (1+i)^(n-1)
```

**Formüller:**
- `i ≠ r`: `BD = a × (1+i)^n × [(1+i)^n - (1+r)^n] / [(1+i)^n × (i-r)]`
- `i = r`: `BD = n × a × (1+i)^(n-1)`

---

### 7️⃣ **Aritmetik Anüiteler** (`aritmetik_anuite`)
Taksitler **aritmetik dizi** şeklinde değişir: a, a+b, a+2b, ...

```python
# Devre sonu (artan taksitler)
bd = arit_ds_bd(ilk_taksit=5000, degisim=500, i=0.30, n=6)
gd = arit_ds_gd(ilk_taksit=5000, degisim=500, i=0.30, n=6)

# Devre sonu (azalan taksitler)
bd = arit_ds_bd(ilk_taksit=5000, degisim=-500, i=0.30, n=6)

# İlk taksit hesaplama
ilk_taksit = arit_ds_ilk_taksit_bd(bugunku_deger=18000, degisim=500, i=0.30, n=6)

# Değişim miktarı (b) hesaplama
degisim = arit_ds_degisim(bugunku_deger=18000, ilk_taksit=1101, i=0.40, n=5)

# Devre başı
bd = arit_db_bd(ilk_taksit=5000, degisim=500, i=0.30, n=6)
```

**Formül:**
- Devre Sonu: `BD = (a + b/i) × [(1+i)^n - 1] / i - b×n / i`

---

### 8️⃣ **Çabuklaştırılmış Anüiteler** (`cabuklas_anuite`)
Ödemeler **c dönem erken** yapılır (öne çekilir).

```python
# Devre sonu çabuklaştırılmış
bd = cab_ds_bd(taksit=10000, i=0.30, n=8, c=2)
gd = cab_ds_gd(taksit=10000, i=0.30, n=8, c=2)

# Devre başı çabuklaştırılmış
bd = cab_db_bd(taksit=10000, i=0.30, n=8, c=2)

# Taksit hesaplama
taksit = cab_taksit_bd(bugunku_deger=48000, i=0.30, n=8, c=2)

# Çabuklaştırma süresi hesaplama
c = cab_sure_hesapla(bugunku_deger=51815.69, taksit=10000, i=0.30, n=8)

# Faiz oranı hesaplama
i = cab_faiz_hesapla(bugunku_deger=51815.69, taksit=10000, n=8, c=2)
```

**Formüller:**
- Devre Sonu: `BD = a × (1+i)^c × [(1+i)^n - 1] / [(1+i)^n × i]`
- Devre Başı: `BD = a × (1+i)^(c+1) × [(1+i)^n - 1] / [(1+i)^n × i]`

---

### 9️⃣ **Yardımcı Fonksiyonlar** (`yardimci`)

#### Faiz Oranı Çevrimleri
```python
# Efektif ↔ Nominal
efektif = efektif_faiz_orani(nominal_oran=0.12, m=12)  # Aylık bileşik
nominal = nominal_faiz_orani(efektif_oran=0.1268, m=12)

# Sürekli faiz (Force of Interest)
delta = surekli_faiz_orani(efektif_oran=0.10)  # δ
efektif = efektif_from_surekli(delta=0.0953)

# Faiz ↔ İskonto
d = faizden_iskonto_orani(i=0.10)  # d = i/(1+i)
i = iskontodan_faiz_orani(d=0.0909)  # i = d/(1-d)
```

#### Zaman Çevrimleri
```python
aylik = yillik_aylik_cevir(yillik_oran=0.12)
yillik = aylik_yillik_cevir(aylik_oran=0.0095)
gunluk = yillik_gunluk_cevir(yillik_oran=0.12)
ceyreklik = yillik_ceyreklik_cevir(yillik_oran=0.12)
```

#### Enflasyon Düzeltmeleri
```python
# Fisher denklemi
reel = reel_faiz_orani(nominal_oran=0.15, enflasyon_orani=0.08)
nominal = nominal_from_reel(reel_oran=0.0648, enflasyon_orani=0.08)
```

#### Duration ve Convexity
```python
nakit_akislari = [(1, 1000), (2, 1000), (3, 1000), (4, 1000), (5, 101000)]

# Macaulay Duration
mac_dur = macaulay_duration(nakit_akislari, faiz_orani=0.05)

# Modified Duration
mod_dur = modified_duration(nakit_akislari, faiz_orani=0.05)

# Convexity (Dışbükeylik)
conv = convexity(nakit_akislari, faiz_orani=0.05)

# DV01
dv01_deger = dv01(nakit_akislari, faiz_orani=0.05)
```

#### NPV ve IRR
```python
# Net Bugünkü Değer
npv = net_bugunku_deger(nakit_akislari, faiz_orani=0.10, baslangic_yatirim=-10000)

# İç Verim Oranı (Internal Rate of Return)
irr = ic_verim_orani(nakit_akislari, baslangic_yatirim=-10000)
```

#### Kredi Hesaplamaları
```python
# Aylık taksit
taksit = aylik_taksit_hesapla(ana_para=100000, yillik_faiz=0.20, ay_sayisi=36)

# Kalan borç
kalan = kalan_borc_hesapla(ana_para=100000, yillik_faiz=0.20, ay_sayisi=36, gecen_ay=12)

# Erken ödeme
erken_odeme = erken_odeme_tutari(ana_para=100000, yillik_faiz=0.20, ay_sayisi=36, gecen_ay=12)
```

---

## 🎯 Örnek Kullanımlar

### Örnek 1: Kredi Hesaplama
```python
from anuiteler import *

# 100.000 TL kredi, %20 yıllık faiz, 36 ay vade
ana_para = 100000
yillik_faiz = 0.20
vade = 36

# Aylık taksit
taksit = aylik_taksit_hesapla(ana_para, yillik_faiz, vade)
print(f"Aylık Taksit: {taksit:.2f} TL")

# 12. ay sonu kalan borç
kalan = kalan_borc_hesapla(ana_para, yillik_faiz, vade, gecen_ay=12)
print(f"12. Ay Kalan Borç: {kalan:.2f} TL")

# Toplam ödenen tutar
toplam = taksit * vade
print(f"Toplam Ödeme: {toplam:.2f} TL")
print(f"Toplam Faiz: {toplam - ana_para:.2f} TL")
```

### Örnek 2: Yatırım Analizi
```python
from anuiteler import *

# 5 yıllık tahvil: Her yıl 1000 TL kupon, son yılda 10.000 TL anapara
nakit_akislari = [
    (1, 1000),
    (2, 1000),
    (3, 1000),
    (4, 1000),
    (5, 11000)
]

# %8 faizle NPV
npv = net_bugunku_deger(nakit_akislari, faiz_orani=0.08, baslangic_yatirim=-10000)
print(f"NPV: {npv:.2f} TL")

# İç verim oranı (IRR)
irr = ic_verim_orani(nakit_akislari, baslangic_yatirim=-10000)
print(f"IRR: %{irr*100:.2f}")

# Duration
mac_dur = macaulay_duration(nakit_akislari, faiz_orani=0.08)
print(f"Macaulay Duration: {mac_dur:.2f} yıl")
```

### Örnek 3: Emeklilik Planlaması
```python
from anuiteler import *

# Ayda 1000 TL biriktirerek 20 yılda ne kadar olur?
# %10 yıllık getiri
aylik_birikim = 1000
yil = 20
ay_sayisi = yil * 12
aylik_faiz = yillik_aylik_cevir(0.10)

# Gelecek değer (devre sonu)
gd = ds_gd_hesapla(odeme=aylik_birikim, n=ay_sayisi, i=aylik_faiz)
print(f"20 yıl sonra birikim: {gd:,.2f} TL")

# Emeklilikte ayda ne kadar çekebilir? (25 yıl boyunca)
cekim_suresi = 25 * 12
aylik_cekim = ds_odeme_bd(bugunku_deger=gd, n=cekim_suresi, i=aylik_faiz)
print(f"Aylık çekilebilecek tutar: {aylik_cekim:.2f} TL")
```

---

## 📖 Dokümantasyon

### Fonksiyon İsimlendirme Mantığı

Kütüphane **Türkçe** ve **tutarlı** isimlendirme kullanır:

| Kısaltma | Anlamı |
|----------|--------|
| `ds` | Devre Sonu |
| `db` | Devre Başı |
| `bd` | Bugünkü Değer |
| `gd` | Gelecek Değer |
| `ert` | Ertelenmiş |
| `geo` | Geometrik |
| `arit` | Aritmetik |
| `cab` | Çabuklaştırılmış |

**Örnekler:**
- `ds_bd_hesapla()` → **D**evre **S**onu **B**ugünkü **D**eğer hesapla
- `db_gd_hesapla()` → **D**evre **B**aşı **G**elecek **D**eğer hesapla
- `ert_ds_taksit_bd()` → **Ert**elenmiş **D**evre **S**onu, BD'den **Taksit** hesapla

---

## 🧪 Test Etme

```bash
# Test dosyasını çalıştır
python tests/test_anuite.py

# veya pytest ile
python -m pytest tests/
```

Tüm modüller için kapsamlı test paketi mevcuttur.

---

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen:

1. Bu repository'yi fork edin
2. Feature branch oluşturun (`git checkout -b yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'i push edin (`git push origin yeni-ozellik`)
5. Pull Request oluşturun

---

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

---

## 👤 Geliştirici

**Zeynep İbiş**
- Tarih: 11 Ocak 2025
- Amaç: Aktüeryal hesaplamalar için Türkçe Python kütüphanesi
- GitHub: [zzeynepibis](https://github.com/zzeynepibis)
- Email: zzeynepibis@gmail.com


---

## 📚 Ders Materyalleri ve Eğitimciler

- Demet Sezer - Finans Matematiği Öğretmeni 
- Zehra Başkaya - Finans Matematiği Ders Notları
- Emine Ebru Akaoy - Aktüerya Matematiği Ders Notları

---

## 📚 Referanslar

Bu kütüphane aşağıdaki kaynaklara dayanmaktadır:

1. **Kellison, S. G.** (2009). *The Theory of Interest* (3rd ed.). McGraw-Hill/Irwin.
2. **Broverman, S. A.** (2008). *Mathematics of Investment and Credit* (4th ed.). ACTEX Publications.
3. **McCutcheon, J. J., & Scott, W. F.** (1986). *An Introduction to the Mathematics of Finance*. Heinemann.

---

## ❓ Sık Sorulan Sorular (SSS)

### Devre sonu ve devre başı arasındaki fark nedir?

- **Devre Sonu:** Ödemeler dönem sonunda (örn: her ayın son günü)
- **Devre Başı:** Ödemeler dönem başında (örn: her ayın ilk günü)

Devre başı anüitelerde bugünkü değer `(1+i)` faktörü kadar daha yüksektir.

### Hangi formülü kullanmalıyım?

| Durum | Modül |
|-------|-------|
| Kredi taksiti | `devre_sonu_anuite` |
| Kira ödemeleri | `devre_basi_anuite` |
| Artan maaşlar | `geometrik_anuite` veya `aritmetik_anuite` |
| Erteleme var | `ertekenmis_anuite` |
| Erken ödeme | `cabuklas_anuite` |
| Sonsuz ödeme | `surekli_anuite` |

### IRR hesaplama yakınsamıyor, ne yapmalıyım?

IRR hesaplaması Newton-Raphson yöntemi kullanır. Yakınsama problemi yaşarsanız:

```python
# Daha iyi başlangıç tahmini verin
irr = ic_verim_orani(nakit_akislari, baslangic_yatirim=-10000, tahmin=0.15)

# Toleransı artırın
irr = ic_verim_orani(nakit_akislari, baslangic_yatirim=-10000, tolerans=1e-4)

# Maksimum iterasyonu artırın
irr = ic_verim_orani(nakit_akislari, baslangic_yatirim=-10000, max_iter=200)
```

---

## 🔄 Versiyon Geçmişi

### v1.0.0 (2025-01-11)
- ✅ İlk stabil sürüm
- ✅ 9 ana modül
- ✅ 150+ fonksiyon
- ✅ Kapsamlı test paketi
- ✅ Türkçe dokümantasyon

---

## ⭐ Destek

Bu projeyi beğendiyseniz lütfen ⭐ vererek destek olun!

---

**Not:** Bu kütüphane eğitim amaçlıdır. Gerçek finansal kararlar almadan önce bir finans uzmanına danışın."# anuite-ve-faiz-hesaplamalari"  
