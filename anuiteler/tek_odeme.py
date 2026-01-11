"""
TEK BİR ÖDEMENİN GELECEK VE PEŞİN (BUGÜNKÜ) DEĞER HESAPLAMALARI

Temel Formüller:
- Gelecek Değer: GD = BD × (1+i)^t
- Peşin Değer: BD = GD × v^t  (v = 1/(1+i))
"""

import math


def bugunku_deger(gelecek_deger, i, t):
    if i <= -1:
        raise ValueError("Faiz oranı -1'den büyük olmalıdır.")
    if t < 0:
        raise ValueError("Dönem sayısı negatif olamaz.")
    
    v = 1 / (1 + i)
    return gelecek_deger * (v ** t)


def gelecek_deger(bugunku_deger, i, t):
    if i <= -1:
        raise ValueError("Faiz oranı -1'den büyük olmalıdır.")
    if t < 0:
        raise ValueError("Dönem sayısı negatif olamaz.")
    
    return bugunku_deger * ((1 + i) ** t)


def faiz_orani_hesapla(bugunku_deger, gelecek_deger, t):
    if bugunku_deger <= 0:
        raise ValueError("Bugünkü değer sıfırdan büyük olmalıdır.")
    if gelecek_deger <= 0:
        raise ValueError("Gelecek değer sıfırdan büyük olmalıdır.")
    if t <= 0:
        raise ValueError("Dönem sayısı sıfırdan büyük olmalıdır.")
    
    # GD/BD = (1+i)^t
    # i = (GD/BD)^(1/t) - 1
    return (gelecek_deger / bugunku_deger) ** (1 / t) - 1


def sure_hesapla(bugunku_deger, gelecek_deger, i):
    if bugunku_deger <= 0:
        raise ValueError("Bugünkü değer sıfırdan büyük olmalıdır.")
    if gelecek_deger <= 0:
        raise ValueError("Gelecek değer sıfırdan büyük olmalıdır.")
    if i <= -1:
        raise ValueError("Faiz oranı -1'den büyük olmalıdır.")
    if i == 0:
        raise ValueError("Faiz oranı sıfır olamaz (basit faizde süre tanımsızdır).")
    
    # GD/BD = (1+i)^t
    # t = log(GD/BD) / log(1+i)
    return math.log(gelecek_deger / bugunku_deger) / math.log(1 + i)


def iskonto_faktoru_hesapla(i, t=1):
    if i <= -1:
        raise ValueError("Faiz oranı -1'den büyük olmalıdır.")
    
    return (1 + i) ** (-t)


def birikim_faktoru_hesapla(i, t=1):
    if i <= -1:
        raise ValueError("Faiz oranı -1'den büyük olmalıdır.")
    
    return (1 + i) ** t