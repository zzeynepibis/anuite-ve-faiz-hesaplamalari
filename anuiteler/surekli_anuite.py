"""
SÜREKLİ ANÜİTELER (Perpetuity / Continuous Annuity)

n → ∞ durumu: Ödemeler sonsuza kadar devam eder

Temel Formüller:
- Devre Sonu Sürekli: BD = a / i
- Devre Başı Sürekli: BD = a × (1+i) / i = a / i + a
"""

import math


# ============================================================
# DEVRE SONU SÜREKLİ ANÜİTE
# ============================================================

def bugunku_deger_devre_sonu(odeme, i):
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    
    return odeme / i


def odeme_devre_sonu(bugunku_deger, i):
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    
    return bugunku_deger * i


def faiz_devre_sonu(bugunku_deger, odeme):
    if bugunku_deger <= 0:
        raise ValueError("Bugünkü değer sıfırdan büyük olmalıdır.")
    
    return odeme / bugunku_deger


# ============================================================
# DEVRE BAŞI SÜREKLİ ANÜİTE
# ============================================================

def bugunku_deger_devre_basi(odeme, i):
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    
    return odeme * (1 + i) / i


def odeme_devre_basi(bugunku_deger, i):
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    
    return bugunku_deger * i / (1 + i)


def faiz_devre_basi(bugunku_deger, odeme):
    if bugunku_deger <= odeme:
        raise ValueError("Bugünkü değer ödemeden büyük olmalıdır.")
    
    return odeme / (bugunku_deger - odeme)


# ============================================================
# ERTELENMİŞ SÜREKLİ ANÜİTE
# ============================================================

def ertelenmis_surekli_anuite(odeme, i, erteleme_suresi):
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    if erteleme_suresi < 0:
        raise ValueError("Erteleme süresi negatif olamaz.")
    
    bd_surekli = odeme / i
    v = 1 / (1 + i)
    
    return bd_surekli * (v ** erteleme_suresi)