import asyncio

baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

async def autentifikacija(korisnik):
    print("Pokrenuta autentifikacija ")
    await asyncio.sleep(3)

    for osoba in baza_korisnika:
        if osoba['korisnicko_ime'] == korisnik['korisnicko_ime'] and \
            osoba['email'] == korisnik['email']:
                rezultat = await autorizacija(osoba, korisnik['lozinka'])
                return rezultat
    return f"Korisnik {korisnik['korisnicko_ime']} nije pronađen."

async def autorizacija(korisnik_iz_baze, lozinka):
    print("Pokrenuta autorizacija ")
    await asyncio.sleep(2)

    for osoba in baza_lozinka:
        if osoba['korisnicko_ime'] == korisnik_iz_baze['korisnicko_ime']:
            if osoba['lozinka'] == lozinka:
                return f"Korisnik {korisnik_iz_baze['korisnicko_ime']}: Autorizacija uspješna."
            else:
                return f"Korisnik {korisnik_iz_baze['korisnicko_ime']}: Autorizacija neuspješna."
    return "Lozinka za korisnika ne postoji u bazi!"

async def main():
    korisnik = {
        'korisnicko_ime': 'mirko123',
        'email': 'mirko123@gmail.com',
        'lozinka': 'lozinka123'
    }
    rezultat = await autentifikacija(korisnik)
    print(rezultat)

asyncio.run(main())
