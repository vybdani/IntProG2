salario_actual = float(input("Ingrese el salario actual del empleado: "))

incremento = salario_actual * 0.08
descuento = salario_actual * 0.025

nuevo_salario = salario_actual + incremento - descuento

print("El nuevo salario del empleado es:", nuevo_salario)
