#zadatak1: zbroj parnih brojeva
zbroj_parnih_brojeva = 0
for i in range(0, 101, 2):
    zbroj_parnih_brojeva += i
print(f"Zbroj svih parnih brojeva od 1 do 100 sa for petljom je : {zbroj_parnih_brojeva}")
print("\n")

j = 0 
zbroj_while = 0
while j < 101:
    zbroj_while += j
    j += 2
print(f"Zbroj parnih brojeva sa while petljom: {zbroj_while}")
print("\n")

#zadatak2: ispis neparnih brojeva obrnutim redoslijedom
for m in range(19, 0, -2):
    print(m, end=" ")
print("\n")

n = 19
while n > 0:
    print(n, end=" ")
    n -= 2
print("\n")

#zadatak 3: fibonnacijev niz do 1000
a, b = 0, 1

for i in range(1000):
    if a > 1000:
        break
    print(a, end=" ")
    a, b = b, a+b
print("\n")
    
a, b = 0, 1
print(a, b, end=" ")
while True:
    korak = a + b
    if korak > 1000:
        break
    print(korak, end=" ")
    a = b
    b = korak
