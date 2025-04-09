edad = int(input("Ingresa tu edad: "))
sexo = input("¿Eres hombre o mujer?: ").lower()

if sexo == "mujer":
    pulsaciones = (220 - edad) / 10
else:
    pulsaciones = (210 - edad) / 10

print(f"Tu número de pulsaciones por 10 segundos es: {pulsaciones}")
