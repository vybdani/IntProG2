
capital_inicial = float(input("Ingresa el capital inicial: "))
tasa_anual = float(input("Ingresa la tasa de interés anual (en %): "))
anios = int(input("Ingresa la cantidad de años: "))

tasa_decimal = tasa_anual / 100

factor = (1 + tasa_decimal) ** anios
monto_final = capital_inicial * factor

interes_ganado = monto_final - capital_inicial

print("Capital inicial:", capital_inicial)
print("Tasa anual (%):", tasa_anual)
print("Años:", anios)
print("Monto final:", round(monto_final, 2))
print("Interés ganado:", round(interes_ganado, 2))
