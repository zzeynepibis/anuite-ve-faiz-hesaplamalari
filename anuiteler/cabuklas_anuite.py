"""
ÇABUKLAŞTIRILMIŞ ANÜİTE HESAPLAMALARI

Temel Formüller:
- Devre Sonu Ödemeli: BD = a × (1+i)^c × [(1+i)^n - 1] / [(1+i)^n × i]
- Devre Başı Ödemeli: BD = a × (1+i)^(c+1) × [(1+i)^n - 1] / [(1+i)^n × i]

Not: c = çabuklaştırma süresi (gecikme süresi)
"""

import math


def bugunku_deger_devre_sonu(taksit, i, n, c):
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    if n <= 0:
        raise ValueError("Dönem sayısı sıfırdan büyük olmalıdır.")
    if c < 0:
        raise ValueError("Çabuklaştırma süresi negatif olamaz.")
    if taksit < 0:
        raise ValueError("Taksit tutarı negatif olamaz.")
    
    # Normal devre sonu anüite × (1+i)^c
    anuite_faktoru = ((1 + i) ** n - 1) / (((1 + i) ** n) * i)
    cabuklas_faktoru = (1 + i) ** c
    
    return taksit * cabuklas_faktoru * anuite_faktoru


def gelecek_deger_devre_sonu(taksit, i, n, c):
    bd = bugunku_deger_devre_sonu(taksit, i, n, c)
    return bd * ((1 + i) ** n)


def bugunku_deger_devre_basi(taksit, i, n, c):
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    if n <= 0:
        raise ValueError("Dönem sayısı sıfırdan büyük olmalıdır.")
    if c < 0:
        raise ValueError("Çabuklaştırma süresi negatif olamaz.")
    if taksit < 0:
        raise ValueError("Taksit tutarı negatif olamaz.")
    
    # Devre sonu × (1+i)
    bd_devre_sonu = bugunku_deger_devre_sonu(taksit, i, n, c)
    return bd_devre_sonu * (1 + i)


def gelecek_deger_devre_basi(taksit, i, n, c):
    bd = bugunku_deger_devre_basi(taksit, i, n, c)
    return bd * ((1 + i) ** n) / (1 + i)


def taksit_hesapla_bd(bugunku_deger, i, n, c, devre_basi=False):
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    if n <= 0:
        raise ValueError("Dönem sayısı sıfırdan büyük olmalıdır.")
    if c < 0:
        raise ValueError("Çabuklaştırma süresi negatif olamaz.")
    if bugunku_deger < 0:
        raise ValueError("Bugünkü değer negatif olamaz.")
    
    anuite_faktoru = ((1 + i) ** n - 1) / (((1 + i) ** n) * i)
    cabuklas_faktoru = (1 + i) ** c
    
    if devre_basi:
        cabuklas_faktoru *= (1 + i)
    
    return bugunku_deger / (cabuklas_faktoru * anuite_faktoru)


def taksit_hesapla_gd(gelecek_deger, i, n, c, devre_basi=False):
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    if n <= 0:
        raise ValueError("Dönem sayısı sıfırdan büyük olmalıdır.")
    if c < 0:
        raise ValueError("Çabuklaştırma süresi negatif olamaz.")
    if gelecek_deger < 0:
        raise ValueError("Gelecek değer negatif olamaz.")
    
    bugunku_deger = gelecek_deger / ((1 + i) ** n)
    return taksit_hesapla_bd(bugunku_deger, i, n, c, devre_basi)


def cabuklas_suresi_hesapla_bd(bugunku_deger, taksit, i, n, devre_basi=False):
    if taksit <= 0:
        raise ValueError("Taksit tutarı sıfırdan büyük olmalıdır.")
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    if n <= 0:
        raise ValueError("Dönem sayısı sıfırdan büyük olmalıdır.")
    if bugunku_deger <= 0:
        raise ValueError("Bugünkü değer sıfırdan büyük olmalıdır.")
    
    anuite_faktoru = ((1 + i) ** n - 1) / (((1 + i) ** n) * i)
    
    if devre_basi:
        # BD / (a × (1+i) × anuite_faktoru) = (1+i)^c
        carpan = taksit * (1 + i) * anuite_faktoru
    else:
        # BD / (a × anuite_faktoru) = (1+i)^c
        carpan = taksit * anuite_faktoru
    
    if carpan <= 0:
        raise ValueError("Geçersiz parametre kombinasyonu.")
    
    # (1+i)^c = BD / carpan
    # c = log(BD / carpan) / log(1+i)
    return math.log(bugunku_deger / carpan) / math.log(1 + i)


def faiz_orani_hesapla_bd(bugunku_deger, taksit, n, c, tahmin=0.1, tolerans=1e-6, maks_iterasyon=100):
    if taksit <= 0:
        raise ValueError("Taksit tutarı sıfırdan büyük olmalıdır.")
    if n <= 0:
        raise ValueError("Dönem sayısı sıfırdan büyük olmalıdır.")
    if c < 0:
        raise ValueError("Çabuklaştırma süresi negatif olamaz.")
    if bugunku_deger <= 0:
        raise ValueError("Bugünkü değer sıfırdan büyük olmalıdır.")
    
    i = tahmin
    
    for _ in range(maks_iterasyon):
        bd_hesaplanan = bugunku_deger_devre_sonu(taksit, i, n, c)
        f = bd_hesaplanan - bugunku_deger
        
        # Sayısal türev
        delta = 1e-8
        bd_delta = bugunku_deger_devre_sonu(taksit, i + delta, n, c)
        f_turev = (bd_delta - bd_hesaplanan) / delta
        
        i_yeni = i - f / f_turev
        
        if i_yeni <= 0:
            i_yeni = 0.01
        
        if abs(i_yeni - i) < tolerans:
            return i_yeni
        
        i = i_yeni
    
    raise ValueError(f"Yakınsama sağlanamadı ({maks_iterasyon} iterasyonda).")


def sure_hesapla_bd(bugunku_deger, taksit, i, c, tahmin=5, tolerans=1e-6, maks_iterasyon=100):
    n = tahmin
    
    for _ in range(maks_iterasyon):
        bd_hesaplanan = bugunku_deger_devre_sonu(taksit, i, int(n), c)
        f = bd_hesaplanan - bugunku_deger
        
        # Sayısal türev
        delta = 0.1
        bd_delta = bugunku_deger_devre_sonu(taksit, i, int(n + delta), c)
        f_turev = (bd_delta - bd_hesaplanan) / delta
        
        n_yeni = n - f / f_turev
        
        if n_yeni < 1:
            n_yeni = 1
        
        if abs(n_yeni - n) < tolerans:
            return n_yeni
        
        n = n_yeni
    
    raise ValueError(f"Yakınsama sağlanamadı ({maks_iterasyon} iterasyonda).")