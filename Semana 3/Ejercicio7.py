precio_original = float(input("Ingrese el precio original del producto: "))

porcentaje_descuento = float(input("Ingrese el porcentaje de descuento (%): "))

descuento = (precio_original * porcentaje_descuento) / 100

precio_con_descuento = precio_original - descuento

porcentaje_iva = float(input("Ingrese el porcentaje de IVA (%): "))

iva = (precio_con_descuento * porcentaje_iva) / 100

precio_final = precio_con_descuento + iva

print("Precio original: C$", round(precio_original, 2))
print("Descuento aplicado: C$", round(descuento, 2))
print("Precio con descuento: C$", round(precio_con_descuento, 2))
print("IVA calculado: C$", round(iva, 2))
print("Precio final a pagar: C$", round(precio_final, 2))
