datos_estudiantes = []

def guardar_estudiante(estudiante):
    datos_estudiantes.append(estudiante)

def mostrar_estudiantes():
    for est in datos_estudiantes:
        print("\n Estudiante ")
        print("Nombres:", est.nombres)
        print("Apellidos:", est.apellidos)
        print("Carrera:", est.carrera)
        print("Año:", est.anio)
        print("Promedio:", est.promedio)
