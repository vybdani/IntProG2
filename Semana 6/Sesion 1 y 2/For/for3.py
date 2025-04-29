#Leer dos numeros e imprimir los numeros entre ellos
def mostrarNumeros(num1 =0, num2=0):
    if (num1 < num2):
        for i in range(num1, num2+1):
            print(i)
    else:
        for i in range(num2, num1+1):
            print(i, end=" ")
def main():
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    mostrarNumeros(num1, num2)


main()