#Ejercicio 1: Diario Personal
#• Problema: Escribe un programa que funcione como un diario simple. Cada vez que se
#ejecute, debe solicitar al usuario una entrada de texto y la guardará, junto con la fecha y hora
#actual, en un archivo llamado diario.txt. Cada nueva entrada debe añadirse al final del
#archivo sin borrar las anteriores.
#• Paso a paso:
#1. Importar el módulo datetime para obtener la fecha y hora.
#2. Solicitar al usuario que ingrese el texto para su entrada del diario.
#3. Abrir el archivo diario.txt en modo de adición ('a').
#4. Escribir la fecha y hora actual, seguida de la entrada del usuario. Asegurarse de
#añadir un salto de línea para separar las entradas.
#5. Cerrar el archivo.
#6. Mostrar un mensaje de confirmación al usuario.

from datetime import datetime  # Importamos para usar fecha y hora

entrada = input("Escribe lo que quieras guardar en tu diario: ")

# Abrimos el archivo en modo añadir (no borra lo que ya tiene)
with open("diario.txt", "a") as archivo:
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Formato bonito
    archivo.write(f"{fecha} - {entrada}\n")  # Guardamos fecha + texto + salto

print("Entrada guardada exitosamente en tu diario.")
