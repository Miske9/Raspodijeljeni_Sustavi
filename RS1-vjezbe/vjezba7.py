lozinka = input("Unesite lozinku: ")
bad_password = ["password", "lozinka"]

def prvojera_lozinke(lozinka):
    if len(lozinka) < 8 or len(lozinka) > 15:
        return "Lozinka mora sadrzavati izmedu 8 i 15 znakova"
    if not any (a.isupper() for a in lozinka):
        return "Lozinka mora sadrzavati barem jedno veliko slovo i jedan broj"
    if not any (a.isdigit() for a in lozinka):
        return "Lozinka mora sadrzavati barem jedno veliko slovo i jedan broj"
    for zabranjeno in bad_password:
        if zabranjeno in lozinka.lower():
            return "Lozinka ne smije sadrzavati rijeci 'password' ili 'lozinka'."
    else:
        return "Lozinka je jaka!"

print(prvojera_lozinke(lozinka))