#Ejercicio 3: Generador de Listas de Compras
#• Problema: Crea un programa que permita al usuario crear una lista de compras. El programa
#solicitará al usuario que ingrese productos uno por uno y los guardará en un archivo llamado
#compras.txt. El usuario indicará que ha terminado de añadir productos introduciendo la palabra "fin".
#• Paso a paso:
#1. Abrir el archivo compras.txt en modo de escritura ('w') para iniciar una nueva lista.
#2. Crear un bucle infinito (while True).
#3. Dentro del bucle, pedir al usuario que ingrese un producto.
#4. Comprobar si la entrada del usuario es "fin". Si lo es, romper el bucle.
#5. Si no es "fin", escribir el producto en el archivo, seguido de un salto de línea (\n).
#6. Una vez que el bucle termina, cerrar el archivo y notificar al usuario que la lista ha sido guardada.

with open("compras.txt", "w") as archivo:
    print("Escribe tus productos uno por uno. Escribe 'fin' para terminar.")
    while True:
        producto = input("Producto: ")
        if producto.lower() == "fin":
            break
        archivo.write(producto + "\n")  # Cada producto en una línea

print("Lista guardada en compras.txt.")
