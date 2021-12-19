##ecponente de un numero


base=int(input('Ingrese la bse del numero: '))
exponente=int(input('Ingrese el exponente: '))
     
def potencia(base, exponente):
    resultado=1
    for i in range(exponente):
        resultado*=base
    return resultado

print('El resultado es: ',potencia(base,exponente))
