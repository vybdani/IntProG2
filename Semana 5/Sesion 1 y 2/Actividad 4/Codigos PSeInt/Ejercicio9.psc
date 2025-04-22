Algoritmo Ejercicio9
	
	Definir a, b, c Como Real
	Escribir 'Ingrese el primer número:'
	Leer a
	Escribir 'Ingrese el segundo número:'
	Leer b
	Escribir 'Ingrese el tercer número:'
	Leer c
	Si a=b Y b=c Entonces
		Escribir 'Los números son iguales'
	SiNo
		Si a>=b Entonces
			Si a>=c Entonces
				Escribir 'El mayor es: ', a
			SiNo
				Escribir 'El mayor es: ', c
			FinSi
		SiNo
			Si b>=c Entonces
				Escribir 'El mayor es: ', b
			SiNo
				Escribir 'El mayor es: ', c
			FinSi
		FinSi
	FinSi
FinAlgoritmo
