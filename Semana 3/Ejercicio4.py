tramo1 = float(input("Ingrese la duración del primer tramo del vuelo (en horas): "))

escala1 = float(input("Ingrese la duración de la primera escala (en horas): "))

tramo2 = float(input("Ingrese la duración del segundo tramo del vuelo (en horas): "))

escala2 = float(input("Ingrese la duración de la segunda escala (en horas): "))

tramo3 = float(input("Ingrese la duración del tercer tramo del vuelo (en horas): "))

tiempo_total = tramo1 + escala1 + tramo2 + escala2 + tramo3

print("El tiempo total del viaje es:", tiempo_total, "horas")
