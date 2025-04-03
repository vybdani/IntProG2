Algoritmo sin_titulo
	Escribir "Ejercicio 4"
	
	Definir divisor, dividiendo como enteros
	definir total Como Real
	
	escribir "Ingrese numero a dividir"
	leer dividiendo
	
	
	Repetir
		escribir "Ingrese numero por el cual dividir (divisor)" 
		leer divisor
		
		Si divisor = 0 Entonces
			Escribir "El divisor no puede ser 0, favor ingresar otro divisor"
		FinSi
	Hasta que divisor <> 0
	
	
	Total = dividiendo / divisor
	
	Escribir "El resultado de la division es de: " total
	

FinAlgoritmo
