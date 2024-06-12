# Hemsire.py
from Personel import Personel  # Personel sınıfını import ediyoruz

class Hemsire(Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)  # Personel sınıfının initializer'ını çağırıyoruz
        self.__calisma_saati = calisma_saati  # Çalışma saati
        self.__sertifika = sertifika  # Sertifika
        self.__hastane = hastane  # Hastane

    # Getter metotları
    def get_calisma_saati(self):
        return self.__calisma_saati

    def get_sertifika(self):
        return self.__sertifika

    def get_hastane(self):
        return self.__hastane

    # Setter metotları
    def set_calisma_saati(self, calisma_saati):
        self.__calisma_saati = calisma_saati

    def set_sertifika(self, sertifika):
        self.__sertifika = sertifika

    def set_hastane(self, hastane):
        self.__hastane = hastane

    # Maaşı belirli bir oranda artıran metot
    def maas_arttir(self, oran):
        self.set_maas(self.get_maas() * (1 + oran))

    # Hemşire bilgilerini döndüren özel __str__ metodu
    def __str__(self):
        return super().__str__() + f", Çalışma Saati: {self.__calisma_saati}, Sertifika: {self.__sertifika}, Hastane: {self.__hastane}"
