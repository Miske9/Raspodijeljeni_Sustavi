broj = 45
pokusaj = 0
broj_je_pogoden = True

while broj_je_pogoden:
    unos = int(input("Unesite broj za koji mislite da je tocan od 1-100: "))
    pokusaj += 1
    if unos > broj:
        print("Trazeni broj je veci od unesenog broja\n")

    elif unos < broj:
        print("Trazeni broj je manji od unesenog broja\n")

    else:
        print(f"Bravo, pogodio si u {pokusaj} pokusaja!")
        broj_je_pogoden = False