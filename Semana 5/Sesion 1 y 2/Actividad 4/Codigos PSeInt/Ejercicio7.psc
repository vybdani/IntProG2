Algoritmo Ejercicio7

    Definir monto, propina, total Como Real
    Definir satisfaccion Como Cadena
    Escribir "Ingrese el monto total:"
    Leer monto
    Escribir "¿Cómo fue el servicio? (buena/mala):"
    Leer satisfaccion
    Si satisfaccion = "buena" Entonces
        propina <- monto * 0.15
    SiNo
        propina <- monto * 0.05
    FinSi
    total <- monto + propina
    Escribir "Total a pagar: ", total
	
FinAlgoritmo
