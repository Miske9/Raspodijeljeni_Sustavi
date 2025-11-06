vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

def count_vowels_consonants(tekst):
    broj_samoglasnika = 0
    broj_suglasnika = 0
    for znak in tekst:
        if znak in vowels:
            broj_samoglasnika += 1
        elif znak in consonants:
            broj_suglasnika += 1
    return {f"Vowels: {broj_samoglasnika}, Consonants: {broj_suglasnika}"}

print(count_vowels_consonants(tekst))
