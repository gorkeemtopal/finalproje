
import pandas as pd  
from Personel import Personel  
from Doktor import Doktor  
from Hemsire import Hemsire  
from Hasta import Hasta  

personel1 = Personel(1, "Ahmet", "Yılmaz", "Muhasebe", 5000)
personel2 = Personel(2, "Mehmet", "Kaya", "IT", 7000)


doktor1 = Doktor(3, "Ali", "Demir", "Cerrahi", 10000, "Genel Cerrahi", 6, "Acıbadem")
doktor2 = Doktor(4, "Ayşe", "Yıldız", "Dahiliye", 12000, "Dahiliye", 8, "Memorial")
doktor3 = Doktor(5, "Fatma", "Kaya", "Kardiyoloji", 9000, "Kardiyoloji", 4, "Florence Nightingale")


hemsire1 = Hemsire(6, "Zeynep", "Aydın", "Cerrahi", 5000, 40, "Yoğun Bakım Sertifikası", "Acıbadem")
hemsire2 = Hemsire(7, "Elif", "Bulut", "Dahiliye", 5500, 36, "Pediatri Sertifikası", "Memorial")
hemsire3 = Hemsire(8, "Hakan", "Öz", "Kardiyoloji", 6000, 38, "Acil Servis Sertifikası", "Florence Nightingale")


hasta1 = Hasta(1, "Ali", "Çelik", "1985-03-25", "Grip", "İstirahat")
hasta2 = Hasta(2, "Veli", "Ak", "1992-07-15", "Kırık", "Alçı")
hasta3 = Hasta(3, "Ayşe", "Güneş", "2000-12-05", "Soğuk Algınlığı", "İlaç")

try:
    
    print(personel1)
    print(personel2)

    
    print(doktor1)
    print(doktor2)
    print(doktor3)

    
    print(hemsire1)
    print(hemsire2)
    print(hemsire3)


    print(hasta1)
    print(hasta2)
    print(hasta3)
except Exception as e:
    print(f"Hata: {e}")  


data = {
    'Personel No': [personel1.get_personel_no(), personel2.get_personel_no(), doktor1.get_personel_no(),
                    doktor2.get_personel_no(), doktor3.get_personel_no(), hemsire1.get_personel_no(),
                    hemsire2.get_personel_no(), hemsire3.get_personel_no(), hasta1.get_hasta_no(),
                    hasta2.get_hasta_no(), hasta3.get_hasta_no()],
    'Ad': [personel1.get_ad(), personel2.get_ad(), doktor1.get_ad(), doktor2.get_ad(), doktor3.get_ad(),
           hemsire1.get_ad(), hemsire2.get_ad(), hemsire3.get_ad(), hasta1.get_ad(), hasta2.get_ad(), hasta3.get_ad()],
    'Soyad': [personel1.get_soyad(), personel2.get_soyad(), doktor1.get_soyad(), doktor2.get_soyad(),
              doktor3.get_soyad(), hemsire1.get_soyad(), hemsire2.get_soyad(), hemsire3.get_soyad(), hasta1.get_soyad(),
              hasta2.get_soyad(), hasta3.get_soyad()],
    'Departman': [personel1.get_departman(), personel2.get_departman(), doktor1.get_departman(),
                  doktor2.get_departman(), doktor3.get_departman(), hemsire1.get_departman(), hemsire2.get_departman(),
                  hemsire3.get_departman(), None, None, None],
    'Maaş': [personel1.get_maas(), personel2.get_maas(), doktor1.get_maas(), doktor2.get_maas(), doktor3.get_maas(),
             hemsire1.get_maas(), hemsire2.get_maas(), hemsire3.get_maas(), None, None, None],
    'Uzmanlık': [None, None, doktor1.get_uzmanlik(), doktor2.get_uzmanlik(), doktor3.get_uzmanlik(), None, None, None,
                 None, None, None],
    'Deneyim Yılı': [None, None, doktor1.get_deneyim_yili(), doktor2.get_deneyim_yili(), doktor3.get_deneyim_yili(),
                     None, None, None, None, None, None],
    'Hastane': [None, None, doktor1.get_hastane(), doktor2.get_hastane(), doktor3.get_hastane(), hemsire1.get_hastane(),
                hemsire2.get_hastane(), hemsire3.get_hastane(), None, None, None],
    'Çalışma Saati': [None, None, None, None, None, hemsire1.get_calisma_saati(), hemsire2.get_calisma_saati(),
                      hemsire3.get_calisma_saati(), None, None, None],
    'Sertifika': [None, None, None, None, None, hemsire1.get_sertifika(), hemsire2.get_sertifika(),
                  hemsire3.get_sertifika(), None, None, None],
    'Hasta No': [None, None, None, None, None, None, None, None, hasta1.get_hasta_no(), hasta2.get_hasta_no(),
                 hasta3.get_hasta_no()],
    'Doğum Tarihi': [None, None, None, None, None, None, None, None, hasta1.get_dogum_tarihi(),
                     hasta2.get_dogum_tarihi(), hasta3.get_dogum_tarihi()],
    'Hastalık': [None, None, None, None, None, None, None, None, hasta1.get_hastalik(), hasta2.get_hastalik(),
                 hasta3.get_hastalik()],
    'Tedavi': [None, None, None, None, None, None, None, None, hasta1.get_tedavi(), hasta2.get_tedavi(),
               hasta3.get_tedavi()]
}

df = pd.DataFrame(data)  


df = df.fillna(0)  


df['Doğum Tarihi'] = pd.to_datetime(df['Doğum Tarihi'], errors='coerce') 


doktor_grup = df[df['Uzmanlık'] != 0].groupby('Uzmanlık').size()
print("\nDoktorları uzmanlık alanlarına göre gruplandırarak toplam sayısı:\n", doktor_grup)


deneyim_fazla_5 = df[(df['Deneyim Yılı'] > 5) & (df['Deneyim Yılı'] != 0)].shape[0]
print("\n5 yıldan fazla deneyime sahip doktorların toplam sayısı:", deneyim_fazla_5)


hasta_df = df[df['Hasta No'] != 0].sort_values(by='Ad')
print("\nHasta adına göre alfabetik olarak sıralanmış DataFrame:\n", hasta_df)


maas_7000_ustu = df[df['Maaş'] > 7000]
print("\nMaaşı 7000 TL üzerinde olan personeller:\n", maas_7000_ustu)


dogum_1990_sonrasi = df[(df['Doğum Tarihi'] != 0) & (df['Doğum Tarihi'] >= '1990-01-01')]
print("\nDoğum tarihi 1990 ve sonrası olan hastalar:\n", dogum_1990_sonrasi)


yeni_df = df[['Ad', 'Soyad', 'Departman', 'Maaş', 'Uzmanlık', 'Deneyim Yılı', 'Hastalık', 'Tedavi']]
print("\nYeni DataFrame:\n", yeni_df)
