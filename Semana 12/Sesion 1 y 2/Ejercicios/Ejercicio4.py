#Ejercicio 4: Lector de Datos CSV
#• Problema: Se proporciona un archivo productos.csv donde cada línea contiene el nombre
#de un producto, su precio y la cantidad en stock, separados por comas (ej: Laptop,1200,15).
#Escribe un programa que lea este archivo y muestre la información en un formato legible
#para el usuario, indicando el nombre, precio y stock de cada producto.
#• Paso a paso:
#1. Abrir el archivo productos.csv en modo de lectura.
#2. Recorrer el archivo línea por línea usando un bucle for.
#3. Para cada línea, eliminar el salto de línea final con .strip().
#4. Usar el método .split(',') para separar la línea en una lista de tres elementos (nombre,
#precio, cantidad).
#5. Imprimir los datos de forma ordenada, por ejemplo: Producto: Laptop | Precio: $1200
#| Stock: 15 unidades.
#6. Cerrar el archivo al finalizar

with open("productos.csv", "r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")  # Quita saltos y separa por coma
        nombre, precio, cantidad = datos
        print(f"Producto: {nombre} | Precio: ${precio} | Stock: {cantidad} unidades")
