import random
numeros = [random.randint(1, 100) for _ in range(10)]
pares = []
impares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print("Original:", numeros)
print("Pares:", pares)
print("Impares:", impares)
