"""Leer una palabra diferente a fin y convertirla a mayuscula"""

palabra = input("Dime una palabra")

for i in range (100000):
    if palabra.lower() == "fin":
        break
    else:
        print(f"{palabra.upper()} tiene {len(palabra)} Letras")
        palabra = input("Dime una palabra")
    
    
    