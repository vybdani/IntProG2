dolares = float(input("Ingrese la cantidad en dólares: "))

tasa_euros = 0.92      # Ejemplo: 1 dólar = 0.92 euros
tasa_libras = 0.78     # Ejemplo: 1 dólar = 0.78 libras
tasa_yenes = 151.25    # Ejemplo: 1 dólar = 151.25 yenes

euros = dolares * tasa_euros

libras = dolares * tasa_libras

yenes = dolares * tasa_yenes

print("Cantidad en dólares: $", round(dolares, 2))
print("Equivalente en euros: €", round(euros, 2))
print("Equivalente en libras: £", round(libras, 2))
print("Equivalente en yenes: ¥", round(yenes, 2))
