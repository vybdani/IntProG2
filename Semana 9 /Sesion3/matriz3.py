nombres = ["Ariadna", "Rommel", "Alfredo", "Jairo", "Alexandra", "Dani", "Arroba", "Duran", "Franklin"]

matriz_nombres = []
indice = 0

for fila in range(3):
    fila_nombres = []
    for col in range(3):
        fila_nombres.append(nombres[indice])
        indice += 1
    matriz_nombres.append(fila_nombres)

print("Matriz de nombres (3x3):")
for fila in matriz_nombres:
    print(fila)
