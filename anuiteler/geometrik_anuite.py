"""
GEOMETRİK DİZİ ŞEKLİNDE DEĞİŞEN TAKSİTLER (ANÜİTELER)

Geometrik Dizi Formülleri:
- i = r durumunda: BD = n.a.(1+i)^(n-1)  veya  GD = n.a
- i ≠ r durumunda: 
  * BD = a.(1+i)^n × [(1+i)^n - (1+r)^n] / [(1+i)^n × (i-r)]
  * GD = a × [(1+i)^n - (1+r)^n] / (i-r)
"""

import math


def bugunku_deger_devre_sonu(ilk_taksit, i, r, n):
    if n <= 0:
        raise ValueError("Dönem sayısı sıfırdan büyük olmalıdır.")
    if ilk_taksit < 0:
        raise ValueError("İlk taksit negatif olamaz.")
    
    # i = r özel durumu
    if abs(i - r) < 1e-10:
        return n * ilk_taksit * ((1 + i) ** (n - 1))
    
    # Genel durum: i ≠ r
    if i <= -1:
        raise ValueError("Faiz oranı -1'den büyük olmalıdır.")
    
    pay = (1 + i) ** n - (1 + r) ** n
    payda = ((1 + i) ** n) * (i - r)
    
    return ilk_taksit * ((1 + i) ** n) * (pay / payda)


def gelecek_deger_devre_sonu(ilk_taksit, i, r, n):
    if n <= 0:
        raise ValueError("Dönem sayısı sıfırdan büyük olmalıdır.")
    if ilk_taksit < 0:
        raise ValueError("İlk taksit negatif olamaz.")
    
    # i = r özel durumu
    if abs(i - r) < 1e-10:
        return n * ilk_taksit
    
    # Genel durum: i ≠ r
    if i <= -1:
        raise ValueError("Faiz oranı -1'den büyük olmalıdır.")
    
    pay = (1 + i) ** n - (1 + r) ** n
    payda = i - r
    
    return ilk_taksit * (pay / payda)


def bugunku_deger_devre_basi(ilk_taksit, i, r, n):
    bd_devre_sonu = bugunku_deger_devre_sonu(ilk_taksit, i, r, n)
    return bd_devre_sonu * (1 + i)


def gelecek_deger_devre_basi(ilk_taksit, i, r, n):
    gd_devre_sonu = gelecek_deger_devre_sonu(ilk_taksit, i, r, n)
    return gd_devre_sonu * (1 + i)


def ilk_taksit_hesapla_bd(bugunku_deger, i, r, n, devre_basi=False):
    if bugunku_deger <= 0:
        raise ValueError("Bugünkü değer sıfırdan büyük olmalıdır.")
    if n <= 0:
        raise ValueError("Dönem sayısı sıfırdan büyük olmalıdır.")
    
    if devre_basi:
        bugunku_deger = bugunku_deger / (1 + i)
    
    # i = r özel durumu
    if abs(i - r) < 1e-10:
        return bugunku_deger / (n * ((1 + i) ** (n - 1)))
    
    # Genel durum
    pay = ((1 + i) ** n) * (i - r)
    payda = ((1 + i) ** n) * (((1 + i) ** n - (1 + r) ** n))
    
    return bugunku_deger * (pay / payda)


def ilk_taksit_hesapla_gd(gelecek_deger, i, r, n, devre_basi=False):
    if gelecek_deger <= 0:
        raise ValueError("Gelecek değer sıfırdan büyük olmalıdır.")
    if n <= 0:
        raise ValueError("Dönem sayısı sıfırdan büyük olmalıdır.")
    
    if devre_basi:
        gelecek_deger = gelecek_deger / (1 + i)
    
    # i = r özel durumu
    if abs(i - r) < 1e-10:
        return gelecek_deger / n
    
    # Genel durum
    payda = (1 + i) ** n - (1 + r) ** n
    pay = i - r
    
    return gelecek_deger * pay / payda


def faiz_orani_hesapla_bd(bugunku_deger, ilk_taksit, r, n, tahmin=0.1, tolerans=1e-6, maks_iterasyon=100):
    i = tahmin
    
    for _ in range(maks_iterasyon):
        # i = r kontrolü
        if abs(i - r) < 1e-10:
            i = r + 0.01  # r'den uzaklaştır
        
        bd_hesaplanan = bugunku_deger_devre_sonu(ilk_taksit, i, r, n)
        f = bd_hesaplanan - bugunku_deger
        
        # Sayısal türev
        delta = 1e-8
        bd_delta = bugunku_deger_devre_sonu(ilk_taksit, i + delta, r, n)
        f_turev = (bd_delta - bd_hesaplanan) / delta
        
        i_yeni = i - f / f_turev
        
        if abs(i_yeni - i) < tolerans:
            return i_yeni
        
        i = i_yeni
    
    raise ValueError(f"Yakınsama sağlanamadı ({maks_iterasyon} iterasyonda).")


def sure_hesapla_gd(gelecek_deger, ilk_taksit, i, r, tahmin=5, tolerans=1e-6, maks_iterasyon=100):
    n = tahmin
    
    for _ in range(maks_iterasyon):
        gd_hesaplanan = gelecek_deger_devre_sonu(ilk_taksit, i, r, int(n))
        f = gd_hesaplanan - gelecek_deger
        
        # Sayısal türev
        delta = 0.1
        gd_delta = gelecek_deger_devre_sonu(ilk_taksit, i, r, int(n + delta))
        f_turev = (gd_delta - gd_hesaplanan) / delta
        
        n_yeni = n - f / f_turev
        
        if n_yeni < 1:
            n_yeni = 1
        
        if abs(n_yeni - n) < tolerans:
            return n_yeni
        
        n = n_yeni
    
    raise ValueError(f"Yakınsama sağlanamadı ({maks_iterasyon} iterasyonda).")