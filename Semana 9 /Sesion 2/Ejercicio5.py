#5. Contar elementos mayores que un número
#Dada una lista de 10 números, contar cuántos son mayores que 50.

numeros = [12, 65, 43, 78, 55, 22, 91, 30, 60, 27]
contador = 0
for n in numeros:
    if n > 50:
        contador += 1
print("Cantidad mayor que 50:", contador)
