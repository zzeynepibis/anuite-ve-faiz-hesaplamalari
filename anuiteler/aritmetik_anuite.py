"""
ARİTMETİK DİZİ ŞEKLİNDE DEĞİŞEN TAKSİTLER (ANÜİTELER)

Taksitlerin değişimi: Taksitler devreden devreye değişim miktarı b olmak üzere;

1) DEVRE SONU ÖDEMELİ ARİTMETİK DİZİ
   Taksitler: a, a+b, a+2b, ..., a+(n-1)b
   
   Formül: BD = (a + b/i) × [(1+i)^n - 1] / i - b.n / i
   
   Alternatif: BD = a × [(1+i)^n - 1] / [(1+i)^n × i] + (b/i) × {[(1+i)^n - 1] / [(1+i)^n × i] - n/(1+i)^n}

2) DEVRE BAŞI ÖDEMELİ ARİTMETİK DİZİ
   Formül: BD = (1+i) × [(a + b/i) × [(1+i)^n - 1] / i - (1+i).b.n / i]
"""

import math


# ============================================================================
# DEVRE SONU ÖDEMELİ ARİTMETİK ANÜİTE
# ============================================================================

def bugunku_deger_devre_sonu(ilk_taksit, degisim, i, n):
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    if n <= 0:
        raise ValueError("Dönem sayısı sıfırdan büyük olmalıdır.")
    
    # BD = (a + b/i) × [(1+i)^n - 1] / i - b.n / i
    birinci_terim = (ilk_taksit + degisim / i) * ((1 + i) ** n - 1) / i
    ikinci_terim = (degisim * n) / i
    
    return birinci_terim - ikinci_terim


def gelecek_deger_devre_sonu(ilk_taksit, degisim, i, n):
    bd = bugunku_deger_devre_sonu(ilk_taksit, degisim, i, n)
    return bd * ((1 + i) ** n)


def ilk_taksit_hesapla_bd_devre_sonu(bugunku_deger, degisim, i, n):
    if bugunku_deger <= 0:
        raise ValueError("Bugünkü değer sıfırdan büyük olmalıdır.")
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    if n <= 0:
        raise ValueError("Dönem sayısı sıfırdan büyük olmalıdır.")
    
    sol = bugunku_deger + (degisim * n) / i
    carpan = i / ((1 + i) ** n - 1)
    
    return sol * carpan - degisim / i


def ilk_taksit_hesapla_gd_devre_sonu(gelecek_deger, degisim, i, n):
    if gelecek_deger <= 0:
        raise ValueError("Gelecek değer sıfırdan büyük olmalıdır.")
    
    bugunku_deger = gelecek_deger / ((1 + i) ** n)
    return ilk_taksit_hesapla_bd_devre_sonu(bugunku_deger, degisim, i, n)


def degisim_hesapla_bd_devre_sonu(bugunku_deger, ilk_taksit, i, n):
    if bugunku_deger <= 0:
        raise ValueError("Bugünkü değer sıfırdan büyük olmalıdır.")
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    if n <= 0:
        raise ValueError("Dönem sayısı sıfırdan büyük olmalıdır.")
    
    anuite_faktoru = ((1 + i) ** n - 1) / i
    sol = bugunku_deger - ilk_taksit * anuite_faktoru
    sag_parantez = anuite_faktoru - n
    
    if abs(sag_parantez) < 1e-10:
        raise ValueError("Geçersiz parametre kombinasyonu (bölme hatası).")
    
    return (sol * i) / sag_parantez


# ============================================================================
# DEVRE BAŞI ÖDEMELİ ARİTMETİK ANÜİTE
# ============================================================================

def bugunku_deger_devre_basi(ilk_taksit, degisim, i, n):
    if i <= 0:
        raise ValueError("Faiz oranı sıfırdan büyük olmalıdır.")
    if n <= 0:
        raise ValueError("Dönem sayısı sıfırdan büyük olmalıdır.")
    
    birinci_terim = (ilk_taksit + degisim / i) * ((1 + i) ** n - 1) / i
    ikinci_terim = ((1 + i) * degisim * n) / i
    
    return (1 + i) * (birinci_terim - ikinci_terim)


def gelecek_deger_devre_basi(ilk_taksit, degisim, i, n):
    bd = bugunku_deger_devre_basi(ilk_taksit, degisim, i, n)
    return bd * ((1 + i) ** n) / (1 + i)


def ilk_taksit_hesapla_bd_devre_basi(bugunku_deger, degisim, i, n):
    bd_devre_sonu = bugunku_deger / (1 + i)
    return ilk_taksit_hesapla_bd_devre_sonu(bd_devre_sonu, degisim, i, n)


# ============================================================================
# TERS FORMÜLLER (i VE n HESAPLAMA)
# ============================================================================

def faiz_orani_hesapla_bd(bugunku_deger, ilk_taksit, degisim, n, devre_basi=False, 
                          tahmin=0.1, tolerans=1e-6, maks_iterasyon=100):
    i = tahmin
    
    for _ in range(maks_iterasyon):
        if devre_basi:
            bd_hesaplanan = bugunku_deger_devre_basi(ilk_taksit, degisim, i, n)
        else:
            bd_hesaplanan = bugunku_deger_devre_sonu(ilk_taksit, degisim, i, n)
        
        f = bd_hesaplanan - bugunku_deger
        
        # Sayısal türev
        delta = 1e-8
        if devre_basi:
            bd_delta = bugunku_deger_devre_basi(ilk_taksit, degisim, i + delta, n)
        else:
            bd_delta = bugunku_deger_devre_sonu(ilk_taksit, degisim, i + delta, n)
        
        f_turev = (bd_delta - bd_hesaplanan) / delta
        
        if abs(f_turev) < 1e-10:
            raise ValueError("Türev sıfıra çok yakın, iterasyon durdu.")
        
        i_yeni = i - f / f_turev
        
        if i_yeni <= 0:
            i_yeni = 0.01
        
        if abs(i_yeni - i) < tolerans:
            return i_yeni
        
        i = i_yeni
    
    raise ValueError(f"Yakınsama sağlanamadı ({maks_iterasyon} iterasyonda).")


def sure_hesapla_bd(bugunku_deger, ilk_taksit, degisim, i, devre_basi=False,
                    tahmin=5, tolerans=1e-6, maks_iterasyon=100):
    n = tahmin
    
    for _ in range(maks_iterasyon):
        n_int = int(max(1, n))
        
        if devre_basi:
            bd_hesaplanan = bugunku_deger_devre_basi(ilk_taksit, degisim, i, n_int)
        else:
            bd_hesaplanan = bugunku_deger_devre_sonu(ilk_taksit, degisim, i, n_int)
        
        f = bd_hesaplanan - bugunku_deger
        
        # Sayısal türev
        delta = 0.1
        n_delta = int(max(1, n + delta))
        
        if devre_basi:
            bd_delta = bugunku_deger_devre_basi(ilk_taksit, degisim, i, n_delta)
        else:
            bd_delta = bugunku_deger_devre_sonu(ilk_taksit, degisim, i, n_delta)
        
        f_turev = (bd_delta - bd_hesaplanan) / delta
        
        if abs(f_turev) < 1e-10:
            raise ValueError("Türev sıfıra çok yakın, iterasyon durdu.")
        
        n_yeni = n - f / f_turev
        
        if n_yeni < 1:
            n_yeni = 1
        
        if abs(n_yeni - n) < tolerans:
            return n_yeni
        
        n = n_yeni
    
    raise ValueError(f"Yakınsama sağlanamadı ({maks_iterasyon} iterasyonda).")


# ============================================================================
# GERİYE UYUMLULUK İÇİN EKSİK FONKSİYONLAR
# ============================================================================

# Genel fonksiyonlar (otomatik devre_basi parametresi ile)
def bugunku_deger(ilk_taksit, degisim, i, n, devre_basi=False):
    """Genel bugünkü değer hesaplama (devre sonu/başı otomatik)"""
    if devre_basi:
        return bugunku_deger_devre_basi(ilk_taksit, degisim, i, n)
    return bugunku_deger_devre_sonu(ilk_taksit, degisim, i, n)


def gelecek_deger(ilk_taksit, degisim, i, n, devre_basi=False):
    """Genel gelecek değer hesaplama (devre sonu/başı otomatik)"""
    if devre_basi:
        return gelecek_deger_devre_basi(ilk_taksit, degisim, i, n)
    return gelecek_deger_devre_sonu(ilk_taksit, degisim, i, n)


def ilk_taksit_hesapla_bd(bugunku_deger, degisim, i, n, devre_basi=False):
    """Genel ilk taksit hesaplama (BD'den)"""
    if devre_basi:
        return ilk_taksit_hesapla_bd_devre_basi(bugunku_deger, degisim, i, n)
    return ilk_taksit_hesapla_bd_devre_sonu(bugunku_deger, degisim, i, n)


def ilk_taksit_hesapla_gd(gelecek_deger, degisim, i, n, devre_basi=False):
    """Genel ilk taksit hesaplama (GD'den)"""
    return ilk_taksit_hesapla_gd_devre_sonu(gelecek_deger, degisim, i, n)


def degisim_hesapla_bd(bugunku_deger, ilk_taksit, i, n, devre_basi=False):
    """Genel değişim hesaplama"""
    return degisim_hesapla_bd_devre_sonu(bugunku_deger, ilk_taksit, i, n)