#MATRIZ
matriz = [[7435.3, 643.675], [300.24, 87.534]]
print("-"*17)
for fila in matriz:
    for columna in fila:
        print(f"|{columna:>6}|", end="")
    print("|")
    print("-"*17)