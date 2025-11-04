lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parna_lista = []
neparna_lista = []
def grupiraj_po_paritetu(lista):
    for element in lista:
        if element % 2 == 0:
            parna_lista.append(element)
        else:
            neparna_lista.append(element)
    return f"Parni brojevi su: {parna_lista}, a neparni brojevi su: {neparna_lista}"

print(grupiraj_po_paritetu(lista))