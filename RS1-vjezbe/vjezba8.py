lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nova_lista = []

def filtriraj_parne(lista):
    for element in lista:
        if element % 2 == 0:
            nova_lista.append(element)
    print(nova_lista)

filtriraj_parne(lista)