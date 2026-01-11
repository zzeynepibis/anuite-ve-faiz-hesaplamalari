"""
YARDIMCI FONKSİYONLAR

Efektif/nominal faiz oranları, sürekli faiz oranları, iskonto hesaplamaları,
duration, convexity ve diğer yardımcı hesaplamalar
"""

import math


# ============================================================
# FAİZ ORANI ÇEVRİMLERİ
# ============================================================

def efektif_faiz_orani(nominal_oran, m):
    """
    Nominal oranı efektif orana çevirir
    
    Args:
        nominal_oran: Nominal yıllık faiz oranı
        m: Yıl içindeki bileşik dönem sayısı
    
    Returns:
        Efektif yıllık faiz oranı
    """
    if m <= 0:
        raise ValueError("Bileşik dönem sayısı sıfırdan büyük olmalıdır.")
    
    return (1 + nominal_oran / m) ** m - 1


def nominal_faiz_orani(efektif_oran, m):
    """
    Efektif oranı nominal orana çevirir
    
    Args:
        efektif_oran: Efektif yıllık faiz oranı
        m: Yıl içindeki bileşik dönem sayısı
    
    Returns:
        Nominal yıllık faiz oranı
    """
    if m <= 0:
        raise ValueError("Bileşik dönem sayısı sıfırdan büyük olmalıdır.")
    if efektif_oran <= -1:
        raise ValueError("Efektif oran -1'den büyük olmalıdır.")
    
    return m * ((1 + efektif_oran) ** (1 / m) - 1)


def surekli_faiz_orani(efektif_oran):
    """
    Efektif oranı sürekli faiz oranına (δ) çevirir
    Force of interest
    
    Args:
        efektif_oran: Efektif yıllık faiz oranı
    
    Returns:
        Sürekli faiz oranı (δ)
    """
    if efektif_oran <= -1:
        raise ValueError("Efektif oran -1'den büyük olmalıdır.")
    
    return math.log(1 + efektif_oran)


def efektif_from_surekli(delta):
    """
    Sürekli faiz oranını (δ) efektif orana çevirir
    
    Args:
        delta: Sürekli faiz oranı
    
    Returns:
        Efektif yıllık faiz oranı
    """
    return math.exp(delta) - 1


# ============================================================
# İSKONTO ORANLARI
# ============================================================

def faizden_iskonto_orani(i):
    """
    Faiz oranından iskonto oranı hesaplar: d = i/(1+i)
    
    Args:
        i: Faiz oranı
    
    Returns:
        İskonto oranı
    """
    if i <= -1:
        raise ValueError("Faiz oranı -1'den büyük olmalıdır.")
    
    return i / (1 + i)


def iskontodan_faiz_orani(d):
    """
    İskonto oranından faiz oranı hesaplar: i = d/(1-d)
    
    Args:
        d: İskonto oranı
    
    Returns:
        Faiz oranı
    """
    if d >= 1:
        raise ValueError("İskonto oranı 1'den küçük olmalıdır.")
    if d < 0:
        raise ValueError("İskonto oranı negatif olamaz.")
    
    return d / (1 - d)


def bileşik_iskonto_orani(nominal_iskonto, m):
    """
    Nominal iskonto oranını efektif iskonto oranına çevirir
    
    Args:
        nominal_iskonto: Nominal yıllık iskonto oranı
        m: Yıl içindeki bileşik dönem sayısı
    
    Returns:
        Efektif yıllık iskonto oranı
    """
    if m <= 0:
        raise ValueError("Bileşik dönem sayısı sıfırdan büyük olmalıdır.")
    if nominal_iskonto >= m:
        raise ValueError("Nominal iskonto oranı geçersiz.")
    
    return 1 - (1 - nominal_iskonto / m) ** m


# ============================================================
# FAKTÖR HESAPLAMALARI
# ============================================================

def iskonto_faktoru(i, n=1):
    """
    İskonto faktörü: v^n = (1+i)^(-n)
    
    Args:
        i: Faiz oranı
        n: Dönem sayısı
    
    Returns:
        İskonto faktörü
    """
    if i <= -1:
        raise ValueError("Faiz oranı -1'den büyük olmalıdır.")
    
    return (1 + i) ** (-n)


def birikim_faktoru(i, n=1):
    """
    Birikim faktörü: (1+i)^n
    
    Args:
        i: Faiz oranı
        n: Dönem sayısı
    
    Returns:
        Birikim faktörü
    """
    if i <= -1:
        raise ValueError("Faiz oranı -1'den büyük olmalıdır.")
    
    return (1 + i) ** n


# ============================================================
# TOPLAM HESAPLAMALAR
# ============================================================

def toplam_odeme_hesapla(odeme, n):
    """
    Toplam ödenen tutar
    
    Args:
        odeme: Dönemsel ödeme
        n: Dönem sayısı
    
    Returns:
        Toplam ödeme
    """
    return odeme * n


def toplam_faiz_hesapla(odeme, n, bugunku_deger):
    """
    Toplam ödenen faiz
    
    Args:
        odeme: Dönemsel ödeme
        n: Dönem sayısı
        bugunku_deger: Başlangıç borcu
    
    Returns:
        Toplam faiz
    """
    toplam_odeme = toplam_odeme_hesapla(odeme, n)
    return toplam_odeme - bugunku_deger


def ortalama_vade_hesapla(odemeler, faiz_orani):
    """
    Ortalama vade hesaplama (Macaulay Duration benzeri)
    
    Args:
        odemeler: [(dönem, tutar), ...] şeklinde liste
        faiz_orani: Dönemsel faiz oranı
    
    Returns:
        Ağırlıklı ortalama vade
    """
    if faiz_orani <= -1:
        raise ValueError("Faiz oranı -1'den büyük olmalıdır.")
    
    v = 1 / (1 + faiz_orani)
    
    bugunku_deger = sum(tutar * (v ** donem) for donem, tutar in odemeler)
    agirlikli_toplam = sum(donem * tutar * (v ** donem) for donem, tutar in odemeler)
    
    if bugunku_deger == 0:
        raise ValueError("Bugünkü değer sıfır olamaz.")
    
    return agirlikli_toplam / bugunku_deger


# ============================================================
# ENFLASYON DÜZELTMELERİ
# ============================================================

def reel_faiz_orani(nominal_oran, enflasyon_orani):
    """
    Reel faiz oranı hesaplar (Fisher denklemi)
    
    Args:
        nominal_oran: Nominal faiz oranı
        enflasyon_orani: Enflasyon oranı
    
    Returns:
        Reel faiz oranı
    """
    if enflasyon_orani <= -1:
        raise ValueError("Enflasyon oranı -1'den büyük olmalıdır.")
    
    return (1 + nominal_oran) / (1 + enflasyon_orani) - 1


def nominal_from_reel(reel_oran, enflasyon_orani):
    """
    Reel orandan nominal oran hesaplar
    
    Args:
        reel_oran: Reel faiz oranı
        enflasyon_orani: Enflasyon oranı
    
    Returns:
        Nominal faiz oranı
    """
    if reel_oran <= -1:
        raise ValueError("Reel oran -1'den büyük olmalıdır.")
    
    return (1 + reel_oran) * (1 + enflasyon_orani) - 1


# ============================================================
# ZAMAN ÇEVRİMLERİ
# ============================================================

def yillik_aylik_cevir(yillik_oran):
    """Yıllık faiz oranını aylığa çevirir"""
    return (1 + yillik_oran) ** (1/12) - 1


def aylik_yillik_cevir(aylik_oran):
    """Aylık faiz oranını yıllığa çevirir"""
    return (1 + aylik_oran) ** 12 - 1


def gunluk_yillik_cevir(gunluk_oran):
    """Günlük faiz oranını yıllığa çevirir (365 gün)"""
    return (1 + gunluk_oran) ** 365 - 1


def yillik_gunluk_cevir(yillik_oran):
    """Yıllık faiz oranını günlüğe çevirir (365 gün)"""
    return (1 + yillik_oran) ** (1/365) - 1


def ceyreklik_yillik_cevir(ceyreklik_oran):
    """Çeyreklik faiz oranını yıllığa çevirir"""
    return (1 + ceyreklik_oran) ** 4 - 1


def yillik_ceyreklik_cevir(yillik_oran):
    """Yıllık faiz oranını çeyrekliğe çevirir"""
    return (1 + yillik_oran) ** (1/4) - 1


# ============================================================
# DURATION VE CONVEXITY
# ============================================================

def macaulay_duration(nakit_akislari, faiz_orani):
    """
    Macaulay Duration hesaplar
    
    Args:
        nakit_akislari: [(dönem, tutar), ...] şeklinde liste
        faiz_orani: Dönemsel faiz oranı
    
    Returns:
        Macaulay Duration
    """
    if faiz_orani <= -1:
        raise ValueError("Faiz oranı -1'den büyük olmalıdır.")
    
    v = 1 / (1 + faiz_orani)
    
    bd = sum(tutar * (v ** donem) for donem, tutar in nakit_akislari)
    agirlikli_toplam = sum(donem * tutar * (v ** donem) for donem, tutar in nakit_akislari)
    
    if bd == 0:
        raise ValueError("Bugünkü değer sıfır olamaz.")
    
    return agirlikli_toplam / bd


def modified_duration(nakit_akislari, faiz_orani):
    """
    Modified Duration hesaplar
    
    Args:
        nakit_akislari: [(dönem, tutar), ...] şeklinde liste
        faiz_orani: Dönemsel faiz oranı
    
    Returns:
        Modified Duration
    """
    mac_dur = macaulay_duration(nakit_akislari, faiz_orani)
    return mac_dur / (1 + faiz_orani)


def convexity(nakit_akislari, faiz_orani):
    """
    Convexity (dışbükeylik) hesaplar
    
    Args:
        nakit_akislari: [(dönem, tutar), ...] şeklinde liste
        faiz_orani: Dönemsel faiz oranı
    
    Returns:
        Convexity
    """
    if faiz_orani <= -1:
        raise ValueError("Faiz oranı -1'den büyük olmalıdır.")
    
    v = 1 / (1 + faiz_orani)
    
    bd = sum(tutar * (v ** donem) for donem, tutar in nakit_akislari)
    
    if bd == 0:
        raise ValueError("Bugünkü değer sıfır olamaz.")
    
    convexity_sum = sum(donem * (donem + 1) * tutar * (v ** (donem + 2)) 
                        for donem, tutar in nakit_akislari)
    
    return convexity_sum / bd


def dv01(nakit_akislari, faiz_orani):
    """
    DV01 (Dollar Value of 01) - Faiz oranındaki 1 baz puanlık değişimin 
    tahvilin değerindeki değişimi
    
    Args:
        nakit_akislari: [(dönem, tutar), ...] şeklinde liste
        faiz_orani: Dönemsel faiz oranı
    
    Returns:
        DV01
    """
    mod_dur = modified_duration(nakit_akislari, faiz_orani)
    v = 1 / (1 + faiz_orani)
    bd = sum(tutar * (v ** donem) for donem, tutar in nakit_akislari)
    
    return mod_dur * bd * 0.0001  # 1 baz puan = 0.0001


# ============================================================
# NET BUGÜNKÜ DEĞER VE İÇ VERİM ORANI
# ============================================================

def net_bugunku_deger(nakit_akislari, faiz_orani, baslangic_yatirim=0):
    """
    Net Bugünkü Değer (NPV) hesaplar
    
    Args:
        nakit_akislari: [(dönem, tutar), ...] şeklinde liste
        faiz_orani: İskonto oranı
        baslangic_yatirim: Başlangıçtaki yatırım (negatif olmalı)
    
    Returns:
        Net Bugünkü Değer
    """
    if faiz_orani <= -1:
        raise ValueError("Faiz oranı -1'den büyük olmalıdır.")
    
    v = 1 / (1 + faiz_orani)
    bd = sum(tutar * (v ** donem) for donem, tutar in nakit_akislari)
    
    return bd + baslangic_yatirim


def ic_verim_orani(nakit_akislari, baslangic_yatirim, tahmin=0.1, tolerans=1e-6, max_iter=100):
    """
    İç Verim Oranı (IRR - Internal Rate of Return) hesaplar
    NPV'yi sıfır yapan faiz oranı
    
    Args:
        nakit_akislari: [(dönem, tutar), ...] şeklinde liste
        baslangic_yatirim: Başlangıçtaki yatırım (negatif)
        tahmin: Başlangıç tahmini
        tolerans: Yakınsama toleransı
        max_iter: Maksimum iterasyon sayısı
    
    Returns:
        İç Verim Oranı
    """
    i = tahmin
    
    for _ in range(max_iter):
        npv = net_bugunku_deger(nakit_akislari, i, baslangic_yatirim)
        
        if abs(npv) < tolerans:
            return i
        
        # Sayısal türev
        delta = 1e-8
        npv_delta = net_bugunku_deger(nakit_akislari, i + delta, baslangic_yatirim)
        turev = (npv_delta - npv) / delta
        
        if abs(turev) < 1e-10:
            raise ValueError("Türev sıfıra çok yakın, yakınsama sağlanamadı.")
        
        i_yeni = i - npv / turev
        
        if i_yeni <= -1:
            i_yeni = -0.99
        
        if abs(i_yeni - i) < tolerans:
            return i_yeni
        
        i = i_yeni
    
    raise ValueError(f"Yakınsama sağlanamadı ({max_iter} iterasyonda).")


# ============================================================
# AMORTİSMAN HESAPLAMALARI
# ============================================================

def aylik_taksit_hesapla(ana_para, yillik_faiz, ay_sayisi):
    """
    Kredi için aylık taksit hesaplar (Eşit taksitli kredi)
    
    Args:
        ana_para: Kredi tutarı
        yillik_faiz: Yıllık faiz oranı
        ay_sayisi: Vade (ay)
    
    Returns:
        Aylık taksit tutarı
    """
    if ana_para <= 0:
        raise ValueError("Ana para pozitif olmalıdır.")
    if ay_sayisi <= 0:
        raise ValueError("Vade pozitif olmalıdır.")
    
    aylik_faiz = yillik_aylik_cevir(yillik_faiz)
    
    if aylik_faiz == 0:
        return ana_para / ay_sayisi
    
    # Devre sonu anüite formülü
    return ana_para * aylik_faiz / (1 - (1 + aylik_faiz) ** (-ay_sayisi))


def kalan_borc_hesapla(ana_para, yillik_faiz, ay_sayisi, gecen_ay):
    """
    Belirli bir dönem sonrası kalan borç hesaplar
    
    Args:
        ana_para: Kredi tutarı
        yillik_faiz: Yıllık faiz oranı
        ay_sayisi: Toplam vade (ay)
        gecen_ay: Geçen ay sayısı
    
    Returns:
        Kalan borç
    """
    if gecen_ay >= ay_sayisi:
        return 0
    
    aylik_faiz = yillik_aylik_cevir(yillik_faiz)
    aylik_taksit = aylik_taksit_hesapla(ana_para, yillik_faiz, ay_sayisi)
    
    kalan_donem = ay_sayisi - gecen_ay
    
    # Kalan borç = Kalan taksitlerin bugünkü değeri
    if aylik_faiz == 0:
        return aylik_taksit * kalan_donem
    
    return aylik_taksit * (1 - (1 + aylik_faiz) ** (-kalan_donem)) / aylik_faiz


def erken_odeme_tutari(ana_para, yillik_faiz, ay_sayisi, gecen_ay):
    """
    Erken ödeme tutarı hesaplar (kalan borç + ceza yok varsayımı)
    
    Args:
        ana_para: Kredi tutarı
        yillik_faiz: Yıllık faiz oranı
        ay_sayisi: Toplam vade (ay)
        gecen_ay: Geçen ay sayısı
    
    Returns:
        Erken ödeme tutarı
    """
    return kalan_borc_hesapla(ana_para, yillik_faiz, ay_sayisi, gecen_ay)


# ============================================================
# DİĞER YARDIMCI FONKSİYONLAR
# ============================================================

def efektif_yillik_verim(nakit_akislari):
    """
    Efektif yıllık verim hesaplar (Basitleştirilmiş - IRR benzeri)
    
    Args:
        nakit_akislari: [(dönem, tutar), ...] - dönem 0'dan başlar
    
    Returns:
        Efektif yıllık verim oranı
    """
    baslangic = next((tutar for donem, tutar in nakit_akislari if donem == 0), 0)
    diger_akislar = [(d, t) for d, t in nakit_akislari if d > 0]
    
    return ic_verim_orani(diger_akislar, baslangic)


def basit_faiz_hesapla(ana_para, faiz_orani, sure):
    """
    Basit faiz hesaplar
    
    Args:
        ana_para: Ana para
        faiz_orani: Dönemsel faiz oranı
        sure: Süre
    
    Returns:
        Toplam tutar (ana para + faiz)
    """
    return ana_para * (1 + faiz_orani * sure)


def bilesik_faiz_hesapla(ana_para, faiz_orani, sure):
    """
    Bileşik faiz hesaplar
    
    Args:
        ana_para: Ana para
        faiz_orani: Dönemsel faiz oranı
        sure: Süre
    
    Returns:
        Toplam tutar (ana para + faiz)
    """
    return ana_para * ((1 + faiz_orani) ** sure)