nombre = input("Nombre del trabajador: ")
horas = float(input("Horas trabajadas: "))
precio_hora = float(input("Pago por hora: "))

bruto = horas * precio_hora
descuento = bruto * 0.05
neto = bruto - descuento

print(f"Trabajador: {nombre}")
print(f"Sueldo bruto: ${bruto}")
print(f"Descuento de renta (5%): ${descuento}")
print(f"Salario neto a pagar: ${neto}")
