Algoritmo Ejercicio9
	
	Definir a, b, c Como Real
	Escribir 'Ingrese el primer n�mero:'
	Leer a
	Escribir 'Ingrese el segundo n�mero:'
	Leer b
	Escribir 'Ingrese el tercer n�mero:'
	Leer c
	Si a=b Y b=c Entonces
		Escribir 'Los n�meros son iguales'
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
