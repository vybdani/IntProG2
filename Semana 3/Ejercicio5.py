total_segundos = int(input("Ingrese la cantidad total de segundos: "))

horas = total_segundos // 3600

segundos_usados_por_horas = horas * 3600

resto1 = total_segundos - segundos_usados_por_horas

minutos = resto1 // 60

segundos_usados_por_minutos = minutos * 60

segundos = resto1 - segundos_usados_por_minutos

print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos:", segundos)
