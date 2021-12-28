class Help_Base():
    def __init__(self) -> None:
        self.fonksiyon_adi = ""
        self.sinif_adi = ""

    def bilgi(self, sinif_adi: str, fonksiyon_adi: str, kullanim: str, ornek: str):
        yardim_mesaji = f"""{"~"*100}
        '{sinif_adi}' sınıfında bulunan;
        '{fonksiyon_adi}' fonksiyonu:
        {kullanim} 
        Örnek kullanım:
        {ornek}
        """
        return yardim_mesaji


class Dil_Kontrol_Help(Help_Base):
    def __init__(self) -> None:
        super().__init__()
        self.sinif_adi = "Dil_Kontrol"

    @property
    def cumlelere_ayir(self):
        self.fonksiyon_adi = "cumlelere_ayir"
        kullanim = """
        \tFonksiyon str tipinde bir parametre alır.
        \tBu parametre '.' (nokta) işaretine göre split işlemine tabi tutulup bir listeye atılır.
        \tListe 'list comprehension' yöntemiyle cümlelere ayrılır. '[cumle.strip() for cumle in cumleler if len(cumle) > 0]'
        \tGeriye her elemanı bir cümle olan bir liste döndürülür.
        """
        ornek = """cumlelere_ayir("örnek metni")"""
        return self.bilgi(self.sinif_adi, self.fonksiyon_adi, kullanim, ornek)

    @property
    def cumle_sayisi(self):
        self.fonksiyon_adi = "cumle_sayisi"
        kullanim = """
        \tFonksiyon str tipinde bir parametre alır.
        \tBu parametre cumlelere_ayir fonksiyonuna gönderilir.
        \tListe len() fonksiyonuna paremetre olrak verilir.
        \tlen() fonksiyonundan gelen değer geriye döndürülür.        
        """
        ornek = """cumle_sayisi("örnek metni")"""
        return self.bilgi(self.sinif_adi, self.fonksiyon_adi, kullanim, ornek)

    @property
    def kelimelere_ayir(self):
        self.fonksiyon_adi = "kelimelere_ayir"
        kullanim = """
        \tFonksiyon str tipinde bir parametre alır.
        \tBu parametre sırasıyla replace(".", " ") ve split(" ") işlemleri uygulanır.
        \tMetin 'list comprehension' yöntemiyle kelimelere ayrılır. '[kelime.strip() for kelime in kelimeler if len(kelime) > 0]'
        \tGeriye her elemanı bir cümle olan bir liste döndürülür.
        """
        ornek = """kelimelere_ayir("örnek metni")"""
        return self.bilgi(self.sinif_adi, self.fonksiyon_adi, kullanim, ornek)

    @property
    def kelime_sayisi(self):
        self.fonksiyon_adi = "kelime_sayisi"
        kullanim = """
        \tFonksiyon str tipinde bir parametre alır.
        \tBu parametre kelimelere_ayir fonksiyonuna gönderilir.
        \tListe len() fonksiyonuna paremetre olrak verilir.
        \tlen() fonksiyonundan gelen değer geriye döndürülür.   
        """
        ornek = """kelime_sayisi("örnek metni")"""
        return self.bilgi(self.sinif_adi, self.fonksiyon_adi, kullanim, ornek)

    @property
    def sesli_harf_sayisi(self):
        self.fonksiyon_adi = "sesli_harf_sayisi"
        kullanim = """
        \tFonksiyon str tipinde bir parametre alır.
        \tBu arametre sesli_harfler = ["a", "e", "ı", "i", "u", "ü", "o", "ö"] listesindeki elemanlar kullanılarak
        sayac_toplam adlı listeye 'list comprehension' yöntemi ile metin içindeki sesli harfler atılır. '[harf for harf in metin if harf in self.sesli_harfler]'
        \tsayac_toplam adlı liste set fonksiyonu ile sayac_unic adlı kümeye aktarılır, böylece harfler kendini tekrar etmemiş olur.
        \tListeler sırasıyla len() fonksiyonuna paremetre olrak verilir.
        \tlen() fonksiyonundan gelen değerler geriye döndürülür.   
        """
        ornek = """sesli_harf_sayisi("örnek metni")"""
        return self.bilgi(self.sinif_adi, self.fonksiyon_adi, kullanim, ornek)

    @property
    def buyuk_unlu_uyumu(self):
        self.fonksiyon_adi = "buyuk_unlu_uyumu"
        kullanim = """
        \tFonksiyon str tipinde bir parametre alır.
        \tFonksiyon içinde başlangıç değerleri 0 olan 'uyan' ve 'uymayan' adlı değişkenler vardır.
        \tBu parametre kelimelere_ayir fonksiyonuna parametre olarak gönderilir ve gelen kelime listesi kelime_listesi adlı listeye atanır.
        \tkelime listesi 'for döngüsüne' sokulur, listedeki her kelime için sırasıyla;
        \t\tsesli_harf_sayisi fonksiyonu kullanılarak sesli harf sayısı belirlenir,
        \t\tkalin_unluler = ["a", "ı", "o", "u"] listesi kullanılarak len(set([harf for harf in kelime if harf in self.kalin_unluler and self.sesli_harfler])), yöntemi ile kelime içindeki kalın ünlü sayısı belirlenir
        \t\tince_unluler = ["e", "i", "ö", "ü"] listesi kullanılarak len(set([harf for harf in kelime if harf in self.ince_unluler and self.sesli_harfler])), yöntemi ile kelime içindeki ince ünlü sayısı belirlenir
        \t\tEğer sesli_harf_sayisi kelimedeki kalın ünlü sayısıya eşitse ya da sesli_harf_sayisi kelimedeki ince ünlü sayısına eşitse 'uyan' değişkeni, aksi taktirse 'uymayan' değişkeninin değeri 1 artırırlır
        \t\t'uyan' ve 'uymayan' adlı değişkenlerin değerleri geriye döndürülür.
        """
        ornek = """sesli_harf_sayisi("örnek metni")"""
        return self.bilgi(self.sinif_adi, self.fonksiyon_adi, kullanim, ornek)


class Sifreleme_Yontemleri_Help(Help_Base):
    def __init__(self) -> None:
        super().__init__()
        self.sinif_adi = "Sifreleme_Yontemleri"

    @property
    def simetrik_sifreleme_1(self):
        self.fonksiyon_adi = "simetrik_sifreleme_1"
        kullanimi = """
        \tFonksiyon str tipinde bir parametre alır.
        \tMetindeki her bir harf önceden belirlenmiş adım sayısı kadar alfabe listesinde kayar.
        \tİşlemler bittiğinde şifrelenmiş metin ters sıraya sokulur.
        \tGeriye şifrelenmiş metni döner.
        """
        ornek = """simetrik_sifreleme_1(metin)"""
        return self.bilgi(self.sinif_adi, self.fonksiyon_adi, kullanimi, ornek)

    @property
    def simetrik_sifreleme_1_coz(self):
        self.fonksiyon_adi = "simetrik_sifreleme_1_coz"
        kullanimi = """
        \tFonksiyon str tipinde bir parametre alır.
        \tMetindeki her bir harf önceden belirlenmiş adım sayısı kadar alfabe listesinde kayar.
        \tİşlemler bittiğinde şifresi çözümlenmiş metin ters sıraya sokulur.
        \tGeriye şifresi çözülmüş metni döner.
        """
        ornek = """simetrik_sifreleme_1_coz(metin)"""
        return self.bilgi(self.sinif_adi, self.fonksiyon_adi, kullanimi, ornek)

    @property
    def simetrik_sifreleme_2(self):
        self.fonksiyon_adi = "simetrik_sifreleme_2"
        kullanimi = """
        \tFonksiyon str tipinde ve int tipinde parametreler alır.
        \tMetindeki her bir harf parametre olarak verilmiş adım sayısı kadar alfabe listesinde kayar.
        \tİşlemler bittiğinde şifrelenmiş metin ters sıraya sokulur.
        \tGeriye şifrelenmiş metni döner.
        """
        ornek = """simetrik_sifreleme_2(metin,adım)"""
        return self.bilgi(self.sinif_adi, self.fonksiyon_adi, kullanimi, ornek)

    @property
    def simetrik_sifreleme_2_coz(self):
        self.fonksiyon_adi = "simetrik_sifreleme_2_coz"
        kullanimi = """
        \tFonksiyon str tipinde ve int tipinde parametreler alır.
        \tMetindeki her bir harf parametre olarak verilmiş adım sayısı kadar alfabe listesinde kayar.
        \tİşlemler bittiğinde şifrelenmiş metin ters sıraya sokulur.
        \tGeriye şifrelenmiş metni döner.
        """
        ornek = """simetrik_sifreleme_2_coz(metin,adım)"""
        return self.bilgi(self.sinif_adi, self.fonksiyon_adi, kullanimi, ornek)

    @property
    def hash_sifreleme_1_MD5(self):
        self.fonksiyon_adi = "hash_sifreleme_1_MD5"
        kullanimi = """
        \tFonksiyon str tipinde bir parametre alır.
        \tMetindeki her bir harf hexadesimal formata çevrilir.
        \tŞifrelenmiş metin 32 karakter olana kadar ilk ve son karakterleri, hex listesindeki indeksleri toplanıp, 16 tabanında modu alınalar tekrar hexadesimal formata döndürülür.
        \tBu işlem şifrelenmiş metin 32 karakter olana kadar devam eder.
        \tİşlemler bittiğinde şifrelenmiş metin ters sıraya sokulur.
        \tGeriye şifrelenmiş metni döner.
        """
        ornek = """hash_sifreleme_1_MD5(metin)"""
        return self.bilgi(self.sinif_adi, self.fonksiyon_adi, kullanimi, ornek)

    @property
    def hash_sifreleme_2_MD5(self):
        self.fonksiyon_adi = "hash_sifreleme_2_MD5"
        kullanimi = """
        \tFonksiyon str tipinde iki parametre alır.
        \tİlk parametre şifrelenmek istenen metin bilgisidir.
        \tİkinci parametre ise şifrelemeyi artırmak için metnin önüne eklenecek olan güvenlik kodudur.
        \tMetindeki her bir harf hexadesimal formata çevrilir.
        \tŞifrelenmiş metin 32 karakter olana kadar ilk ve son karakterleri, hex listesindeki indeksleri toplanıp, 16 tabanında modu alınalar tekrar hexadesimal formata döndürülür.
        \tBu işlem şifrelenmiş metin 32 karakter olana kadar devam eder.
        \tİşlemler bittiğinde şifrelenmiş metin ters sıraya sokulur.
        \tGeriye şifrelenmiş metni döner.
        """
        ornek = """hash_sifreleme_2_MD5(metin, guvenlik_kodu)"""
        return self.bilgi(self.sinif_adi, self.fonksiyon_adi, kullanimi, ornek)

    @property
    def hash_sifreleme_3_MD5(self):
        self.fonksiyon_adi = "hash_sifreleme_3_MD5"
        kullanimi = """
        \tFonksiyon str tipinde bir parametre alır.
        \tMetindeki her bir harf hexadesimal formata çevrilir.
        \tMetin ters sıraya sokulur.
        \tŞifrelenmiş metin 32 karakter olana kadar ilk ve son karakterleri, hex listesindeki indeksleri toplanıp, 16 tabanında modu alınalar tekrar hexadesimal formata döndürülür.
        \tBu işlem şifrelenmiş metin 32 karakter olana kadar devam eder.
        \tİşlemler bittiğinde şifrelenmiş metin ters sıraya sokulur.
        \tGeriye şifrelenmiş metni döner.
        """
        ornek = """hash_sifreleme_3_MD5(metin)"""
        return self.bilgi(self.sinif_adi, self.fonksiyon_adi, kullanimi, ornek)

    @property
    def hash_sifreleme_4_SHA(self):
        self.fonksiyon_adi = "hash_sifreleme_4_SHA"
        kullanimi = """
        \tFonksiyon str tipinde bir parametre alır.
        \tMetindeki her bir harf hexadesimal formata çevrilir.
        \tŞifrelenmiş metin 64 karakter olana kadar ilk ve son karakterleri, hex listesindeki indeksleri toplanıp, 16 tabanında modu alınalar tekrar hexadesimal formata döndürülür.
        \tBu işlem şifrelenmiş metin 64 karakter olana kadar devam eder.
        \tİşlemler bittiğinde şifrelenmiş metin ters sıraya sokulur.
        \tGeriye şifrelenmiş metni döner.
        """
        ornek = """hash_sifreleme_4_SHA(metin)"""
        return self.bilgi(self.sinif_adi, self.fonksiyon_adi, kullanimi, ornek)

    @property
    def hash_sifreleme_5_SHA(self):
        self.fonksiyon_adi = "hash_sifreleme_5_SHA"
        kullanimi = """
        \tFonksiyon str tipinde iki parametre alır.
        \tİlk parametre şifrelenmek istenen metin bilgisidir.
        \tİkinci parametre ise şifrelemeyi artırmak için metnin önüne eklenecek olan güvenlik kodudur.
        \tMetindeki her bir harf hexadesimal formata çevrilir.
        \tŞifrelenmiş metin 64 karakter olana kadar ilk ve son karakterleri, hex listesindeki indeksleri toplanıp, 16 tabanında modu alınalar tekrar hexadesimal formata döndürülür.
        \tBu işlem şifrelenmiş metin 64 karakter olana kadar devam eder.
        \tİşlemler bittiğinde şifrelenmiş metin ters sıraya sokulur.
        \tGeriye şifrelenmiş metni döner.
        """
        ornek = """hash_sifreleme_5_SHA(metin, guvenlik_kodu)"""
        return self.bilgi(self.sinif_adi, self.fonksiyon_adi, kullanimi, ornek)


class Modul_Help(Help_Base):
    def __init__(self) -> None:
        super().__init__()
        self.sinif_adi = "Modul"

    @property
    def help(self):
        self.fonksiyon_adi = "help"
        kullanimi = """
        \tFonksiyon property'dir herhangi bir parametre almaz.
        \tModül hakkında genel bilgi verir.
        """
        ornek = """help"""
        return self.bilgi(self.sinif_adi, self.fonksiyon_adi, kullanimi, ornek)

    @property
    def dosya_oku(self):
        self.fonksiyon_adi = "dosya_oku"
        kullanimi = """
        \tFonksiyon okunacak dosyanın adını parametre olarak alır.
        \tDosya dizinde varsa okunur, yok ise oluşturulup okunur.
        \tGeriye okunan dosyanın içeriğini döndürür.
        """
        ornek = """dosya_oku(okunacak)"""
        return self.bilgi(self.sinif_adi, self.fonksiyon_adi, kullanimi, ornek)

    @property
    def dosyaya_yaz(self):
        self.fonksiyon_adi = "dosyaya_yaz"
        kullanimi = """
            \tFonksiyon yazılacak dosyanın adını, şifrelemede kullanılacak adım sayısını ve yine şifrelemede kullanılacak "tuzluk" ek önlem metnini parametre olarak alır.
            \tFonksiyon içerisinde Dil_Kontrol ve Sifreleme_Yontemleri sınıflarının fonksiyonları kullanılarak okunan metin üzerinde işlemler gerçekleştirilir.
            \tDaha önce okunmuş olan dosyanın içeriğini işlemler gerçekleştirdikten sonra başka bir doyaya kaydeder.
            """
        ornek = """dosyaya_yaz(yazılacak, 15, python)"""
        return self.bilgi(self.sinif_adi, self.fonksiyon_adi, kullanimi, ornek)

    @property
    def cumlelere_ayir(self):
        self.fonksiyon_adi = "cumlelere_ayir"
        kullanimi = """
            \tFonksiyon cümlelere ayrılacak metni parametre olarak alır.
            \tDil_Kontrol sınıfındaki cumlelere_ayir fonksiyonuna parametre olarak geçer.
            \tGeriye bilgilendirme mesajı ve cümlelerin olduğu bir liste döner.
            """
        ornek = """cumlelere_ayir(metin)"""
        return self.bilgi(self.sinif_adi, self.fonksiyon_adi, kullanimi, ornek)

    @property
    def cumle_sayisi(self):
        self.fonksiyon_adi = "cumle_sayisi"
        kullanimi = """
            \tFonksiyon cümlelere ayrılacak metni parametre olarak alır.
            \tDil_Kontrol sınıfındaki cumle_sayisi fonksiyonuna parametre olarak geçer.
            \tGeriye bilgilendirme mesajı ve cümle sayısı döner.
            """
        ornek = """cumle_sayisi(metin)"""
        return self.bilgi(self.sinif_adi, self.fonksiyon_adi, kullanimi, ornek)

    @property
    def kelimelere_ayir(self):
        self.fonksiyon_adi = "cumlelere_ayir"
        kullanimi = """
            \tFonksiyon cümlelere ayrılacak metni parametre olarak alır.
            \tDil_Kontrol sınıfındaki kelimelere_ayir fonksiyonuna parametre olarak geçer.
            \tGeriye bilgilendirme mesajı ve kelimelerin olduğu bir liste döner.
            """
        ornek = """kelimelere_ayir(metin)"""
        return self.bilgi(self.sinif_adi, self.fonksiyon_adi, kullanimi, ornek)

    @property
    def kelime_sayisi(self):
        self.fonksiyon_adi = "kelime_sayisi"
        kullanimi = """
            \tFonksiyon cümlelere ayrılacak metni parametre olarak alır.
            \tDil_Kontrol sınıfındaki kelime_sayisi fonksiyonuna parametre olarak geçer.
            \tGeriye bilgilendirme mesajı ve kelime sayısı döner.
            """
        ornek = """kelime_sayisi(metin)"""
        return self.bilgi(self.sinif_adi, self.fonksiyon_adi, kullanimi, ornek)

    @property
    def sesli_harf_sayisi(self):
        self.fonksiyon_adi = "sesli_harf_sayisi"
        kullanimi = """
            \tFonksiyon cümlelere ayrılacak metni parametre olarak alır.
            \tDil_Kontrol sınıfındaki sesli_harf_sayisi fonksiyonuna parametre olarak geçer.
            \tDil_Kontrol sınıfındaki sesli_harf_sayisi fonksiyonu geriye sesli harflerin toplam sayısını ve terkararsız sesli harflerin sayısını döner.
            \tFonksiyon geriye bilgilendirme mesajı ve sesli harflerin sayılarını döner.
            """
        ornek = """sesli_harf_sayisi(metin)"""
        return self.bilgi(self.sinif_adi, self.fonksiyon_adi, kullanimi, ornek)

    @property
    def buyuk_unlu_uyumu(self):
        self.fonksiyon_adi = "buyuk_unlu_uyumu"
        kullanimi = """
            \tFonksiyon cümlelere ayrılacak metni parametre olarak alır.
            \tDil_Kontrol sınıfındaki buyuk_unlu_uyumu fonksiyonuna parametre olarak geçer.
            \tDil_Kontrol sınıfındaki buyuk_unlu_uyumu fonksiyonu geriye büyük ünli uyumuna uyan ve uymayan kelimelerin sayısını döner.
            \tFonksiyon geriye bilgilendirme mesajı ve kelimelerin sayılarını döner.
            """
        ornek = """buyuk_unlu_uyumu(metin)"""
        return self.bilgi(self.sinif_adi, self.fonksiyon_adi, kullanimi, ornek)
