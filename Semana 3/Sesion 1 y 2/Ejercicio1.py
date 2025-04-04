temp_fah = float(input("Ingresa la temperatura en F: "))

temp_cel = ((temp_fah - 32) * 5) / 9

temp_kel = temp_cel + 273.15
print(f"Grados celsious {temp_cel:2}f")
print(f"Grados Kelvin {temp_kel}")