Algoritmo sin_titulo
	Escribir "Ejercicio 10"
	Definir cantidad, i Como Entero
    Definir precio, subtotal, descuento, total_pagar Como Real
	
    subtotal = 0 
	
    Escribir "Ingrese la cantidad de productos:"
    Leer cantidad
	
    Para i = 1 Hasta cantidad Hacer
        Escribir "Ingrese el precio del producto ", i, ":"
        Leer precio
        subtotal = subtotal + precio 
    FinPara
	
    
    descuento = subtotal * 0.10
    total_pagar = subtotal - descuento
	
	
    Escribir "Subtotal: ", subtotal
    Escribir "Descuento (10%): ", descuento
    Escribir "Total a pagar: ", total_pagar

FinAlgoritmo
