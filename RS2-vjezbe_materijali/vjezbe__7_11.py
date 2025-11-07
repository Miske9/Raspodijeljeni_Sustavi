#lista
lista = [1,2,3,4,[1,2,3,9]]

# enumerate  
for index, vrijednost in enumerate(lista):
    if index == -1:
        for element in vrijednost:
            print(element)
        continue
print(vrijednost)
    
#tuple
tapl = ("margherita", "123", 123, None)
lista_2 = list(tapl)

print(tapl)
print(lista_2)

for element in tapl:
    print(element)
    
#range brojeva
lista_brojeva = range(1,101)

#dictionary
osoba = {
    "ime" : "Marko",
    "prezime " : "Maric",
    2 : "Pero",
    (1,2,3) : False
}

print(osoba["ime"])

for kljuc, vrijednost in osoba.items():
    print(f"kljuc - {kljuc} :  {vrijednost}")
    
#set
skup = {1,2,3,4,4,5} #set
lista = [20, 30, 40, 40, 50]

#lambda
def kvadriraj (x : int) -> float: #hintovi
    return x ** 2

broj = 5
kvadriraj(1)

def konkatenacija (x : str, y : str) -> str: #hintovi
    return x + y

print(konkatenacija("123", "12"))

#lambda arguments : expression
print((lambda x : x ** 2)(12)) #self_invoke

print((lambda x, y : x + y)(12, 13)) #self_invoke

funkcija = lambda x : f"Pozz {x}"
print(funkcija("pero"))

kruznica = lambda r = 2, pi = 3.14 : r ** 2 * pi
print(kruznica())

#funkcija koja ce primjeniti drugu funkciju na svaki element liste
def primjeni_na_sve(lista : list, funkcija : callable):
    nova_lista = []
    for element in lista:
        nova_vrijednosst = funkcija(element)
        nova_lista.append(nova_vrijednosst)
    return nova_lista

#def uvecaj_pa_kvadriraj(x): -- zamijenjeno sa lambda izrazon
 #   return (x + 1) ** 2

listaa = [1,2,3,4,5]

print(primjeni_na_sve(listaa, lambda x : (x + 1) ** 2))

#SINTAKSA
#lambda arguments : expression if true else expression_2
#lambda izraz koji kvadrira broj ako je paran, ako ne na trecu potencija

broj2 = 5
f = lambda x: x**2 if x % 2 == 0 else x ** 3
print(f(3))

def pomnozi_s_faktorom(faktor: int):
    return lambda x: x * faktor

broj3 = pomnozi_s_faktorom(3)
print(broj3(3))
print(broj3)
print(type(broj3))

kolekcija = [broj3(3), broj3(10)]
print(kolekcija)

#map (function, iterables)
lista = [1, 2, 3, 4]
#def kubiraj(x:int):
 #   return x ** 3 --> lambda izraz

print(list(map(lambda x : x ** 3, lista)))

lista_stringova = ["Pero", "Marko", "Sanja", "Josip"]
print(list(map(lambda  ime: len(ime), lista_stringova)))

#rjecnik
studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "jmbag": "0303077889"},
    {"ime": "Marko", "prezime": "Marković", "jmbag": "0303099878"},
    {"ime": "Ana", "prezime": "Anić", "jmbag": "0303088777"}
]
print(list(map(lambda jmb: jmb["jmbag"], studenti)))

#filter
#expression mora biti Bool(), filter vraca reduciranu iterable/kolekciju
#Sintaksa:
#filter(function, iterablers)

lista4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: x % 2 == 0, lista4))) #map vraca true, false listu // filter vraca podskup postojece kolekcije

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "jmbag": "0303077889", "godina_rodenja" : 2000},
    {"ime": "Marko", "prezime": "Marković", "jmbag": "0303099878", "godina_rodenja" : 1999},
    {"ime": "Ana", "prezime": "Anić", "jmbag": "0303088777", "godina_rodenja" : 2003},
    {"ime": "Petra", "prezime": "Petrić", "jmbag": "0303088777", "godina_rodenja" : 2001}
]

print(list(filter(lambda student : student["godina_rodenja"] < 2001, studenti)))

#any vraca True ako je bilo koji element iterabilnog objekta istinit
#all vraca True ako su svi element iterabilnog objekta istinit

lista_brojeva2 = [2, 4, 7, 11, 13, 15, 16]

print(all(list(map(lambda broj : broj % 2 == 0, lista_brojeva2))))

putnici = [
    {"ime": "Ivan", "uplata" : True},
    {"ime": "Marko", "uplata" : True},
    {"ime": "Ana", "uplata" : False}
]

print(all(list(map(lambda x : x["uplata"] == True, putnici))))

#comperhension
brojevi = [1,2,3,4,5]
kvadrati = list(map(lambda x: x ** 2, brojevi))
#rezultat = [expression for element in iterable]
kvadrati_c = [element ** 2 for element in brojevi]
print(kvadrati_c)

nizovi = ["jabuka", "kruska", "brek", "banana"]
#lista velicina stringova
nizovi_map = [len(x) for x in nizovi]
print(nizovi_map)

brojevi2 = [3,4,6,7,10]
#list comprehension
#[expression if true else expression_2 for element in iterable]
br_trans = [x for x in brojevi2 if x % 2 != 0]
print(br_trans)