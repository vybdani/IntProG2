from main.menu import pedir_datos, mostrar_datos
from main.menu import limpiarpantalla as lim
import time as t

while True:
    lim()
    print("\n Menu")
    print("1. Ingresar nuevo estudiante")
    print("2. Mostrar estudiantes")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        pedir_datos()
    elif opcion == "2":
        mostrar_datos()
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opción no válida.")
        t.sleep (2.0)
        lim()
        
    
