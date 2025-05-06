#3. Contar vocales en una cadena
#o Enunciado: Pide al usuario una cadena y cuenta cuántas vocales (a, e, i, o, u) tiene.
#o Especificación: Usa un bucle for para recorrer la cadena y contadores para cada
#vocal.

cadena = input ("Ingresa una cadena:")
contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

for letra in cadena:
    if letra.lower() == "a":
        contador_a += 1
    elif letra.lower() == "e":
        contador_e += 1
    elif letra.lower() == "i":
        contador_i += 1
    elif letra.lower() == "o":
        contador_o += 1
    else:
        contador_u += 1
        
print (f"La cadena tiene {contador_a} letra a")
print (f"La cadena tiene {contador_e} letra e")
print (f"La cadena tiene {contador_i} letra i")
print (f"La cadena tiene {contador_o} letra o")
print (f"La cadena tiene {contador_u} letra u")
    