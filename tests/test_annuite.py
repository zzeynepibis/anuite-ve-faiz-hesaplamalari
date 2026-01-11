"""
ANÜİTELER Kütüphanesi - Kapsamlı Test Programı

Tüm modülleri ve formüllerin tersini test eder

Geliştirici: Zeynep İbiş
Tarih: 11 Ocak 2025
Proje: anuite-ve-faiz-hesaplamalari
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from anuiteler import *


def test_tek_odeme():
    """Tek ödeme hesaplamalarını test et"""
    print("\n" + "="*60)
    print("TEK ÖDEME TESTLERİ")
    print("="*60)
    
    # Test 1: BD → GD → BD
    print("\n[Test 1: BD → GD → BD]")
    bd_baslangic = 1000
    i = 0.10
    t = 5
    
    gd = tek_odeme_gd(bd_baslangic, i, t)
    bd_son = tek_odeme_bd(gd, i, t)
    
    print(f"Başlangıç BD: {bd_baslangic} TL")
    print(f"Hesaplanan GD: {gd:.2f} TL")
    print(f"Geri hesaplanan BD: {bd_son:.2f} TL")
    print(f"Hata: {abs(bd_baslangic - bd_son):.6f}")
    
    # Test 2: Faiz oranı hesaplama
    print("\n[Test 2: Faiz oranı hesaplama]")
    bd = 1000
    gd = 1610.51
    t = 5
    
    i_hesaplanan = tek_odeme_faiz(bd, gd, t)
    print(f"BD={bd}, GD={gd}, t={t}")
    print(f"Hesaplanan i: {i_hesaplanan:.4f} (%{i_hesaplanan*100:.2f})")
    
    # Test 3: Süre hesaplama
    print("\n[Test 3: Süre hesaplama]")
    bd = 1000
    gd = 1610.51
    i = 0.10
    
    t_hesaplanan = tek_odeme_sure(bd, gd, i)
    print(f"BD={bd}, GD={gd}, i={i}")
    print(f"Hesaplanan t: {t_hesaplanan:.2f} dönem")


def test_devre_sonu():
    """Devre sonu anüite testleri"""
    print("\n" + "="*60)
    print("DEVRE SONU ANÜİTE TESTLERİ")
    print("="*60)
    
    # Test 1: BD'den tüm formüller
    print("\n[Test 1: Bugünkü Değer Formülleri]")
    odeme = 1000
    n = 5
    i = 0.10
    
    bd = ds_bd_hesapla(odeme, n, i)
    print(f"Ödeme={odeme}, n={n}, i={i}")
    print(f"Bugünkü Değer: {bd:.2f} TL")
    
    # Ters formül: BD'den ödeme
    odeme_ters = ds_odeme_bd(bd, n, i)
    print(f"BD'den hesaplanan ödeme: {odeme_ters:.2f} TL (hata: {abs(odeme-odeme_ters):.6f})")
    
    # Ters formül: BD'den süre
    n_ters = ds_sure_bd(bd, odeme, i)
    print(f"BD'den hesaplanan n: {n_ters:.2f} dönem (hata: {abs(n-n_ters):.6f})")
    
    # Ters formül: BD'den faiz
    i_ters = ds_faiz_bd(bd, odeme, n)
    print(f"BD'den hesaplanan i: {i_ters:.4f} (hata: {abs(i-i_ters):.6f})")
    
    # Test 2: GD'den tüm formüller
    print("\n[Test 2: Gelecek Değer Formülleri]")
    gd = ds_gd_hesapla(odeme, n, i)
    print(f"Gelecek Değer: {gd:.2f} TL")
    
    # Ters formüller
    odeme_ters2 = ds_odeme_gd(gd, n, i)
    print(f"GD'den hesaplanan ödeme: {odeme_ters2:.2f} TL (hata: {abs(odeme-odeme_ters2):.6f})")
    
    n_ters2 = ds_sure_gd(gd, odeme, i)
    print(f"GD'den hesaplanan n: {n_ters2:.2f} dönem (hata: {abs(n-n_ters2):.6f})")
    
    i_ters2 = ds_faiz_gd(gd, odeme, n)
    print(f"GD'den hesaplanan i: {i_ters2:.4f} (hata: {abs(i-i_ters2):.6f})")


def test_devre_basi():
    """Devre başı anüite testleri"""
    print("\n" + "="*60)
    print("DEVRE BAŞI ANÜİTE TESTLERİ")
    print("="*60)
    
    # Test 1: BD formülleri
    print("\n[Test 1: Bugünkü Değer Formülleri]")
    odeme = 1000
    n = 5
    i = 0.10
    
    bd = db_bd_hesapla(odeme, n, i)
    print(f"Ödeme={odeme}, n={n}, i={i}")
    print(f"Bugünkü Değer (Devre Başı): {bd:.2f} TL")
    
    # Ters formüller
    odeme_ters = db_odeme_bd(bd, n, i)
    n_ters = db_sure_bd(bd, odeme, i)
    i_ters = db_faiz_bd(bd, odeme, n)
    
    print(f"BD'den hesaplanan ödeme: {odeme_ters:.2f} TL")
    print(f"BD'den hesaplanan n: {n_ters:.2f} dönem")
    print(f"BD'den hesaplanan i: {i_ters:.4f}")
    
    # Test 2: GD formülleri
    print("\n[Test 2: Gelecek Değer Formülleri]")
    gd = db_gd_hesapla(odeme, n, i)
    print(f"Gelecek Değer (Devre Başı): {gd:.2f} TL")
    
    # Devre sonu ile karşılaştır
    gd_ds = ds_gd_hesapla(odeme, n, i)
    print(f"Gelecek Değer (Devre Sonu): {gd_ds:.2f} TL")
    print(f"Fark: {gd - gd_ds:.2f} TL (= {odeme * i:.2f} TL olmalı)")


def test_surekli():
    """Sürekli anüite testleri"""
    print("\n" + "="*60)
    print("SÜREKLİ ANÜİTE TESTLERİ")
    print("="*60)
    
    # Test 1: Devre sonu sürekli
    print("\n[Test 1: Devre Sonu Sürekli Anüite]")
    odeme = 1000
    i = 0.10
    
    bd = surekli_ds_bd(odeme, i)
    print(f"Ödeme={odeme}, i={i}")
    print(f"Bugünkü Değer: {bd:.2f} TL")
    print(f"Beklenen: {1000/0.10:.2f} TL")
    
    # Ters formüller
    odeme_ters = surekli_ds_odeme(bd, i)
    i_ters = surekli_ds_faiz(bd, odeme)
    
    print(f"BD'den ödeme: {odeme_ters:.2f} TL")
    print(f"BD'den faiz: {i_ters:.4f}")
    
    # Test 2: Devre başı sürekli
    print("\n[Test 2: Devre Başı Sürekli Anüite]")
    bd_basi = surekli_db_bd(odeme, i)
    print(f"Bugünkü Değer (Devre Başı): {bd_basi:.2f} TL")
    print(f"Beklenen: {odeme * (1+i) / i:.2f} TL")
    
    # Test 3: Ertelenmiş sürekli
    print("\n[Test 3: Ertelenmiş Sürekli Anüite]")
    m = 3
    bd_ertelenme = ertelenmis_surekli_anuite(odeme, i, m)
    print(f"{m} dönem ertelenmiş sürekli anüite BD: {bd_ertelenme:.2f} TL")


def test_ertelenmis():
    """Ertelenmiş anüite testleri (YENİ!)"""
    print("\n" + "="*60)
    print("ERTELENMİŞ ANÜİTE TESTLERİ")
    print("="*60)
    
    # Test 1: Devre sonu ertelenmiş
    print("\n[Test 1: Devre Sonu Ertelenmiş - Notlardan Örnek]")
    # 4 yıl sonra başlayacak 8 yıllık ödeme, %30 faiz, 32000 TL kredi
    taksit = 10367.87
    i = 0.30
    n = 8
    m = 4
    
    bd = ert_ds_bd(taksit, i, n, m)
    print(f"Taksit={taksit}, i={i}, n={n}, m={m}")
    print(f"Bugünkü Değer: {bd:.2f} TL")
    print(f"Beklenen: ~32000 TL")
    
    # Ters formül: Taksit hesaplama
    print("\n[Test 2: BD'den Taksit Hesaplama]")
    bd_hedef = 32000
    taksit_hesaplanan = ert_ds_taksit_bd(bd_hedef, i, n, m)
    print(f"BD={bd_hedef}, i={i}, n={n}, m={m}")
    print(f"Hesaplanan taksit: {taksit_hesaplanan:.2f} TL")
    print(f"Kontrol - Geri hesaplanan BD: {ert_ds_bd(taksit_hesaplanan, i, n, m):.2f} TL")
    
    # Test 3: Gecikme süresi hesaplama
    print("\n[Test 3: Gecikme Süresi (m) Hesaplama]")
    m_hesaplanan = ert_gecikme_hesapla(bd_hedef, taksit, i, n)
    print(f"BD={bd_hedef}, taksit={taksit}, i={i}, n={n}")
    print(f"Hesaplanan gecikme süresi: {m_hesaplanan:.2f} dönem")
    print(f"Gerçek m: {m}")


def test_geometrik():
    """Geometrik anüite testleri (YENİ!)"""
    print("\n" + "="*60)
    print("GEOMETRİK ANÜİTE TESTLERİ")
    print("="*60)
    
    # Test 1: i ≠ r durumu (Notlardan örnek)
    print("\n[Test 1: Geometrik Dizi - i≠r]")
    ilk_taksit = 5000
    i = 0.05
    r = 0.20
    n = 6
    
    bd = geo_ds_bd(ilk_taksit, i, r, n)
    print(f"İlk taksit={ilk_taksit}, i={i}, r={r}, n={n}")
    print(f"Bugünkü Değer: {bd:.2f} TL")
    print(f"Beklenen: ~40939.59 TL (notlardan)")
    
    # Test 2: i = r durumu
    print("\n[Test 2: Geometrik Dizi - i=r (Özel Durum)]")
    i_esit = 0.10
    r_esit = 0.10
    bd_esit = geo_ds_bd(ilk_taksit, i_esit, r_esit, n)
    print(f"İlk taksit={ilk_taksit}, i=r={i_esit}, n={n}")
    print(f"Bugünkü Değer: {bd_esit:.2f} TL")
    print(f"Formül: n × a × (1+i)^(n-1) = {n * ilk_taksit * ((1+i_esit)**(n-1)):.2f} TL")
    
    # Test 3: Ters formül - İlk taksit hesaplama
    print("\n[Test 3: BD'den İlk Taksit Hesaplama]")
    bd_hedef = 40939.59
    ilk_taksit_hesaplanan = geo_ilk_taksit_bd(bd_hedef, i, r, n)
    print(f"BD={bd_hedef}, i={i}, r={r}, n={n}")
    print(f"Hesaplanan ilk taksit: {ilk_taksit_hesaplanan:.2f} TL")
    print(f"Gerçek ilk taksit: {ilk_taksit} TL")


def test_aritmetik():
    """Aritmetik anüite testleri (YENİ!)"""
    print("\n" + "="*60)
    print("ARİTMETİK ANÜİTE TESTLERİ")
    print("="*60)
    
    # Test 1: Artan taksitler (Notlardan örnek)
    print("\n[Test 1: Artan Taksitler - a, a+b, a+2b, ...]")
    ilk_taksit = 5000
    degisim = 500  # Her dönem 500 TL artış
    i = 0.30
    n = 6
    
    bd = arit_ds_bd(ilk_taksit, degisim, i, n)
    print(f"İlk taksit={ilk_taksit}, değişim={degisim}, i={i}, n={n}")
    print(f"Taksitler: {ilk_taksit}, {ilk_taksit+degisim}, {ilk_taksit+2*degisim}, ...")
    print(f"Bugünkü Değer: {bd:.2f} TL")
    
    # Test 2: Azalan taksitler
    print("\n[Test 2: Azalan Taksitler]")
    degisim_azalan = -500  # Her dönem 500 TL azalış
    bd_azalan = arit_ds_bd(ilk_taksit, degisim_azalan, i, n)
    print(f"İlk taksit={ilk_taksit}, değişim={degisim_azalan}, i={i}, n={n}")
    print(f"Taksitler: {ilk_taksit}, {ilk_taksit+degisim_azalan}, {ilk_taksit+2*degisim_azalan}, ...")
    print(f"Bugünkü Değer: {bd_azalan:.2f} TL")
    
    # Test 3: Değişim miktarı (b) hesaplama
    print("\n[Test 3: Değişim Miktarı (b) Hesaplama]")
    bd_hedef = 18000
    ilk_taksit = 1101
    i = 0.40
    n = 5
    
    degisim_hesaplanan = arit_ds_degisim(bd_hedef, ilk_taksit, i, n)
    print(f"BD={bd_hedef}, ilk_taksit={ilk_taksit}, i={i}, n={n}")
    print(f"Hesaplanan değişim (b): {degisim_hesaplanan:.2f} TL/dönem")
    
    # Kontrol
    bd_kontrol = arit_ds_bd(ilk_taksit, degisim_hesaplanan, i, n)
    print(f"Kontrol BD: {bd_kontrol:.2f} TL (hata: {abs(bd_hedef - bd_kontrol):.2f})")


def test_cabuklas():
    """Çabuklaştırılmış anüite testleri (YENİ!)"""
    print("\n" + "="*60)
    print("ÇABUKLAŞTIRILMIŞ ANÜİTE TESTLERİ")
    print("="*60)
    
    # Test 1: Devre sonu çabuklaştırılmış (Notlardan örnek)
    print("\n[Test 1: Çabuklaştırılmış Anüite]")
    taksit = 10000
    i = 0.30
    n = 8
    c = 2  # 2 dönem erken çekildi
    
    bd = cab_ds_bd(taksit, i, n, c)
    print(f"Taksit={taksit}, i={i}, n={n}, çabuklaştırma={c}")
    print(f"Bugünkü Değer: {bd:.2f} TL")
    print(f"Beklenen: ~51815.69 TL (notlardan)")
    
    # Normal anüite ile karşılaştır
    bd_normal = ds_bd_hesapla(taksit, n, i)
    print(f"Normal anüite BD: {bd_normal:.2f} TL")
    print(f"Fark: {bd - bd_normal:.2f} TL")
    
    # Test 2: Taksit hesaplama
    print("\n[Test 2: BD'den Taksit Hesaplama]")
    bd_hedef = 48000
    taksit_hesaplanan = cab_taksit_bd(bd_hedef, i, n, c)
    print(f"BD={bd_hedef}, i={i}, n={n}, c={c}")
    print(f"Hesaplanan taksit: {taksit_hesaplanan:.2f} TL")
    
    # Test 3: Çabuklaştırma süresi hesaplama
    print("\n[Test 3: Çabuklaştırma Süresi (c) Hesaplama]")
    bd_test = 51815.69
    c_hesaplanan = cab_sure_hesapla(bd_test, taksit, i, n)
    print(f"BD={bd_test}, taksit={taksit}, i={i}, n={n}")
    print(f"Hesaplanan çabuklaştırma süresi: {c_hesaplanan:.2f} dönem")
    print(f"Gerçek c: {c}")


def test_yardimci():
    """Yardımcı fonksiyonları test et"""
    print("\n" + "="*60)
    print("YARDIMCI FONKSİYON TESTLERİ")
    print("="*60)
    
    # Test 1: Efektif/Nominal çevirme
    print("\n[Test 1: Faiz Oranı Çevrimleri]")
    nominal = 0.12
    m = 12
    
    efektif = efektif_faiz_orani(nominal, m)
    nominal_ters = nominal_faiz_orani(efektif, m)
    
    print(f"Nominal (%12 yıllık, aylık bileşik): {nominal}")
    print(f"Efektif: {efektif:.6f} (%{efektif*100:.2f})")
    print(f"Geri hesaplanan nominal: {nominal_ters:.6f}")
    print(f"Hata: {abs(nominal - nominal_ters):.10f}")
    
    # Test 2: Sürekli faiz
    print("\n[Test 2: Sürekli Faiz Oranı]")
    i = 0.10
    delta = surekli_faiz_orani(i)
    i_ters = efektif_from_surekli(delta)
    
    print(f"Efektif faiz: {i}")
    print(f"Sürekli faiz (δ): {delta:.6f}")
    print(f"Geri hesaplanan efektif: {i_ters:.6f}")
    print(f"Hata: {abs(i - i_ters):.10f}")
    
    # Test 3: İskonto/Faiz çevirme
    print("\n[Test 3: İskonto Oranı Çevrimleri]")
    i = 0.10
    d = faizden_iskonto_orani(i)
    i_ters = iskontodan_faiz_orani(d)
    
    print(f"Faiz oranı: {i}")
    print(f"İskonto oranı: {d:.6f}")
    print(f"Geri hesaplanan faiz: {i_ters:.6f}")
    print(f"Hata: {abs(i - i_ters):.10f}")
    
    # Test 4: Reel faiz
    print("\n[Test 4: Reel Faiz Hesaplama]")
    nominal = 0.15
    enflasyon = 0.08
    
    reel = reel_faiz_orani(nominal, enflasyon)
    nominal_ters = nominal_from_reel(reel, enflasyon)
    
    print(f"Nominal faiz: %{nominal*100}")
    print(f"Enflasyon: %{enflasyon*100}")
    print(f"Reel faiz: {reel:.6f} (%{reel*100:.2f})")
    print(f"Geri hesaplanan nominal: {nominal_ters:.6f}")


def test_ters_kontrol():
    """Tüm formüllerin ters kontrolü"""
    print("\n" + "="*60)
    print("KAPSAMLI TERS KONTROL TESTİ")
    print("="*60)
    
    basarili = 0
    toplam = 0
    
    testler = [
        ("Tek Ödeme BD→GD→BD", lambda: test_tek_odeme_ters()),
        ("Devre Sonu BD Formülleri", lambda: test_ds_bd_ters()),
        ("Devre Sonu GD Formülleri", lambda: test_ds_gd_ters()),
        ("Devre Başı BD Formülleri", lambda: test_db_bd_ters()),
        ("Devre Başı GD Formülleri", lambda: test_db_gd_ters()),
        ("Sürekli Anüite", lambda: test_surekli_ters()),
        ("Ertelenmiş Anüite", lambda: test_ertelenmis_ters()),
        ("Geometrik Anüite", lambda: test_geometrik_ters()),
        ("Aritmetik Anüite", lambda: test_aritmetik_ters()),
        ("Çabuklaştırılmış Anüite", lambda: test_cabuklas_ters()),
    ]
    
    for test_adi, test_func in testler:
        toplam += 1
        try:
            test_func()
            print(f"✓ {test_adi}: BAŞARILI")
            basarili += 1
        except Exception as e:
            print(f"✗ {test_adi}: BAŞARISIZ - {str(e)}")
    
    print(f"\n{basarili}/{toplam} test başarılı (%{basarili/toplam*100:.0f})")


# Ters test fonksiyonları
def test_tek_odeme_ters():
    bd = 1000
    i = 0.10
    t = 5
    gd = tek_odeme_gd(bd, i, t)
    bd_ters = tek_odeme_bd(gd, i, t)
    assert abs(bd - bd_ters) < 0.01


def test_ds_bd_ters():
    odeme = 1000
    n = 5
    i = 0.10
    bd = ds_bd_hesapla(odeme, n, i)
    odeme_ters = ds_odeme_bd(bd, n, i)
    assert abs(odeme - odeme_ters) < 0.01


def test_ds_gd_ters():
    odeme = 1000
    n = 5
    i = 0.10
    gd = ds_gd_hesapla(odeme, n, i)
    odeme_ters = ds_odeme_gd(gd, n, i)
    assert abs(odeme - odeme_ters) < 0.01


def test_db_bd_ters():
    odeme = 1000
    n = 5
    i = 0.10
    bd = db_bd_hesapla(odeme, n, i)
    odeme_ters = db_odeme_bd(bd, n, i)
    assert abs(odeme - odeme_ters) < 0.01


def test_db_gd_ters():
    odeme = 1000
    n = 5
    i = 0.10
    gd = db_gd_hesapla(odeme, n, i)
    odeme_ters = db_odeme_gd(gd, n, i)
    assert abs(odeme - odeme_ters) < 0.01


def test_surekli_ters():
    odeme = 1000
    i = 0.10
    bd = surekli_ds_bd(odeme, i)
    odeme_ters = surekli_ds_odeme(bd, i)
    assert abs(odeme - odeme_ters) < 0.01


def test_ertelenmis_ters():
    taksit = 10000
    i = 0.30
    n = 8
    m = 4
    bd = ert_ds_bd(taksit, i, n, m)
    taksit_ters = ert_ds_taksit_bd(bd, i, n, m)
    assert abs(taksit - taksit_ters) < 0.01


def test_geometrik_ters():
    ilk_taksit = 5000
    i = 0.05
    r = 0.20
    n = 6
    bd = geo_ds_bd(ilk_taksit, i, r, n)
    ilk_taksit_ters = geo_ilk_taksit_bd(bd, i, r, n)
    assert abs(ilk_taksit - ilk_taksit_ters) < 0.01


def test_aritmetik_ters():
    ilk_taksit = 5000
    degisim = 500
    i = 0.30
    n = 6
    bd = arit_ds_bd(ilk_taksit, degisim, i, n)
    ilk_taksit_ters = arit_ds_ilk_taksit_bd(bd, degisim, i, n)
    assert abs(ilk_taksit - ilk_taksit_ters) < 0.01


def test_cabuklas_ters():
    taksit = 10000
    i = 0.30
    n = 8
    c = 2
    bd = cab_ds_bd(taksit, i, n, c)
    taksit_ters = cab_taksit_bd(bd, i, n, c)
    assert abs(taksit - taksit_ters) < 0.01


def test_tablo():
    """Anüite tablosu testi"""
    print("\n" + "="*60)
    print("ANÜİTE TABLOSU TESTİ")
    print("="*60)
    
    print("\n[Devre Sonu Ödemeli Tablo]")
    tablo = ds_tablo(1000, 5, 0.10)
    
    print(f"\n{'Dönem':<8} {'Ödeme':<12} {'Faiz':<12} {'Anapara':<12} {'Kalan':<12}")
    print("-" * 60)
    
    for satir in tablo:
        print(f"{satir['donem']:<8} {satir['odeme']:<12.2f} {satir['faiz']:<12.2f} "
              f"{satir['anapara']:<12.2f} {satir['kalan']:<12.2f}")


def test_hizli_hesapla():
    """Hızlı hesaplama fonksiyonu testi"""
    print("\n" + "="*60)
    print("HIZLI HESAPLAMA FONKSİYONU TESTİ")
    print("="*60)
    
    # Test 1: Ödeme bilinmiyor
    print("\n[Test: Ödeme hesaplama]")
    sonuc = anuite_hesapla(bugunku_deger=50000, n=24, i=0.015, tip='devre_sonu')
    print(f"BD=50000, n=24, i=0.015")
    print(f"Hesaplanan ödeme: {sonuc['odeme']:.2f} TL")


if __name__ == "__main__":
    print("=" * 60)
    print("ANÜİTELER KÜTÜPHANESİ - KAPSAMLI TEST PROGRAMI")
    print("Geliştirici: Zeynep İbiş")
    print("Tarih: 11 Ocak 2025")
    print("=" * 60)
    
    test_tek_odeme()
    test_devre_sonu()
    test_devre_basi()
    test_surekli()
    test_ertelenmis()      # YENİ!
    test_geometrik()       # YENİ!
    test_aritmetik()       # YENİ!
    test_cabuklas()        # YENİ!
    test_yardimci()
    test_tablo()
    test_hizli_hesapla()
    test_ters_kontrol()
    
    print("\n" + "=" * 60)
    print("TÜM TESTLER TAMAMLANDI!")
    print("Geliştirici: Zeynep İbiş")
    print("=" * 60)