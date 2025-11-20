#1 lambda funkcije
nizovi = ["jabuka", "kruška", "banana", "naranča"]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
lista = [1,2,3,4,5]
kvadriraj_parne = lambda x: x ** 2 if x % 2 == 0 else x
#print(kvadriraj_parne(4))

dulji_od_5 = lambda niz: len(niz) if len(niz) > 4 else niz
#print(dulji_od_5(lista))

#funkcije viseg reda
kvadrirana_lista = list(map(lambda x: x ** 2, lista))
#print(kvadrirana_lista)

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "jmbag": "0303077889"},
    {"ime": "Marko", "prezime": "Marković", "jmbag": "0303099878"},
    {"ime": "Ana", "prezime": "Anić", "jmbag": "0303088777"}
]

jmbagovi = list(map(lambda x: x['jmbag'], studenti))
#print(jmbagovi)

parni = list(filter(lambda x: x % 2 == 0, lista))
#print(parni)

studenti2 = [
    {"ime": "Ivan", "prezime": "Ivić", "jmbag": "0303077889", "godina_rodenja" : 2000},
    {"ime": "Marko", "prezime": "Marković", "jmbag": "0303099878", "godina_rodenja" : 1999},
    {"ime": "Ana", "prezime": "Anić", "jmbag": "0303088777", "godina_rodenja" : 2003},
    {"ime": "Petra", "prezime": "Petrić", "jmbag": "0303088777", "godina_rodenja" : 2001}
]

rodenje = tuple(filter(lambda x: x['godina_rodenja'] < 2000, studenti2))
#print(rodenje)

#print(any(map(lambda x: x % 2 == 0, lista)))
#print(all(map(lambda x: x % 2 == 0, lista)))

kvadrati = list(map(lambda x: x ** 2, range(1, 4)))
#print(kvadrati)

kvadrati2 = [x ** 2 for x in range (1,4)] #list comprehension
#print(kvadrati2)

duljine = [len(niz) for niz in nizovi]
#print(duljine)

neparni_kvadrati = [x ** 2 for x in range (1,11) if x % 2 != 0]
#print(neparni_kvadrati)

stari_studenti = [x['ime'] for x in studenti2 if x['godina_rodenja'] < 2000]
#print(stari_studenti)

prva_3_slova = [fruit[:3] for fruit in fruits]
#print(prva_3_slova)

sa_slovom_a = [x for x in fruits if 'a' in x]
#print(sa_slovom_a)

duljine_voca = {fruit: len(fruit) for fruit in fruits}
#print(duljine_voca)

kvad = {broj: broj ** 2 for broj in lista}
#print(kvad)

kvad_par = {broj: broj ** 2 for broj in lista if broj % 2 == 0}
#print(kvad_par)

