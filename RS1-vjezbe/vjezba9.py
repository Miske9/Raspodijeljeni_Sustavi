lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

def ukloni_duplikate(lista):
    skup = set(lista)
    nova_lista = list(skup)
    return nova_lista

print(ukloni_duplikate(lista))