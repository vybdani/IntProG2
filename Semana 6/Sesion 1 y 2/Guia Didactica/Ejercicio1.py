# Ejercicio 1: Tabla de multiplicar de un número

#1. Solicita al usuario un número entero positivo.
#2. Usa un bucle para que vaya de 1 a 10.
#3. En cada iteración, multiplica el número ingresado por el número de la iteración.
#4. Muestra el resultado en cada paso en pantalla.


numero = int(input("Introduce un numero entero positivo:"))

def tabla (numero):
    for i in range (1, 11):
        resultado = numero * i
        print (f"{numero} x {i} = {resultado}")
    
tabla (numero)    