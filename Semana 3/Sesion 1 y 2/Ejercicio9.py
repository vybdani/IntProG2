duracion_pelicula = int(input("Ingrese la duración de la película (en minutos): "))

comerciales_previos = int(input("Ingrese la duración de los comerciales previos (en minutos): "))

cantidad_pausas = int(input("Ingrese la cantidad de pausas comerciales: "))

duracion_pausa = int(input("Ingrese la duración de cada pausa (en minutos): "))

comerciales_durante = cantidad_pausas * duracion_pausa

comerciales_totales = comerciales_previos + comerciales_durante

total_parcial = duracion_pelicula + comerciales_previos

duracion_total = total_parcial + comerciales_durante

print("Duración original de la película:", duracion_pelicula, "minutos")
print("Comerciales totales (previos + pausas):", comerciales_totales, "minutos")
print("Tiempo total de la proyección:", duracion_total, "minutos")
