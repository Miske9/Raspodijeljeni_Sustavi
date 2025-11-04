tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

def brojanje_rijeci(tekst):
    rijeci = tekst.split()  
    brojanje = {}        
    for rijec in rijeci:
        rijec = rijec.lower()  
        if rijec in brojanje:
            brojanje[rijec] += 1
        else:
            brojanje[rijec] = 1
    return brojanje

print(brojanje_rijeci(tekst))
