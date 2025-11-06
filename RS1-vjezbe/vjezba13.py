#1 zadatak
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def prvi_i_zadnji(lista):
    return (lista[0], lista[-1])
        
print(prvi_i_zadnji(lista))


#2 zadatak
lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]

def max_i_min(lista):
    najmanji = lista[0]
    najveci = lista[0]
    
    for broj in lista:
        if broj < najmanji:
            najmanji = broj
        elif broj > najveci:
            najveci = broj
    return (najveci, najmanji)

print(max_i_min(lista))


#3 zadatak
skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}
novi_skup = set()

def presjek(skup_1, skup_2):
    for broj in skup_1:
        for broj2 in skup_2:
            if broj == broj2:
                novi_skup.add(broj)
    return novi_skup

print(presjek(skup_1, skup_2))