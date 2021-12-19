##Dado un (1) número, imprimir 0 si es par y 1 si es impar.

numero = int(input("Ingresa un número: "))

if numero & 1 == 0:
    print("0")
else:
    print("1")
