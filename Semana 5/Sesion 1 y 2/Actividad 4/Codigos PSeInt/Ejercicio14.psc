Algoritmo Ejercicio14
	
    Definir edad_persona Como Entero
    Escribir "Ingrese la edad:"
    Leer edad_persona
    Si edad_persona >= 0 Y edad_persona <= 11 Entonces
        Escribir "Niño"
    SiNo
        Si edad_persona <= 17 Entonces
            Escribir "Adolescente"
        SiNo
            Si edad_persona <= 64 Entonces
                Escribir "Adulto"
            SiNo
                Escribir "Adulto mayor"
            FinSi
        FinSi
    FinSi
	
FinAlgoritmo
