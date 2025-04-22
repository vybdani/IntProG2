Algoritmo Ejercicio15
	
	Definir puntos Como Real
    Escribir "Ingrese puntos de conducta (0 a 10):"
    Leer puntos
    Si puntos < 0 O puntos > 10 Entonces
        Escribir "Error: puntos fuera de rango"
    SiNo
        Si puntos >= 9 Entonces
            Escribir "Excelente"
        SiNo
            Si puntos >= 7 Entonces
                Escribir "Bueno"
            SiNo
                Si puntos >= 5 Entonces
                    Escribir "Regular"
                SiNo
                    Escribir "Deficiente"
                FinSi
            FinSi
        FinSi
    FinSi

	
FinAlgoritmo
