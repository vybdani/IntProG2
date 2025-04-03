Algoritmo sin_titulo
	definir monto_inicial, monto_final, intereses Como Real
	definir años Como Entero
	
	intereses = 0.03
	años = 5
	
	escribir "Ingrese el monto inicial del prestamo"
	leer monto_inicial
	
	monto_final = monto_inicial * (1 + intereses) ^ años
	
	Escribir "El monto a pagar al cabo de 5 años es de: " monto_final

FinAlgoritmo
