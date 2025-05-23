numeros = [10, 20, 30, 40, 50, 60, 70]
suma = 0
for i in range(0, len(numeros), 2):  # Solo posiciones pares: 0, 2, 4, 6
    suma += numeros[i]
print("Suma en posiciones pares:", suma)
