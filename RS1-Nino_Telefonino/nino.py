from pozivni_brojevi import fiksni, mobilni, posebni

def ispravi(broj):
    znakovi = [' ', '-', '(', ')', '\t', '\n']
    for znak in znakovi:
        broj = broj.replace(znak, '')
    broj = broj.strip()

    if broj.startswith('+385'):
        broj = "0" + broj[4:]
    elif broj.startswith('00385'):
        broj = "0" + broj[5:]
    elif broj.startswith('385'):
        broj = "0" + broj[3:]

    return broj

def validiraj_broj_telefona(broj: str):
    broj = ispravi(broj)
    
    rezultat = {
        "validan": False,
        "pozivni_broj": None,
        "broj_ostatak": None,
        "vrsta": None,
        "mjesto": None,
        "operater": None
    }

    svi_pozivni = list(fiksni.keys()) + list(mobilni.keys()) + list(posebni.keys())
    svi_pozivni.sort(key=lambda x: - len(x))  

    pozivni = None
    for kljuc in svi_pozivni:
        if broj.startswith(kljuc):
            pozivni = kljuc
            break
    if not pozivni:
        return rezultat  

    broj_ostatak = broj[len(pozivni):]
    rezultat["pozivni_broj"] = pozivni
    rezultat["broj_ostatak"] = broj_ostatak
    
    if pozivni in fiksni:
        rezultat["vrsta"] = "fiksna"
        rezultat["mjesto"] = fiksni[pozivni]
        if 6 <= len(broj_ostatak) <= 7:
            rezultat["validan"] = True

    elif pozivni in mobilni:
        rezultat["vrsta"] = "mobilna"
        rezultat["operater"] = mobilni[pozivni]
        if 6 <= len(broj_ostatak) <= 7:
            rezultat["validan"] = True

    elif pozivni in posebni:
        rezultat["vrsta"] = "posebna"
        if len(broj_ostatak) == 6:
            rezultat["validan"] = True

    return rezultat
    
print(validiraj_broj_telefona(" 00385 52 721-633 "))
print(validiraj_broj_telefona(" +385 (95) 721-7633 "))
print(validiraj_broj_telefona(" 099 721-7633 "))
print(validiraj_broj_telefona(" 065 721-763 "))