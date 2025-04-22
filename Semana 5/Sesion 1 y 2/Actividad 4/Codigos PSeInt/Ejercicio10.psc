Algoritmo Ejercicio10
	
    Definir dia, mes, anio Como Entero
    Escribir "Ingrese día:"
    Leer dia
    Escribir "Ingrese mes:"
    Leer mes
    Escribir "Ingrese año:"
    Leer anio
    Si mes = 2 Y dia > 29 Entonces
        Escribir "Fecha inválida"
    FinSi
    Si (mes = 4 O mes = 6 O mes = 9 O mes = 11) Y dia > 30 Entonces
        Escribir "Fecha inválida"
    FinSi
    Si (mes = 1 O mes = 3 O mes = 5 O mes = 7 O mes = 8 O mes = 10 O mes = 12) Y dia > 31 Entonces
        Escribir "Fecha inválida"
    FinSi

	
FinAlgoritmo
