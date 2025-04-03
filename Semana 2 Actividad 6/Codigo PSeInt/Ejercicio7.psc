Algoritmo sin_titulo
	Escribir "Ejercicio 7"
	
	Definir cordobas, dolares, cambio, total Como Real
	
	Escribir "Ingresa los dolares que quieras cambiar a cordobas"
	leer dolares
	Escribir "Ingresa el tipo de cambio"
	leer cambio
	
	si dolares >= 0 y cambio > 0 Entonces
		cordobas = dolares * cambio
		Escribir dolares " son equivalentes a " cordobas " cordobas"
		
	SiNo
		Escribir "Error, no puede ingresar cantidades negativas, favor ingresar datos validos"
	FinSi

FinAlgoritmo
