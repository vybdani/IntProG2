
tareas = float(input("Ingrese la calificación de las tareas: "))
examen_parcial = float(input("Ingrese la calificación del examen parcial: "))
examen_final = float(input("Ingrese la calificación del examen final: "))

ponderacion_tareas = 0.30
ponderacion_parcial = 0.30
ponderacion_final = 0.40

calificacion_final = (tareas * ponderacion_tareas) + (examen_parcial * ponderacion_parcial) + (examen_final * ponderacion_final)

print(f"La calificación final del estudiante es: {calificacion_final}")
