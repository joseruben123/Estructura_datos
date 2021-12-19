##Dado un (1) número binario de cuatro (4) dígitos imprimir su valor

def binarioDeci(binario):
    posicion = 0
    decimal = 0
    binario = binario[::-1]
    for digito in binario:
        # Elevar 2 a la posición actual
        multiplicador = 2**posicion
        decimal += int(digito) * multiplicador
        posicion += 1
    return decimal


binario = input("Ingresa un número binario de 4 digitos: ")
decimal = binarioDeci(binario)
print(decimal)
