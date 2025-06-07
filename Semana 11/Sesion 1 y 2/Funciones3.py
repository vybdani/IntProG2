#Calcular el area de un circulo

def calcular_area_circulo(radio):
    pi = 3.14159
    return pi * (radio ** 2)
radio = float(input("Ingrese el radio del círculo: "))
area = calcular_area_circulo(radio)
print(f"El área del círculo con radio {radio} es: {area:.2f}") 
