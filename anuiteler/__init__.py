"""
ANÜİTELER - Aktüeryal Hesaplama Kütüphanesi

Kapsamlı finans matematiği hesaplamaları için Türkçe Python paketi.

Modüller:
- tek_odeme: Tek bir ödemenin BD/GD hesaplamaları
- devre_sonu_anuite: Devre sonu ödemeli anüiteler  
- devre_basi_anuite: Devre başı ödemeli anüiteler
- surekli_anuite: Sürekli (perpetuity) anüiteler
- ertelenmis_anuite: Ertelenmiş (geciktirilmiş) anüiteler
- geometrik_anuite: Geometrik dizi şeklinde değişen taksitler
- aritmetik_anuite: Aritmetik dizi şeklinde değişen taksitler
- cabuklas_anuite: Çabuklaştırılmış anüiteler
- yardimci: Faiz çevrimleri ve yardımcı fonksiyonlar
"""

__version__ = "1.0.0"
__author__ = "Zeynep İbiş"

# ============================================================
# TEK ÖDEME MODÜLÜ
# ============================================================
from . import tek_odeme

# Tek ödeme fonksiyonları
from .tek_odeme import (
    bugunku_deger as tek_odeme_bd,
    gelecek_deger as tek_odeme_gd,
    faiz_orani_hesapla as tek_odeme_faiz,
    sure_hesapla as tek_odeme_sure,
    iskonto_faktoru_hesapla,
    birikim_faktoru_hesapla
)

# ============================================================
# DEVRE SONU ANÜİTE MODÜLÜ
# ============================================================
from . import devre_sonu_anuite

# Devre sonu fonksiyonları - Bugünkü Değer
from .devre_sonu_anuite import (
    bugunku_deger_hesapla as ds_bd_hesapla,
    odeme_bugunku_degerden as ds_odeme_bd,
    sure_bugunku_degerden as ds_sure_bd,
    faiz_bugunku_degerden as ds_faiz_bd,
)

# Devre sonu fonksiyonları - Gelecek Değer
from .devre_sonu_anuite import (
    gelecek_deger_hesapla as ds_gd_hesapla,
    odeme_gelecek_degerden as ds_odeme_gd,
    sure_gelecek_degerden as ds_sure_gd,
    faiz_gelecek_degerden as ds_faiz_gd,
)

# Devre sonu faktörler
from .devre_sonu_anuite import (
    pesin_deger_faktoru as ds_pesin_faktor,
    gelecek_deger_faktoru as ds_gelecek_faktor,
    anuite_tablosu_olustur as ds_tablo
)

# ============================================================
# DEVRE BAŞI ANÜİTE MODÜLÜ
# ============================================================
from . import devre_basi_anuite

# Devre başı fonksiyonları - Bugünkü Değer
from .devre_basi_anuite import (
    bugunku_deger_hesapla as db_bd_hesapla,
    odeme_bugunku_degerden as db_odeme_bd,
    sure_bugunku_degerden as db_sure_bd,
    faiz_bugunku_degerden as db_faiz_bd,
)

# Devre başı fonksiyonları - Gelecek Değer
from .devre_basi_anuite import (
    gelecek_deger_hesapla as db_gd_hesapla,
    odeme_gelecek_degerden as db_odeme_gd,
    sure_gelecek_degerden as db_sure_gd,
    faiz_gelecek_degerden as db_faiz_gd,
)

# Devre başı faktörler
from .devre_basi_anuite import (
    pesin_deger_faktoru as db_pesin_faktor,
    gelecek_deger_faktoru as db_gelecek_faktor,
    anuite_tablosu_olustur as db_tablo
)

# ============================================================
# SÜREKLİ ANÜİTE MODÜLÜ
# ============================================================
from . import surekli_anuite

from .surekli_anuite import (
    bugunku_deger_devre_sonu as surekli_ds_bd,
    odeme_devre_sonu as surekli_ds_odeme,
    faiz_devre_sonu as surekli_ds_faiz,
    bugunku_deger_devre_basi as surekli_db_bd,
    odeme_devre_basi as surekli_db_odeme,
    faiz_devre_basi as surekli_db_faiz,
    ertelenmis_surekli_anuite
)

# ============================================================
# ERTELENMİŞ ANÜİTE MODÜLÜ (YENİ!)
# ============================================================
from . import ertelenmis_anuite

# Ertelenmiş anüite - Devre Sonu
from .ertelenmis_anuite import (
    bugunku_deger_devre_sonu as ert_ds_bd,
    gelecek_deger_devre_sonu as ert_ds_gd,
    taksit_hesapla_bd_devre_sonu as ert_ds_taksit_bd,
    taksit_hesapla_gd_devre_sonu as ert_ds_taksit_gd,
)

# Ertelenmiş anüite - Devre Başı
from .ertelenmis_anuite import (
    bugunku_deger_devre_basi as ert_db_bd,
    gelecek_deger_devre_basi as ert_db_gd,
    taksit_hesapla_bd_devre_basi as ert_db_taksit_bd,
)

# Ertelenmiş anüite - Ters Formüller
from .ertelenmis_anuite import (
    gecikme_suresi_hesapla_bd as ert_gecikme_hesapla,
    faiz_orani_hesapla_bd as ert_faiz_hesapla,
    sure_hesapla_bd as ert_sure_hesapla,
)

# Çabuklaştırılmış Ertelenmiş
from .ertelenmis_anuite import (
    bugunku_deger_cabuklas_ertekenmis as ert_cabuklas_bd,
)

# ============================================================
# GEOMETRİK ANÜİTE MODÜLÜ (YENİ!)
# ============================================================
from . import geometrik_anuite

# Geometrik - Devre Sonu
from .geometrik_anuite import (
    bugunku_deger_devre_sonu as geo_ds_bd,
    gelecek_deger_devre_sonu as geo_ds_gd,
)

# Geometrik - Devre Başı
from .geometrik_anuite import (
    bugunku_deger_devre_basi as geo_db_bd,
    gelecek_deger_devre_basi as geo_db_gd,
)

# Geometrik - Ters Formüller
from .geometrik_anuite import (
    ilk_taksit_hesapla_bd as geo_ilk_taksit_bd,
    ilk_taksit_hesapla_gd as geo_ilk_taksit_gd,
    faiz_orani_hesapla_bd as geo_faiz_hesapla,
    sure_hesapla_gd as geo_sure_hesapla,
)

# ============================================================
# ARİTMETİK ANÜİTE MODÜLÜ (YENİ!)
# ============================================================
from . import aritmetik_anuite

# Aritmetik - Devre Sonu
from .aritmetik_anuite import (
    bugunku_deger_devre_sonu as arit_ds_bd,
    gelecek_deger_devre_sonu as arit_ds_gd,
    ilk_taksit_hesapla_bd_devre_sonu as arit_ds_ilk_taksit_bd,
    ilk_taksit_hesapla_gd_devre_sonu as arit_ds_ilk_taksit_gd,
    degisim_hesapla_bd_devre_sonu as arit_ds_degisim,
)

# Aritmetik - Devre Başı
from .aritmetik_anuite import (
    bugunku_deger_devre_basi as arit_db_bd,
    gelecek_deger_devre_basi as arit_db_gd,
    ilk_taksit_hesapla_bd_devre_basi as arit_db_ilk_taksit_bd,
)

# Aritmetik - Ters Formüller
from .aritmetik_anuite import (
    faiz_orani_hesapla_bd as arit_faiz_hesapla,
    sure_hesapla_bd as arit_sure_hesapla,
)

# ============================================================
# ÇABUKLAŞTIRILMIŞ ANÜİTE MODÜLÜ (YENİ!)
# ============================================================
from . import cabuklas_anuite

# Çabuklaştırılmış - Devre Sonu
from .cabuklas_anuite import (
    bugunku_deger_devre_sonu as cab_ds_bd,
    gelecek_deger_devre_sonu as cab_ds_gd,
)

# Çabuklaştırılmış - Devre Başı
from .cabuklas_anuite import (
    bugunku_deger_devre_basi as cab_db_bd,
    gelecek_deger_devre_basi as cab_db_gd,
)

# Çabuklaştırılmış - Ters Formüller
from .cabuklas_anuite import (
    taksit_hesapla_bd as cab_taksit_bd,
    taksit_hesapla_gd as cab_taksit_gd,
    cabuklas_suresi_hesapla_bd as cab_sure_hesapla,
    faiz_orani_hesapla_bd as cab_faiz_hesapla,
    sure_hesapla_bd as cab_donem_hesapla,
)

# ============================================================
# YARDIMCI FONKSİYONLAR
# ============================================================
from . import yardimci

from .yardimci import (
    efektif_faiz_orani,
    nominal_faiz_orani,
    surekli_faiz_orani,
    efektif_from_surekli,
    faizden_iskonto_orani,
    iskontodan_faiz_orani,
    iskonto_faktoru,
    birikim_faktoru,
    toplam_odeme_hesapla,
    toplam_faiz_hesapla,
    ortalama_vade_hesapla,
    reel_faiz_orani,
    nominal_from_reel,
    yillik_aylik_cevir,
    aylik_yillik_cevir,
    gunluk_yillik_cevir,
    yillik_gunluk_cevir
)

# ============================================================
# HIZLI ERİŞİM FONKSİYONLARI
# ============================================================

def anuite_hesapla(odeme=None, bugunku_deger=None, gelecek_deger=None, n=None, i=None, tip='devre_sonu'):
    import warnings
    
    # Kaç değer verilmiş?
    verilen = sum([
        odeme is not None,
        bugunku_deger is not None,
        gelecek_deger is not None,
        n is not None,
        i is not None
    ])
    
    if verilen < 3:
        raise ValueError("En az 3 parametre gerekli!")
    
    if tip == 'devre_sonu':
        if odeme is None and bugunku_deger is not None and n is not None and i is not None:
            odeme = ds_odeme_bd(bugunku_deger, n, i)
        elif bugunku_deger is None and odeme is not None and n is not None and i is not None:
            bugunku_deger = ds_bd_hesapla(odeme, n, i)
        elif n is None and bugunku_deger is not None and odeme is not None and i is not None:
            n = ds_sure_bd(bugunku_deger, odeme, i)
        elif i is None and bugunku_deger is not None and odeme is not None and n is not None:
            i = ds_faiz_bd(bugunku_deger, odeme, n)
        else:
            warnings.warn("Bu kombinasyon henüz desteklenmiyor")
    
    elif tip == 'devre_basi':
        if odeme is None and bugunku_deger is not None and n is not None and i is not None:
            odeme = db_odeme_bd(bugunku_deger, n, i)
        elif bugunku_deger is None and odeme is not None and n is not None and i is not None:
            bugunku_deger = db_bd_hesapla(odeme, n, i)
        elif n is None and bugunku_deger is not None and odeme is not None and i is not None:
            n = db_sure_bd(bugunku_deger, odeme, i)
        elif i is None and bugunku_deger is not None and odeme is not None and n is not None:
            i = db_faiz_bd(bugunku_deger, odeme, n)
    
    return {
        'odeme': odeme,
        'bugunku_deger': bugunku_deger,
        'gelecek_deger': gelecek_deger,
        'n': n,
        'i': i,
        'tip': tip
    }


__all__ = [
    # Modüller
    'tek_odeme',
    'devre_sonu_anuite',
    'devre_basi_anuite',
    'surekli_anuite',
    'ertelenmis_anuite',
    'geometrik_anuite',
    'aritmetik_anuite',
    'cabuklas_anuite',
    'yardimci',
    
    # Hızlı erişim
    'anuite_hesapla',
    
    # Tek ödeme
    'tek_odeme_bd',
    'tek_odeme_gd',
    'tek_odeme_faiz',
    'tek_odeme_sure',
    'iskonto_faktoru_hesapla',
    'birikim_faktoru_hesapla',
    
    # Devre sonu
    'ds_bd_hesapla',
    'ds_odeme_bd',
    'ds_sure_bd',
    'ds_faiz_bd',
    'ds_gd_hesapla',
    'ds_odeme_gd',
    'ds_sure_gd',
    'ds_faiz_gd',
    'ds_pesin_faktor',
    'ds_gelecek_faktor',
    'ds_tablo',
    
    # Devre başı
    'db_bd_hesapla',
    'db_odeme_bd',
    'db_sure_bd',
    'db_faiz_bd',
    'db_gd_hesapla',
    'db_odeme_gd',
    'db_sure_gd',
    'db_faiz_gd',
    'db_pesin_faktor',
    'db_gelecek_faktor',
    'db_tablo',
    
    # Sürekli anüite
    'surekli_ds_bd',
    'surekli_ds_odeme',
    'surekli_ds_faiz',
    'surekli_db_bd',
    'surekli_db_odeme',
    'surekli_db_faiz',
    'ertelenmis_surekli_anuite',
    
    # Ertelenmiş anüite (YENİ!)
    'ert_ds_bd',
    'ert_ds_gd',
    'ert_ds_taksit_bd',
    'ert_ds_taksit_gd',
    'ert_db_bd',
    'ert_db_gd',
    'ert_db_taksit_bd',
    'ert_gecikme_hesapla',
    'ert_faiz_hesapla',
    'ert_sure_hesapla',
    'ert_cabuklas_bd',
    
    # Geometrik anüite (YENİ!)
    'geo_ds_bd',
    'geo_ds_gd',
    'geo_db_bd',
    'geo_db_gd',
    'geo_ilk_taksit_bd',
    'geo_ilk_taksit_gd',
    'geo_faiz_hesapla',
    'geo_sure_hesapla',
    
    # Aritmetik anüite (YENİ!)
    'arit_ds_bd',
    'arit_ds_gd',
    'arit_ds_ilk_taksit_bd',
    'arit_ds_ilk_taksit_gd',
    'arit_ds_degisim',
    'arit_db_bd',
    'arit_db_gd',
    'arit_db_ilk_taksit_bd',
    'arit_faiz_hesapla',
    'arit_sure_hesapla',
    
    # Çabuklaştırılmış anüite (YENİ!)
    'cab_ds_bd',
    'cab_ds_gd',
    'cab_db_bd',
    'cab_db_gd',
    'cab_taksit_bd',
    'cab_taksit_gd',
    'cab_sure_hesapla',
    'cab_faiz_hesapla',
    'cab_donem_hesapla',
    
    # Yardımcı
    'efektif_faiz_orani',
    'nominal_faiz_orani',
    'surekli_faiz_orani',
    'efektif_from_surekli',
    'faizden_iskonto_orani',
    'iskontodan_faiz_orani',
    'reel_faiz_orani',
    'nominal_from_reel',
    'iskonto_faktoru',
    'birikim_faktoru',
    'toplam_odeme_hesapla',
    'toplam_faiz_hesapla',
    'ortalama_vade_hesapla',
    'yillik_aylik_cevir',
    'aylik_yillik_cevir',
    'gunluk_yillik_cevir',
    'yillik_gunluk_cevir',
]