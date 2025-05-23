# 4. Buscar un elemento
#✓ Dada una lista de palabras, solicita al usuario una palabra y muestra si está o no en la lista.

palabras = ["gato", "perro", "pez", "conejo"]
buscar = "perro"
if buscar in palabras:
    print(buscar, "está en la lista.")
else:
    print(buscar, "NO está en la lista.")
