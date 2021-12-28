class Dil_Kontrol():
    def __init__(self) -> None:
        self.kalin_unluler = ["a", "ı", "o", "u"]
        self.ince_unluler = ["e", "i", "ö", "ü"]
        self.sesli_harfler = ["a", "e", "ı", "i", "u", "ü", "o", "ö"]

    def cumlelere_ayir(self, metin: str):
        cumleler = metin.split(".")
        return [cumle.strip() for cumle in cumleler if len(cumle) > 0]

    def cumle_sayisi(self, metin: str):
        return len(self.cumlelere_ayir(metin))

    def kelimelere_ayir(self, metin: str):
        kelimeler = metin.replace(".", " ").replace(
            ",", " ").replace(";", " ").replace(":", " ").replace("...", " ").replace("?", " ").replace("!", " ").split(" ")
        kirpilmis_kelimeler = [kelime.strip()
                               for kelime in kelimeler if len(kelime) > 0]
        return kirpilmis_kelimeler

    def kelime_sayisi(self, metin: str):
        return len(self.kelimelere_ayir(metin))

    def sesli_harf_sayisi(self, metin: str):
        sayac_toplam = [harf for harf in metin if harf in self.sesli_harfler]
        sayac_unic = set(sayac_toplam)
        return len(sayac_toplam), len(sayac_unic)

    def buyuk_unlu_uyumu(self, metin: str):
        uyan = uymayan = 0
        kelime_listesi = self.kelimelere_ayir(metin)
        for kelime in kelime_listesi:
            sesli_harf_sayisi = self.sesli_harf_sayisi(kelime)
            kalin_unlu_sayisi = len(
                set([harf for harf in kelime if harf in self.kalin_unluler and self.sesli_harfler]))
            ince_unlu_sayisi = len(
                set([harf for harf in kelime if harf in self.ince_unluler and self.sesli_harfler]))
            if (len(kelime) > 1):
                if(sesli_harf_sayisi[1] == kalin_unlu_sayisi) or ((sesli_harf_sayisi[1] == ince_unlu_sayisi)):
                    uyan += 1
                else:
                    uymayan += 1
        return uyan, uymayan
