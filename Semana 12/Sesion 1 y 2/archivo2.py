mi_archivo = open(r'C:\Users\USUARIO\Documents\Archivo\notas.txt', 'w')
texto = input("Only beauty, only Dani: ")
mi_archivo.write(texto)
mi_archivo.close()