#Suma de los primeros N números
#o Enunciado: Pide al usuario un número entero positivo N y calcula la suma de los
#números desde 1 hasta N.
#o Especificación: Usa un bucle for y un acumulador.

numero = int(input("Ingresa un numero: "))
suma = 0
for i in range(1, numero +1):
    suma += i
    print (f"La suma de los primero {i} numeros es {suma}")
    
    
    