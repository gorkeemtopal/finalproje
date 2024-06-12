# Doktor.py
from Personel import Personel  # Personel sınıfını import ediyoruz

class Doktor(Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)  # Personel sınıfının initializer'ını çağırıyoruz
        self.__uzmanlik = uzmanlik  # Uzmanlık alanı
        self.__deneyim_yili = deneyim_yili  # Deneyim yılı
        self.__hastane = hastane  # Hastane

    # Getter metotları
    def get_uzmanlik(self):
        return self.__uzmanlik

    def get_deneyim_yili(self):
        return self.__deneyim_yili

    def get_hastane(self):
        return self.__hastane

    # Setter metotları
    def set_uzmanlik(self, uzmanlik):
        self.__uzmanlik = uzmanlik

    def set_deneyim_yili(self, deneyim_yili):
        self.__deneyim_yili = deneyim_yili

    def set_hastane(self, hastane):
        self.__hastane = hastane

    # Maaşı belirli bir oranda artıran metot
    def maas_arttir(self, oran):
        self.set_maas(self.get_maas() * (1 + oran))

    # Doktor bilgilerini döndüren özel __str__ metodu
    def __str__(self):
        return super().__str__() + f", Uzmanlık: {self.__uzmanlik}, Deneyim Yılı: {self.__deneyim_yili}, Hastane: {self.__hastane}"
