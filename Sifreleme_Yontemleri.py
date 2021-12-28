class Sifreleme_Yontemleri():
    def __init__(self) -> None:
        self.alfabe = [
            "a", "𐰢", "0", "𐰸", "A", "𐱂", "{", "𐰀", "Z", "𐰣", "#", "z", "𐰁", "b", "𐰤",  "1", "𐰹",  "B", "[", "𐰂", "Y", "𐰥", "?", "y", "·",
            "𐰃", "c", "𐰦",  "2", "𐰺", "C", "]", "𐰄",  "X", "𐰧", "$", "x", "×", "𐰅", "ç", "𐰨", "3", "𐰻", "Ç", "}", "𐰆",  "V", "𐰩", "=", "v",
            "µ", "𐰇", "d", "𐰪", "4", "𐰼",  "D", "~", "𐰈", "Ü", "𐰫",  ")", "ü", "”", "𐰉", "e", "𐰬", "5", "𐰽", "E", "¢", "𐰊",  "U", "𐰭", "(",
            "u", "<", "𐰋",  "f", "𐰮", "6", "𐰾", "F", ">", "𐰌", "T", "&", "t", "“", "𐰍", "G", "7", "𐰿", "g", "|", "𐰎", "Ş", "%", "ş", "»",
            "𐰏", "Ğ", "8", "𐱀", "ğ", "¾", "𐰐", "S", "*", "s", "«", "𐰑", "G", "9", "𐱁", "g", "é", "𐰒", "R", "𐰯", "_", "r", "´", "𐰓", "ı",
            "𐰰", ".", "I", "£", "𐰔", "P", "𐰱", "\\", "p", "𐰲", "ß", "𐰕", "i", "𐰳", ":", "İ", "½", "𐰖", "Ö", "𐰴", "/", "ö", "←", "𐰗",  "j",
            "𐰵", "J", "`", "𐰘", "O", "-", "𐱄", "ô", "𐱅", "Ô", "o", "¶", "𐰙", "q", ";", "𐰚", "W", "î", "Î", "₺", "𐰛", "N", "+", "n", "€", "𐰜",
            "l", "!", "𐱇", "L", "ª", "𐰝", "M", "û", "𐱆", "'", "𐰞", "m", "@", "k", "𐰟", "Q", "Û", "𐰠", "K", "𐰶", "w", "H", "Â", "𐰡", "h", ",",
            "𐰷", "\n", "â", "𐱃", "𐱈"]

        self.hex = ["0", "1", "2", "3", "4", "5", "6",
                    "7", "8", "9", "A", "B", "C", "D", "E", "F"]

    def simetrik_sifreleme_1(self, metin: str):
        adim = 30
        metin_boyutu = len(metin)
        if metin_boyutu > 0:
            sifreli = ""
            alfabe_boyutu = len(self.alfabe)
            for i in range(metin_boyutu):
                if metin[i] == " ":
                    sifreli += " "
                else:
                    metin_harf_sirasi = self.alfabe.index(metin[i])
                    if (metin_harf_sirasi + adim) >= alfabe_boyutu:
                        metin_harf_sirasi = (
                            metin_harf_sirasi + adim) % alfabe_boyutu
                    else:
                        metin_harf_sirasi = metin_harf_sirasi+adim
                    sifreli += self.alfabe[metin_harf_sirasi]
            sifreli = sifreli[::-1]
            return sifreli
        return f"Şifrelenecek metin bulunamadı"

    def simetrik_sifreleme_1_coz(self, metin: str):
        adim = 30
        metin_boyutu = len(metin)
        if metin_boyutu > 0:
            sifreli = ""
            alfabe_boyutu = len(self.alfabe)
            for i in range(metin_boyutu):
                if metin[i] == " ":
                    sifreli += " "
                else:
                    metin_harf_sirasi = self.alfabe.index(metin[i])
                    if (metin_harf_sirasi - adim) < 0:
                        metin_harf_sirasi = (
                            metin_harf_sirasi - adim) + alfabe_boyutu
                    else:
                        metin_harf_sirasi = metin_harf_sirasi - adim
                    sifreli += self.alfabe[metin_harf_sirasi]
            sifreli = sifreli[::-1]
            return sifreli
        return "Şifrelenecek bulunamadı"

    def simetrik_sifreleme_2(self, metin: str, adim: int):
        metin_boyutu = len(metin)
        if metin_boyutu > 0:
            sifreli = ""
            alfabe_boyutu = len(self.alfabe)
            for i in range(metin_boyutu):
                if metin[i] == " ":
                    sifreli += " "
                else:
                    metin_harf_sirasi = self.alfabe.index(metin[i])
                    if (metin_harf_sirasi + adim) >= alfabe_boyutu:
                        metin_harf_sirasi = (
                            metin_harf_sirasi + adim) % alfabe_boyutu
                    else:
                        metin_harf_sirasi = metin_harf_sirasi+adim
                    sifreli += self.alfabe[metin_harf_sirasi]
            sifreli = sifreli[::-1]
            return sifreli
        return "Şifrelenecek metin bulunamadı"

    def simetrik_sifreleme_2_coz(self, metin: str, adim: int):
        metin_boyutu = len(metin)
        sifreli = ""
        alfabe_boyutu = len(self.alfabe)
        if metin_boyutu > 0:
            for i in range(metin_boyutu):
                if metin[i] == " ":
                    sifreli += " "
                else:
                    metin_harf_sirasi = self.alfabe.index(metin[i])
                    if (metin_harf_sirasi - adim) < 0:
                        metin_harf_sirasi = (
                            metin_harf_sirasi - adim) + alfabe_boyutu
                    else:
                        metin_harf_sirasi = metin_harf_sirasi - adim
                    sifreli += self.alfabe[metin_harf_sirasi]
            sifreli = sifreli[::-1]
            return sifreli
        return "Şifrelenecek metin bulunamadı"

    def hash_sifreleme_1_MD5(self, metin: str):
        boyut = len(metin)
        if boyut > 0:
            metin_hex = ""
            sifreli = ""
            for m in range(boyut):
                if metin[m] != " ":
                    metin_hex += self.hex[self.alfabe.index(metin[m]) % 16]
            if len(metin_hex) % 2 != 0:
                metin_hex += self.hex[0]
            while len(metin_hex) > 0:
                sifreli += self.hex[(self.hex.index(metin_hex[0]) +
                                     self.hex.index(metin_hex[-1])) % 16]
                metin_hex = metin_hex[1:-1]
                if len(sifreli) == 32:
                    break
            while(len(sifreli) < 32):
                sifreli += self.hex[(self.hex.index(sifreli[0]) +
                                     self.hex.index(sifreli[-1])) % 16]
            sifreli = sifreli[::-1]
            return sifreli
        return "Şifrelenecek metin bulunamadı"

    def hash_sifreleme_2_MD5(self, metin: str, guvenlik_kodu: str):
        boyut = len(metin)
        if boyut > 0:
            metin = f"{guvenlik_kodu}{metin}"
            metin_hex = ""
            sifreli = ""
            for m in range(boyut):
                if metin[m] != " ":
                    metin_hex += self.hex[self.alfabe.index(metin[m]) % 16]
            if len(metin_hex) % 2 != 0:
                metin_hex += self.hex[0]
            while len(metin_hex) > 0:
                sifreli += self.hex[(self.hex.index(metin_hex[0]) +
                                     self.hex.index(metin_hex[-1])) % 16]
                metin_hex = metin_hex[1:-1]
                if len(sifreli) == 32:
                    break
            while(len(sifreli) < 32):
                sifreli += self.hex[(self.hex.index(sifreli[0]) +
                                     self.hex.index(sifreli[-1])) % 16]
            sifreli = sifreli[::-1]
            return sifreli
        return "Şifrelenecek metin bulunamadı"

    def hash_sifreleme_3_MD5(self, metin: str):
        boyut = len(metin)
        if boyut > 0:
            metin_hex = ""
            sifreli = ""
            for m in range(boyut):
                if metin[m] != " ":
                    metin_hex += self.hex[self.alfabe.index(metin[m]) % 16]
                    metin_hex += self.hex[m % 16]
            if len(metin_hex) % 2 != 0:
                metin_hex += self.hex[0]
            metin_hex = metin_hex[::-1]
            while len(metin_hex) > 0:
                sifreli += self.hex[(self.hex.index(metin_hex[0]) +
                                     self.hex.index(metin_hex[-1])) % 16]
                metin_hex = metin_hex[1:-1]
                if len(sifreli) == 32:
                    break
            while(len(sifreli) < 32):
                sifreli += self.hex[(self.hex.index(sifreli[0]) +
                                     self.hex.index(sifreli[-1])) % 16]
            sifreli = sifreli[::-1]
            return sifreli
        return "Şifrelenecek metin bulunamadı"

    def hash_sifreleme_4_SHA(self, metin: str):
        boyut = len(metin)
        if boyut > 0:
            metin_hex = ""
            sifreli = ""
            for m in range(boyut):
                if metin[m] != " ":
                    metin_hex += self.hex[self.alfabe.index(metin[m]) % 16]
            if len(metin_hex) % 2 != 0:
                metin_hex += self.hex[0]
            while len(metin_hex) > 0:
                sifreli += self.hex[(self.hex.index(metin_hex[0]) +
                                     self.hex.index(metin_hex[-1])) % 16]
                metin_hex = metin_hex[1:-1]
                if len(sifreli) == 64:
                    break
            while(len(sifreli) < 64):
                sifreli += self.hex[(self.hex.index(sifreli[0]) +
                                     self.hex.index(sifreli[-1])) % 16]
            sifreli = sifreli[::-1]
            return sifreli
        return "Şifrelenecek metin bulunamadı"

    def hash_sifreleme_5_SHA(self, metin: str, guvenlik_kodu: str):
        boyut = len(metin)
        metin = f"{guvenlik_kodu}{metin}"
        if boyut > 0:
            metin_hex = ""
            sifreli = ""
            for m in range(boyut):
                if metin[m] != " ":
                    metin_hex += self.hex[self.alfabe.index(metin[m]) % 16]
            if len(metin_hex) % 2 != 0:
                metin_hex += self.hex[0]
            while len(metin_hex) > 0:
                sifreli += self.hex[(self.hex.index(metin_hex[0]) +
                                     self.hex.index(metin_hex[-1])) % 16]
                metin_hex = metin_hex[1:-1]
                if len(sifreli) == 64:
                    break
            while(len(sifreli) < 64):
                sifreli += self.hex[(self.hex.index(sifreli[0]) +
                                     self.hex.index(sifreli[-1])) % 16]
            sifreli = sifreli[::-1]
            return sifreli
        return "Şifrelenecek metin bulunamadı"
