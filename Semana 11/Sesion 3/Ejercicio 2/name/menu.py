from models.estudiante import Estudiante
from dao.almacen import guardar_estudiante, mostrar_estudiantes
import os
def limpiarpantalla():
    os.system ("cls")

def pedir_datos():
    print("\n Ingresar Datos del Estudiante")
    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    carrera = input("Carrera: ")
    anio = input("Año: ")
    promedio = float(input("Promedio: "))

    nuevo_estudiante = Estudiante(nombres, apellidos, carrera, anio, promedio)
    guardar_estudiante(nuevo_estudiante)

def mostrar_datos():
    print("\n Lista de Estudiantes")
    mostrar_estudiantes()
