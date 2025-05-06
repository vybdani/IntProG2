#Producto de los primeros M números pares
#o Enunciado: Pide al usuario un número entero positivo M y calcula el producto de los
#primeros M números pares.
#o Especificación: Usa un bucle while, un acumulador (para el producto), y un contador
#(para los números pares).

numero = int (input("Ingresa un numero:"))
producto = 1
contador = 0
i = 0
while contador < numero:
    i += 2
    contador += 1
    producto *= i
    print (f"El producto de los primeros {contador} numero pares es {producto}")