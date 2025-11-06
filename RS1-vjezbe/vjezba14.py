def isPrime(b):
    if b <= 1:
        return False
    for i in range (2, b):
        if b % i == 0:
            return False
    return True

def primes_in_range(a, c):
    nova_lista = []
    for broj in range(a, c):
        if isPrime(broj):
            nova_lista.append(broj)
    return nova_lista

print(isPrime(7))
print(isPrime(10))

print(primes_in_range(1, 10))