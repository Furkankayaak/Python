def normalize_olasiliklar(olasiliklar):
    return [olasilik / 100 for olasilik in olasiliklar]

def risk_altinda_karar_ver(dogal_durumlar, alternatifler, olasiliklar, getiriler):
    beklenen_degerler = [0] * len(alternatifler)
    tam_bilgi_beklenen_deger = 0
    tam_bilginin_beklenen_degeri = 0
    firsat_kayiplari = [0] * len(alternatifler)

    # Tüm doğal durumları dön ve olasılıkları kullanarak beklenen değeri hesapla
    for i, durum in enumerate(dogal_durumlar):
        for j, alternatif in enumerate(alternatifler):
            getiri = getiriler[alternatif][i]
            beklenen_degerler[j] += olasiliklar[i] * getiri

    en_iyi_alternatif_beklenen_deger = max(beklenen_degerler)
    
    for i, durum in enumerate(dogal_durumlar):
        en_iyi_alternatif_getiri = max(getiriler[alternatif][i] for alternatif in alternatifler)
        tam_bilgi_beklenen_deger += olasiliklar[i] * en_iyi_alternatif_getiri

    tam_bilginin_beklenen_degeri = tam_bilgi_beklenen_deger - en_iyi_alternatif_beklenen_deger

    for i, alternatif in enumerate(alternatifler):
        firsat_kayiplari[i] = tam_bilgi_beklenen_deger - beklenen_degerler[i]

    # En düşük fırsat kaybına sahip alternatifi bul
    en_dusuk_firsat_kaybi = min(firsat_kayiplari)
    secilen_alternatif = alternatifler[firsat_kayiplari.index(en_dusuk_firsat_kaybi)]

    return beklenen_degerler, tam_bilgi_beklenen_deger, tam_bilginin_beklenen_degeri, firsat_kayiplari, secilen_alternatif

# Kullanıcıdan girişleri al
dogal_durum_sayisi = int(input("Doğal Durum Sayısı: "))
alternatif_sayisi = int(input("Alternatif Sayısı: "))

dogal_durumlar = [input(f"Doğal Durum {i+1}: ") for i in range(dogal_durum_sayisi)]
alternatifler = [input(f"Alternatif {i+1}: ") for i in range(alternatif_sayisi)]
olasiliklar = [float(input(f"Olasılık {i+1} (%): ")) for i in range(dogal_durum_sayisi)]

# Olasılıkları normalize et
normalized_olasiliklar = normalize_olasiliklar(olasiliklar)

getiriler = {alternatif: [float(input(f"{alternatif} için {durum} getirisi: ")) for durum in dogal_durumlar] for alternatif in alternatifler}

# Fonksiyonları çağır
beklenen_degerler, tam_bilgi_beklenen_deger, tam_bilginin_beklenen_degeri, firsat_kayiplari, secilen_alternatif = risk_altinda_karar_ver(dogal_durumlar, alternatifler, normalized_olasiliklar, getiriler)

# Sonuçları yazdır
print("Seçilen Alternatif:", secilen_alternatif)