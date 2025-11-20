class Osoba:
    def __init__(self, ime, prezime, godine):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
    
    def pozdrav(self):
        return f"Pozdrav, ja sam {self.ime} {self.prezime} i imam {self.godine} godina."
    
osoba = Osoba('Ivan', 'Ivic', 25)
print(osoba.ime)

osoba2 = Osoba('Marko', 'Markovic', 30)
print(osoba2.godine)

print(osoba.pozdrav())

class Zbroj:
    def zbroji(self, *args):
        return sum(args)

zbroj_objekt = Zbroj()
print(zbroj_objekt.zbroji(1,2,3,4,5,6))

class Ispis:
    def ispisi_kljuc_vrijednost(self, **kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")

ispis_objekt = Ispis()
ispis_objekt.ispisi_kljuc_vrijednost(ime = "Ana", prezime = "Anic", godine = 22)
