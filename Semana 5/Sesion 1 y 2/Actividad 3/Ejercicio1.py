calificacion1 = int(input("Ingrese calificacion 1: "))
calificacion2 = int(input("Ingrese calificacion 2: "))
calificacion3 = int(input("Ingrese calificacion 3: "))
suma = calificacion1 + calificacion2 + calificacion3
promedio = suma / 3

print(f"""Calificacion 1: {calificacion1:>3}
Calificacion 2: {calificacion2:>3}
Calificacion 3: {calificacion3:>3}
{"Promedio:":<15}{promedio:>3.0f}""")