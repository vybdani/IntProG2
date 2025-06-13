try:
    mi_ruta = 'C:\\Users\\USUARIO\\Documents\\Archivo\\datos.txt'
    mi_archivo = open(mi_ruta, 'r')
    contenido = mi_archivo.read()
    print(contenido)
    mi_archivo.close()
except FileNotFoundError:
    print("El archivo no se encuentra en la ruta especificada.")