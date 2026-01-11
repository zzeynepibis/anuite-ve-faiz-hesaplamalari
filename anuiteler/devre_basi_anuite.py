"""
DEVRE BAŞI ÖDEMELİ ANÜİTELER (Annuity-Due)

Ödemeler her dönemin BAŞINDA yapılır.

Temel Formüller:
- Bugünkü Değer: BD = a × (1+i) × [(1 - v^n) / i]  --> ä(n,i)
- Gelecek Değer: GD = a × (1+i) × [(1+i)^n - 1] / i  --> s̈(n,i)

İlişki:
- ä(n,i) = a(n,i) × (1+i)
- s̈(n,i) = s(n,i) × (1+i)
"""

import math


def pesin_deger_faktoru(i, n):
    """Peşin değer faktörü: ä(n,i)"""
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    if n <= 0:
        raise ValueError("Dönem sayısı sıfırdan büyük olmalıdır.")
    
    v = 1 / (1 + i)
    a_ni = (1 - v**n) / i
    return a_ni * (1 + i)


def gelecek_deger_faktoru(i, n):
    """Gelecek değer faktörü: s̈(n,i)"""
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    if n <= 0:
        raise ValueError("Dönem sayısı sıfırdan büyük olmalıdır.")
    
    s_ni = ((1 + i)**n - 1) / i
    return s_ni * (1 + i)


# ============================================================
# BUGÜNKÜ DEĞER HESAPLAMALARI (BD = a × ä(n,i))
# ============================================================

def bugunku_deger_hesapla(odeme, n, i):
    """BD = a × ä(n,i)"""
    a_due = pesin_deger_faktoru(i, n)
    return odeme * a_due


def odeme_bugunku_degerden(bugunku_deger, n, i):
    """a = BD / ä(n,i)"""
    a_due = pesin_deger_faktoru(i, n)
    return bugunku_deger / a_due


def sure_bugunku_degerden(bugunku_deger, odeme, i):
    """n hesaplama: BD/a = ä(n,i)"""
    if odeme <= 0:
        raise ValueError("Ödeme tutarı sıfırdan büyük olmalıdır.")
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    
    v = 1 / (1 + i)
    hedef_a = bugunku_deger / (odeme * (1 + i))
    
    # i × hedef_a = 1 - v^n
    # v^n = 1 - i × hedef_a
    hedef = 1 - (i * hedef_a)
    
    if hedef <= 0:
        raise ValueError("Geçersiz parametre kombinasyonu.")
    
    return math.log(hedef) / math.log(v)


def faiz_bugunku_degerden(bugunku_deger, odeme, n, tahmin=0.10, tolerans=1e-6, max_iter=100):
    """Newton-Raphson ile faiz oranı hesaplama"""
    if n <= 0:
        raise ValueError("Dönem sayısı sıfırdan büyük olmalıdır.")
    if odeme <= 0:
        raise ValueError("Ödeme tutarı sıfırdan büyük olmalıdır.")
    
    hedef = bugunku_deger / odeme
    
    i = tahmin
    for _ in range(max_iter):
        v = 1 / (1 + i)
        a_ni = (1 - v**n) / i
        a_due = a_ni * (1 + i)
        
        f = a_due - hedef
        
        if abs(f) < tolerans:
            return i
        
        # Türev
        da_di = (n * v**(n+1) / (1+i) - (1 - v**n) / (i**2)) / i
        da_due_di = da_di * (1+i) + a_ni
        
        i = i - f / da_due_di
        
        if i < 0.0001:
            i = 0.0001
    
    return i


# ============================================================
# GELECEK DEĞER HESAPLAMALARI (GD = a × s̈(n,i))
# ============================================================

def gelecek_deger_hesapla(odeme, n, i):
    """GD = a × s̈(n,i)"""
    s_due = gelecek_deger_faktoru(i, n)
    return odeme * s_due


def odeme_gelecek_degerden(gelecek_deger, n, i):
    """a = GD / s̈(n,i)"""
    s_due = gelecek_deger_faktoru(i, n)
    return gelecek_deger / s_due


def sure_gelecek_degerden(gelecek_deger, odeme, i):
    """n hesaplama: GD/a = s̈(n,i)"""
    if odeme <= 0:
        raise ValueError("Ödeme tutarı sıfırdan büyük olmalıdır.")
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    
    hedef_s = gelecek_deger / (odeme * (1 + i))
    
    # i × hedef_s = (1+i)^n - 1
    # (1+i)^n = 1 + i × hedef_s
    hedef = 1 + (i * hedef_s)
    
    if hedef <= 0:
        raise ValueError("Geçersiz parametre kombinasyonu.")
    
    return math.log(hedef) / math.log(1 + i)


def faiz_gelecek_degerden(gelecek_deger, odeme, n, tahmin=0.10, tolerans=1e-6, max_iter=100):
    """Newton-Raphson ile faiz oranı hesaplama (GD'den)"""
    if n <= 0:
        raise ValueError("Dönem sayısı sıfırdan büyük olmalıdır.")
    if odeme <= 0:
        raise ValueError("Ödeme tutarı sıfırdan büyük olmalıdır.")
    
    hedef = gelecek_deger / odeme
    
    i = tahmin
    for _ in range(max_iter):
        s_ni = ((1 + i)**n - 1) / i
        s_due = s_ni * (1 + i)
        
        f = s_due - hedef
        
        if abs(f) < tolerans:
            return i
        
        # Türev
        ds_di = (n * (1+i)**(n-1) / i - ((1+i)**n - 1) / i**2)
        ds_due_di = ds_di * (1+i) + s_ni
        
        i = i - f / ds_due_di
        
        if i < 0.0001:
            i = 0.0001
    
    return i


# ============================================================
# YENİ EKLENENLER: EKSİK FONKSİYONLAR
# ============================================================

def bugunku_deger(odeme, n, i):
    """Genel BD fonksiyonu (kısa isim)"""
    return bugunku_deger_hesapla(odeme, n, i)


def gelecek_deger(odeme, n, i):
    """Genel GD fonksiyonu (kısa isim)"""
    return gelecek_deger_hesapla(odeme, n, i)


def odeme_hesapla_bd(bugunku_deger, n, i):
    """BD'den ödeme (alternatif isim)"""
    return odeme_bugunku_degerden(bugunku_deger, n, i)


def odeme_hesapla_gd(gelecek_deger, n, i):
    """GD'den ödeme (alternatif isim)"""
    return odeme_gelecek_degerden(gelecek_deger, n, i)


def sure_hesapla_bd(bugunku_deger, odeme, i):
    """BD'den süre (alternatif isim)"""
    return sure_bugunku_degerden(bugunku_deger, odeme, i)


def sure_hesapla_gd(gelecek_deger, odeme, i):
    """GD'den süre (alternatif isim)"""
    return sure_gelecek_degerden(gelecek_deger, odeme, i)


def faiz_hesapla_bd(bugunku_deger, odeme, n, tahmin=0.10, tolerans=1e-6, max_iter=100):
    """BD'den faiz (alternatif isim)"""
    return faiz_bugunku_degerden(bugunku_deger, odeme, n, tahmin, tolerans, max_iter)


def faiz_hesapla_gd(gelecek_deger, odeme, n, tahmin=0.10, tolerans=1e-6, max_iter=100):
    """GD'den faiz (alternatif isim)"""
    return faiz_gelecek_degerden(gelecek_deger, odeme, n, tahmin, tolerans, max_iter)


# ============================================================
# YARDIMCI FONKSİYONLAR
# ============================================================

def anuite_tablosu_olustur(odeme, n, i):
    """Amortisman tablosu oluşturur (Devre Başı)"""
    bd = bugunku_deger_hesapla(odeme, n, i)
    kalan = bd
    tablo = []
    
    for donem in range(1, n + 1):
        # Devre başında ödeme yapılıyor
        kalan = kalan - odeme
        faiz = kalan * i
        kalan = kalan + faiz
        
        tablo.append({
            'donem': donem,
            'odeme': odeme,
            'faiz': faiz,
            'anapara': odeme,
            'kalan': max(0, kalan)
        })
    
    return tablo


def toplam_odenen_hesapla(odeme, n):
    """Toplam ödenen tutar"""
    return odeme * n


def toplam_faiz_hesapla(odeme, n, bugunku_deger):
    """Toplam ödenen faiz"""
    toplam_odeme = toplam_odenen_hesapla(odeme, n)
    return toplam_odeme - bugunku_deger


def ortalama_sure_hesapla(odeme, n, i):
    """Ortalama vade (Macaulay duration benzeri) - Devre Başı"""
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    
    v = 1 / (1 + i)
    bd = bugunku_deger_hesapla(odeme, n, i)
    
    # Devre başında ödemeler 0, 1, 2, ..., n-1 zamanlarında
    agirlikli_toplam = sum(t * odeme * (v ** t) for t in range(0, n))
    
    return agirlikli_toplam / bd