import math
radio = float(input("Ingrese el radio del cilindro: "))

altura = float(input("Ingrese la altura del cilindro: "))

area_base = math.pi * (radio ** 2)

volumen = area_base * altura

area_lateral = 2 * math.pi * radio * altura

area_superficial = area_lateral + (2 * area_base)

print("Radio ingresado:", radio, "cm")
print("Altura ingresada:", altura, "cm")
print("Volumen del cilindro:", round(volumen, 2), "cm³")
print("Área superficial del cilindro:", round(area_superficial, 2), "cm²")
