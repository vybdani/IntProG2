Algoritmo sin_titulo
	
	Escribir "Ejercicio 8"
	definir cordobas, dolares, cambio Como Real
	
	Escribir "Ingresa la cantidad de cordobas que quieras cambiar a dolares"
	leer cordobas
	escribir "Ingresa el tipo de cambio"
	leer dolares
	
	si cordobas >= 0 y cambio > 0 Entonces
		dolares = cordobas / cambio
		Escribir dolares " equivales a " cordobas " cordobas"
		
	sino 
		escribir "Error, no puede ingresar datos negativos, favor ingrese datos validos"
	FinSi

FinAlgoritmo
