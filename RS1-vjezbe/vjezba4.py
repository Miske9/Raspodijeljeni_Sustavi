zbroj = 0
nula = True

while nula:
    unos = int(input("Unesi broj, a 0 ako zelis prekid programa: "))
    zbroj += unos
    if unos == 0:
        nula = False
        print(f"Zbroj svih unesenih brojeva je {zbroj}.")