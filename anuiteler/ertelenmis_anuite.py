"""
ERTELENMİŞ (GECİKTİRİLMİŞ) ANÜİTE HESAPLAMALARI
1) DEVRE SONU ÖDEMELİ ERTELENMİŞ ANÜİTE:
   - m dönem sonra n taksit ödenecek
   - Taksitler m+1, m+2, ..., m+n noktalarında
   
   BD = a × [(1+i)^n - 1] / [(1+i)^(n+m) × i]
   
   Alternatif: BD = a × v^m × [(1+i)^n - 1] / [(1+i)^n × i]
   
   GD = a × [(1+i)^n - 1] / i  (Normal anüite ile aynı)

2) DEVRE BAŞI ÖDEMELİ ERTELENMİŞ ANÜİTE:
   - m dönem sonra n taksit ödenecek
   - Taksitler m, m+1, ..., m+n-1 noktalarında
   
   BD = a × (1+i) × [(1+i)^n - 1] / [(1+i)^(n+m) × i]
   BD = a × [(1+i)^n - 1] / [(1+i)^(n+m-1) × i]

ÇABUKLAŞTIRILMIŞ ERTELENMİŞ ANÜİTE:Hem gecikme (m) hem de çabuklaştırma (c) süresi vardır.
   BD = a × (1+i)^c × [(1+i)^n - 1] / [(1+i)^(n+m) × i]
"""

import math


# ============================================================================
# DEVRE SONU ÖDEMELİ ERTELENMİŞ ANÜİTE
# ============================================================================

def bugunku_deger_devre_sonu(taksit, i, n, m):
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    if n <= 0:
        raise ValueError("Taksit sayısı sıfırdan büyük olmalıdır.")
    if m < 0:
        raise ValueError("Gecikme süresi negatif olamaz.")
    if taksit < 0:
        raise ValueError("Taksit tutarı negatif olamaz.")
    
    pay = (1 + i) ** n - 1
    payda = ((1 + i) ** (n + m)) * i
    
    return taksit * (pay / payda)


def gelecek_deger_devre_sonu(taksit, i, n, m):
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    if n <= 0:
        raise ValueError("Taksit sayısı sıfırdan büyük olmalıdır.")
    
    # Erteleme GD'yi etkilemez, sadece BD'yi etkiler
    return taksit * ((1 + i) ** n - 1) / i


def taksit_hesapla_bd_devre_sonu(bugunku_deger, i, n, m):
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    if n <= 0:
        raise ValueError("Taksit sayısı sıfırdan büyük olmalıdır.")
    if m < 0:
        raise ValueError("Gecikme süresi negatif olamaz.")
    if bugunku_deger < 0:
        raise ValueError("Bugünkü değer negatif olamaz.")
    
    payda = (1 + i) ** n - 1
    pay = ((1 + i) ** (n + m)) * i
    
    return bugunku_deger * (pay / payda)


def taksit_hesapla_gd_devre_sonu(gelecek_deger, i, n):
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    if n <= 0:
        raise ValueError("Taksit sayısı sıfırdan büyük olmalıdır.")
    if gelecek_deger < 0:
        raise ValueError("Gelecek değer negatif olamaz.")
    
    return gelecek_deger * i / ((1 + i) ** n - 1)


# ============================================================================
# DEVRE BAŞI ÖDEMELİ ERTELENMİŞ ANÜİTE
# ============================================================================

def bugunku_deger_devre_basi(taksit, i, n, m):
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    if n <= 0:
        raise ValueError("Taksit sayısı sıfırdan büyük olmalıdır.")
    if m < 0:
        raise ValueError("Gecikme süresi negatif olamaz.")
    if taksit < 0:
        raise ValueError("Taksit tutarı negatif olamaz.")
    
    # Yöntem 1: Devre sonu × (1+i)
    bd_devre_sonu = bugunku_deger_devre_sonu(taksit, i, n, m)
    return bd_devre_sonu * (1 + i)
    
    # Yöntem 2 (alternatif):
    # pay = (1 + i) ** n - 1
    # payda = ((1 + i) ** (n + m - 1)) * i
    # return taksit * (pay / payda)


def gelecek_deger_devre_basi(taksit, i, n):
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    if n <= 0:
        raise ValueError("Taksit sayısı sıfırdan büyük olmalıdır.")
    
    return taksit * (1 + i) * ((1 + i) ** n - 1) / i


def taksit_hesapla_bd_devre_basi(bugunku_deger, i, n, m):
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    if n <= 0:
        raise ValueError("Taksit sayısı sıfırdan büyük olmalıdır.")
    if m < 0:
        raise ValueError("Gecikme süresi negatif olamaz.")
    if bugunku_deger < 0:
        raise ValueError("Bugünkü değer negatif olamaz.")
    
    # BD_devre_başı = BD_devre_sonu × (1+i)
    bd_devre_sonu = bugunku_deger / (1 + i)
    return taksit_hesapla_bd_devre_sonu(bd_devre_sonu, i, n, m)


# ============================================================================
# ÇABUKLAŞTIRILMIŞ ERTELENMİŞ ANÜİTE
# ============================================================================

def bugunku_deger_cabuklas_ertelenmis(taksit, i, n, m, c):
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    if n <= 0:
        raise ValueError("Taksit sayısı sıfırdan büyük olmalıdır.")
    if m < 0:
        raise ValueError("Gecikme süresi negatif olamaz.")
    if c < 0:
        raise ValueError("Çabuklaştırma süresi negatif olamaz.")
    
    bd_ertekenmis = bugunku_deger_devre_sonu(taksit, i, n, m)
    return bd_ertekenmis * ((1 + i) ** c)


# ============================================================================
# TERS FORMÜLLER (i, n, m HESAPLAMA)
# ============================================================================

def gecikme_suresi_hesapla_bd(bugunku_deger, taksit, i, n, devre_basi=False):
    if taksit <= 0:
        raise ValueError("Taksit tutarı sıfırdan büyük olmalıdır.")
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    if n <= 0:
        raise ValueError("Taksit sayısı sıfırdan büyük olmalıdır.")
    if bugunku_deger <= 0:
        raise ValueError("Bugünkü değer sıfırdan büyük olmalıdır.")
    
    if devre_basi:
        bugunku_deger = bugunku_deger / (1 + i)
    
    pay = taksit * ((1 + i) ** n - 1)
    payda = bugunku_deger * i
    
    if payda <= 0:
        raise ValueError("Geçersiz parametre kombinasyonu.")
    
    n_plus_m = math.log(pay / payda) / math.log(1 + i)
    m = n_plus_m - n
    
    if m < 0:
        raise ValueError("Hesaplanan gecikme süresi negatif (geçersiz parametre).")
    
    return m


def faiz_orani_hesapla_bd(bugunku_deger, taksit, n, m, devre_basi=False,
                          tahmin=0.1, tolerans=1e-6, maks_iterasyon=100):
    if taksit <= 0:
        raise ValueError("Taksit tutarı sıfırdan büyük olmalıdır.")
    if n <= 0:
        raise ValueError("Taksit sayısı sıfırdan büyük olmalıdır.")
    if m < 0:
        raise ValueError("Gecikme süresi negatif olamaz.")
    if bugunku_deger <= 0:
        raise ValueError("Bugünkü değer sıfırdan büyük olmalıdır.")
    
    i = tahmin
    
    for _ in range(maks_iterasyon):
        if devre_basi:
            bd_hesaplanan = bugunku_deger_devre_basi(taksit, i, n, m)
        else:
            bd_hesaplanan = bugunku_deger_devre_sonu(taksit, i, n, m)
        
        f = bd_hesaplanan - bugunku_deger
        
        # Sayısal türev
        delta = 1e-8
        if devre_basi:
            bd_delta = bugunku_deger_devre_basi(taksit, i + delta, n, m)
        else:
            bd_delta = bugunku_deger_devre_sonu(taksit, i + delta, n, m)
        
        f_turev = (bd_delta - bd_hesaplanan) / delta
        
        if abs(f_turev) < 1e-10:
            raise ValueError("Türev sıfıra çok yakın.")
        
        i_yeni = i - f / f_turev
        
        if i_yeni <= 0:
            i_yeni = 0.01
        
        if abs(i_yeni - i) < tolerans:
            return i_yeni
        
        i = i_yeni
    
    raise ValueError(f"Yakınsama sağlanamadı ({maks_iterasyon} iterasyonda).")


def sure_hesapla_bd(bugunku_deger, taksit, i, m, devre_basi=False,
                    tahmin=5, tolerans=1e-6, maks_iterasyon=100):
    n = tahmin
    
    for _ in range(maks_iterasyon):
        n_int = int(max(1, n))
        
        if devre_basi:
            bd_hesaplanan = bugunku_deger_devre_basi(taksit, i, n_int, m)
        else:
            bd_hesaplanan = bugunku_deger_devre_sonu(taksit, i, n_int, m)
        
        f = bd_hesaplanan - bugunku_deger
        
        # Sayısal türev
        delta = 0.1
        n_delta = int(max(1, n + delta))
        
        if devre_basi:
            bd_delta = bugunku_deger_devre_basi(taksit, i, n_delta, m)
        else:
            bd_delta = bugunku_deger_devre_sonu(taksit, i, n_delta, m)
        
        f_turev = (bd_delta - bd_hesaplanan) / delta
        
        if abs(f_turev) < 1e-10:
            raise ValueError("Türev sıfıra çok yakın.")
        
        n_yeni = n - f / f_turev
        
        if n_yeni < 1:
            n_yeni = 1
        
        if abs(n_yeni - n) < tolerans:
            return n_yeni
        
        n = n_yeni
    
    raise ValueError(f"Yakınsama sağlanamadı ({maks_iterasyon} iterasyonda).")


# ============================================================================
# GERİYE UYUMLULUK FONKSİYONLARI
# ============================================================================

def bugunku_deger(taksit, i, n, m, devre_basi=False):
    """Genel bugünkü değer hesaplama (devre sonu/başı otomatik)"""
    if devre_basi:
        return bugunku_deger_devre_basi(taksit, i, n, m)
    return bugunku_deger_devre_sonu(taksit, i, n, m)


def gelecek_deger(taksit, i, n, devre_basi=False):
    """Genel gelecek değer hesaplama (erteleme GD'yi etkilemez)"""
    if devre_basi:
        return gelecek_deger_devre_basi(taksit, i, n)
    return gelecek_deger_devre_sonu(taksit, i, n, m=0)


def taksit_hesapla_bd(bugunku_deger, i, n, m, devre_basi=False):
    """Genel taksit hesaplama (BD'den)"""
    if devre_basi:
        return taksit_hesapla_bd_devre_basi(bugunku_deger, i, n, m)
    return taksit_hesapla_bd_devre_sonu(bugunku_deger, i, n, m)