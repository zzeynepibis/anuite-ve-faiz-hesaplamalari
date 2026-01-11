"""
DEVRE SONU ÖDEMELİ ANÜİTELER (Ordinary Annuity)

Ödemeler her dönemin SONUNDA yapılır.

Temel Formüller:
- Bugünkü Değer: BD = a × [(1 - v^n) / i]  --> a(n,i)
- Gelecek Değer: GD = a × [(1+i)^n - 1] / i  --> s(n,i)

Burada:
- a: Her dönem yapılan ödeme tutarı
- n: Toplam dönem sayısı
- i: Dönemsel faiz oranı
- v: İskonto faktörü = 1/(1+i)
"""

import math


def pesin_deger_faktoru(i, n):
    """Peşin değer faktörü: a(n,i)"""
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    if n <= 0:
        raise ValueError("Dönem sayısı sıfırdan büyük olmalıdır.")
    
    v = 1 / (1 + i)
    return (1 - v**n) / i


def gelecek_deger_faktoru(i, n):
    """Gelecek değer faktörü: s(n,i)"""
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    if n <= 0:
        raise ValueError("Dönem sayısı sıfırdan büyük olmalıdır.")
    
    return ((1 + i)**n - 1) / i


# ============================================================
# BUGÜNKÜ DEĞER HESAPLAMALARI (BD = a × a(n,i))
# ============================================================

def bugunku_deger_hesapla(odeme, n, i):
    """BD = a × a(n,i)"""
    a_ni = pesin_deger_faktoru(i, n)
    return odeme * a_ni


def odeme_bugunku_degerden(bugunku_deger, n, i):
    """a = BD / a(n,i)"""
    a_ni = pesin_deger_faktoru(i, n)
    return bugunku_deger / a_ni


def sure_bugunku_degerden(bugunku_deger, odeme, i):
    """n hesaplama: BD/a = (1-v^n)/i"""
    if odeme <= 0:
        raise ValueError("Ödeme tutarı sıfırdan büyük olmalıdır.")
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    
    v = 1 / (1 + i)
    hedef = 1 - (i * bugunku_deger / odeme)
    
    if hedef <= 0:
        raise ValueError("Geçersiz parametre kombinasyonu: Çözüm mevcut değil.")
    
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
        
        f = a_ni - hedef
        
        if abs(f) < tolerans:
            return i
        
        # Türev: da/di
        da_di = (n * v**(n+1) / (1+i) - (1 - v**n) / (i**2)) / i
        
        i = i - f / da_di
        
        if i < 0.0001:
            i = 0.0001
    
    return i


# ============================================================
# GELECEK DEĞER HESAPLAMALARI (GD = a × s(n,i))
# ============================================================

def gelecek_deger_hesapla(odeme, n, i):
    """GD = a × s(n,i)"""
    s_ni = gelecek_deger_faktoru(i, n)
    return odeme * s_ni


def odeme_gelecek_degerden(gelecek_deger, n, i):
    """a = GD / s(n,i)"""
    s_ni = gelecek_deger_faktoru(i, n)
    return gelecek_deger / s_ni


def sure_gelecek_degerden(gelecek_deger, odeme, i):
    """n hesaplama: GD/a = [(1+i)^n - 1]/i"""
    if odeme <= 0:
        raise ValueError("Ödeme tutarı sıfırdan büyük olmalıdır.")
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    
    hedef = 1 + (i * gelecek_deger / odeme)
    
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
        
        f = s_ni - hedef
        
        if abs(f) < tolerans:
            return i
        
        # Türev: ds/di
        ds_di = (n * (1+i)**(n-1) / i - ((1+i)**n - 1) / i**2)
        
        i = i - f / ds_di
        
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
    """Amortisman tablosu oluşturur"""
    bd = bugunku_deger_hesapla(odeme, n, i)
    kalan = bd
    tablo = []
    
    for donem in range(1, n + 1):
        faiz = kalan * i
        anapara = odeme - faiz
        kalan = kalan - anapara
        
        tablo.append({
            'donem': donem,
            'odeme': odeme,
            'faiz': faiz,
            'anapara': anapara,
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
    """Ortalama vade (Macaulay duration benzeri)"""
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    
    v = 1 / (1 + i)
    bd = bugunku_deger_hesapla(odeme, n, i)
    
    agirlikli_toplam = sum(t * odeme * (v ** t) for t in range(1, n + 1))
    
    return agirlikli_toplam / bd