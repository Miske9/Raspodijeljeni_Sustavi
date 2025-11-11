rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples", "pjesma", "otorinolaringolog"]
min_duljina = int(input("Unesite minimalnu duljinu riječi: "))
print(f"Minimalna duljina rijeci: {min_duljina} znakova!\n")
duge_rijeci = list(filter(lambda x: len(x) > min_duljina, rijeci))
print(duge_rijeci)
