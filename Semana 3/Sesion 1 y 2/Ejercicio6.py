peso = float(input("Ingrese su peso en kilogramos: "))

altura = float(input("Ingrese su altura en metros: "))

altura_cuadrado = altura * altura

imc = peso / altura_cuadrado

imc_redondeado = round(imc, 2)

print("Peso ingresado:", peso, "kg")
print("Altura ingresada:", altura, "m")

print("Su IMC es:", imc_redondeado)

if imc_redondeado < 18.5:
    print("Clasificación: Bajo peso")
elif imc_redondeado < 25:
    print("Clasificación: Peso normal")
elif imc_redondeado < 30:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificación: Obesidad")
