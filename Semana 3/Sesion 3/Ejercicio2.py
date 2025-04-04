#Leer X cantidad de producto comprado a X precio,
#aplica el iva del 15%
# un descuento del 10%
#Mostrar el total nates del IVA
#Monto del IVA
#Monto del descuento
#Monto a pagar
""" Se debe leer el nombre del cliente, nombre del producto y mostrar
una factura """
print("="*20)
print("Sistema de facturacion")
print("="*20)
print("Ingresa los isguientes datos")
cliente = input("Nombre del cliente: ")
producto = input("Nombre del producto: ")
precio = float(input("Precio del producto:"))
cantidad = float(input("Cantidad del producto: "))

total = precio * cantidad
iva = total * 0.15
descuento = total * 0.1
monto = total + iva - descuento

import os 
press_key = input("PPresiona una tecla para continuar...")
os.system("cis || clear ")
print("+"*30)
print("Factura ")
print("+"*30)
print(f"Cliente: {cliente}")
print("Productos \t Cantidad \t Precio \t Total")
print(f"{producto} \t {cantidad} \t {precio} \t {total}")
print(f"IVA: {iva}")
print(f"Desc: {descuento}")
print(f"Monto: {Monto}")