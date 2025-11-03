for i in range(1, 2):
    print(i)
    
for i in range(10, 1, 2):
    print(i)
    
for i in range(10, 1, -1):
    print(i)

"""
1) Prva petlja nema smisla jer ce se ispisati samo broj 1

2) Druga petlja nece ispisati nista jer je pocetna vrijednost veca od krajnje, a korak je pozitivan

3) Treca petlja ce ispisati brojeve od 10 do 1, ali jedinica nije ukljucena u ispis jer funkcija range() nikad ne ispisuje krajnju vrijednost
"""