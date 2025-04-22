inventario_inicial = int(input("Ingresa la cantidad inicial en inventario: "))
productos_recibidos = int(input("Ingresa la cantidad de productos recibidos: "))
productos_vendidos = int(input("Ingresa la cantidad de productos vendidos: "))

inventario_total = inventario_inicial + productos_recibidos
inventario_actual = inventario_total - productos_vendidos

print("Inventario inicial:", inventario_inicial)
print("Productos recibidos:", productos_recibidos)
print("Productos vendidos:", productos_vendidos)
print("Inventario final disponible:", inventario_actual)
