from Dil_Kontrol import Dil_Kontrol
from Sifreleme_Yontemleri import Sifreleme_Yontemleri
from Help import Dil_Kontrol_Help, Sifreleme_Yontemleri_Help, Modul_Help


class Modul():
    def __init__(self) -> None:
        self._dil_kontrol = Dil_Kontrol()
        self._sifreleme = Sifreleme_Yontemleri()
        self._dil_help = Dil_Kontrol_Help()
        self._modul_help = Modul_Help()
        self._sifreleme_help = Sifreleme_Yontemleri_Help()
        self._okunan_dosya = ""

    @property
    def help(self):
        print(self._modul_help.help)
        print(self._modul_help.dosya_oku)
        print(self._modul_help.dosyaya_yaz)
        print(self._modul_help.cumlelere_ayir)
        print(self._modul_help.cumle_sayisi)
        print(self._modul_help.kelimelere_ayir)
        print(self._modul_help.kelime_sayisi)
        print(self._modul_help.sesli_harf_sayisi)
        print(self._modul_help.buyuk_unlu_uyumu)
        print(self._dil_help.cumlelere_ayir)
        print(self._dil_help.cumle_sayisi)
        print(self._dil_help.kelimelere_ayir)
        print(self._dil_help.kelime_sayisi)
        print(self._dil_help.sesli_harf_sayisi)
        print(self._dil_help.buyuk_unlu_uyumu)
        print(self._sifreleme_help.simetrik_sifreleme_1)
        print(self._sifreleme_help.simetrik_sifreleme_1_coz)
        print(self._sifreleme_help.simetrik_sifreleme_2)
        print(self._sifreleme_help.simetrik_sifreleme_2_coz)
        print(self._sifreleme_help.hash_sifreleme_1_MD5)
        print(self._sifreleme_help.hash_sifreleme_2_MD5)
        print(self._sifreleme_help.hash_sifreleme_3_MD5)
        print(self._sifreleme_help.hash_sifreleme_4_SHA)
        print(self._sifreleme_help.hash_sifreleme_5_SHA)

    def dosyayi_oku(self, dosya_adi: str):
        try:
            with open(f"{dosya_adi}.txt") as f:
                self._okunan_dosya = f.read()
        except FileNotFoundError:
            print("\nDosya bulunamadı! Şimdi oluşturulacak, lütfen içini doldurunuz.\n")
            with open(f"{dosya_adi}.txt", "w") as f:
                f.write(input("Dosya içine ne yazılsın?:\n"))
            with open(f"{dosya_adi}.txt") as f:
                self._okunan_dosya = f.read()

    def dosyaya_yaz(self, dosya_adi: str, kaydirma_adimi: int, tuzluk: str):
        try:
            yazilacak_metin = self.cumle_sayisi(self._okunan_dosya)
            cumleler = self.cumlelere_ayir(self._okunan_dosya)
            for cumle in cumleler:
                yazilacak_metin += f"\n{cumle}"
            yazilacak_metin = str(yazilacak_metin)
            yazilacak_metin += f"\n{self.kelime_sayisi(self._okunan_dosya)}"
            kelimeler = self.kelimelere_ayir(self._okunan_dosya)
            for kelime in kelimeler:
                yazilacak_metin += f"\n{kelime}"
            yazilacak_metin += f"\n{self.sesli_harf_sayisi(self._okunan_dosya)}"
            yazilacak_metin += f"\n{self.buyuk_unlu_uyumu(self._okunan_dosya)}"

            yazilacak_metin += f"\n\nSimetrik 1"
            for cumle in cumleler:
                yazilacak_metin += f"\n{self._sifreleme.simetrik_sifreleme_1(cumle)}"

            yazilacak_metin += f"\n\nSimetrik 2"
            for cumle in cumleler:
                yazilacak_metin += f"\n{self._sifreleme.simetrik_sifreleme_2(cumle,int(kaydirma_adimi))}"

            yazilacak_metin += f"\n\nMD5 1"
            for cumle in cumleler:
                yazilacak_metin += f"\n{self._sifreleme.hash_sifreleme_1_MD5(cumle)}"

            yazilacak_metin += f"\n\nMD5 2"
            for cumle in cumleler:
                yazilacak_metin += f"\n{self._sifreleme.hash_sifreleme_2_MD5(cumle,str(tuzluk))}"

            yazilacak_metin += f"\n\nMD5 3"
            for cumle in cumleler:
                yazilacak_metin += f"\n{self._sifreleme.hash_sifreleme_3_MD5(cumle)}"

            yazilacak_metin += f"\n\nSHA 1"
            for cumle in cumleler:
                yazilacak_metin += f"\n{self._sifreleme.hash_sifreleme_4_SHA(cumle)}"

            yazilacak_metin += f"\n\nSHA 2"
            for cumle in cumleler:
                yazilacak_metin += f"\n{self._sifreleme.hash_sifreleme_5_SHA(cumle,str(tuzluk))}"

            with open(f"{dosya_adi}_kayit.txt", "w") as f:
                f.write(yazilacak_metin)
        except Exception as ex:
            print(ex)

    def cumlelere_ayir(self, metin: str):
        cumle_listesi = []
        for cumle in self._dil_kontrol.cumlelere_ayir(str(metin)):
            cumle_listesi.append(cumle)
        return cumle_listesi

    def cumle_sayisi(self, metin: str):
        return f"Metin içindeki cümle sayısı: {self._dil_kontrol.cumle_sayisi(str(metin))}"

    def kelimelere_ayir(self, metin: str):
        kelime_listesi = []
        for kelime in self._dil_kontrol.kelimelere_ayir(str(metin)):
            kelime_listesi.append(kelime)
        return kelime_listesi

    def kelime_sayisi(self, metin: str):
        return f"\nMetin içindeki kelime sayısı: {self._dil_kontrol.kelime_sayisi(str(metin))}"

    def sesli_harf_sayisi(self, metin: str):
        return f"\nMetin içinde toplam {self._dil_kontrol.sesli_harf_sayisi(str(metin))[0]} adet sesli harf varken, \
{self._dil_kontrol.sesli_harf_sayisi(str(metin))[1]} adet benzersiz sesli harf vardır."

    def buyuk_unlu_uyumu(self, metin: str):
        uyan, uymayan = self._dil_kontrol.buyuk_unlu_uyumu(str(metin))
        return f"\nMetin içinde büyük ünlü uyumuna uyan kelime sayısı: {uyan}, uymayan kelime sayısı: {uymayan}"


mod = Modul()

mod.dosyayi_oku("oncado")
mod.dosyaya_yaz("ciktilar", 29, "29 Aralık Çarşamba")

# mod.help
