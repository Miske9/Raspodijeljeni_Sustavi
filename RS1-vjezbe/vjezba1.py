broj_1 = float(input("Unesite prvi broj: "))
broj_2 = float(input("Unesite drugi broj: "))
operator = input("Odaberite operator (+, -, *, /): ")

if operator == '+':
    rezultat = broj_1 + broj_2
    print(f"Rezultat operacije {broj_1} {operator} {broj_2} je {rezultat}! ")
elif operator == '-':
    rezultat = broj_1 - broj_2
    print(f"Rezultat operacije {broj_1} {operator} {broj_2} je {rezultat}! ")
elif operator == '*':
    rezultat = broj_1 * broj_2
    print(f"Rezultat operacije {broj_1} {operator} {broj_2} je {rezultat}! ")
elif operator == '/':
    if broj_2 == 0:
        print("Dijeljenje s nulom nije moguce!")
    else:
        rezultat = broj_1 / broj_2
        print(f"Rezultat operacije {broj_1} {operator} {broj_2} je {rezultat}! ")
else:
    print("Nepodrzani operator!")
