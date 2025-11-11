import math
faktorijeli = {x: [math.factorial(i) for i in range(1, x + 1)] for x in range(1, 11)}
print(faktorijeli)
