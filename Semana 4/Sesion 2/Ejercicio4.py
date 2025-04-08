# Solicita nombre, precio y descuento
nombre = input("Nombre del producto: ")
precio = float(input("Precio del producto: "))
descuento = float(input("Porcentaje de descuento: "))

# Calcula el precio final
rebaja = precio * descuento / 100
precio_final = precio - rebaja

# Muestra resultados
print(f"Producto: {nombre}")
print(f"Precio final: {precio_final}")
