mujeres = int(input("Ingrese la cantidad de mujeres: "))
varones = int(input("Ingrese la cantidad de varones: "))

total = mujeres + varones
porcentaje_mujeres = (mujeres / total) * 100
porcentaje_varones = (varones / total) * 100

print("Porcentaje de mujeres:", porcentaje_mujeres, "%")
print("Porcentaje de varones:", porcentaje_varones, "%")
