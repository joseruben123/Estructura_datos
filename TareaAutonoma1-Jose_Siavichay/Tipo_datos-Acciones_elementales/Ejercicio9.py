##Dado un (1) número binario de cuatro (4) dígitos imprimir su bit da paridad.
##El bit de paridad es 1 si el número de bits 1 es impar y 0 en caso contrario


bits = int(input("Ingresa un numero binario de 4 digitos: "))
if numero & 1 == 0:
    print("0")
else:
    print("1")
