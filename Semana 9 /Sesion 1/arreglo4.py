import os
import random
import time

CLEAR_COMMAND = "cls||clear"

participantes = list()
while True:
    os.system(CLEAR_COMMAND)
    os.system("color a1")
    nombre = input("Ingrese el nombre del participante (o 'fin' para terminar): ")
    if nombre.lower() == 'fin':
        break
    participantes.append(nombre.upper())
    
os.system(CLEAR_COMMAND)
print("Participantes registrados:")
print(participantes)
x = input("Presione 'Enter' para continuar...")
#Cuenta regresiva de 10 segundos
for cont in range(10, 0, -1):
    os.system(CLEAR_COMMAND)
    print(cont)
    time.sleep(1)

fin = len(participantes) - 1
ganador = random.randint(0, fin)
print("El ganador es:", participantes[ganador])
