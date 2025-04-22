Algoritmo Ejercicio13
	
    Definir saldo_inicial, opcion, cantidad Como Real
    Escribir "Ingrese el saldo inicial:"
    Leer saldo_inicial
    Escribir "Opciones: 1=Vaciar, 2=Depositar, 3=Retirar"
    Leer opcion
    Segun opcion Hacer
        1:
            saldo_inicial <- 0
        2:
            Escribir "Ingrese cantidad a depositar:"
            Leer cantidad
            saldo_inicial <- saldo_inicial + cantidad
        3:
            Escribir "Ingrese cantidad a retirar:"
            Leer cantidad
            saldo_inicial <- saldo_inicial - cantidad
    FinSegun
    Escribir "Nuevo saldo: ", saldo_inicial

	
FinAlgoritmo
