##Dado un (1) número de cuatro (4) dígitos imprimirlo por
##separado en unidades, decenas, centenas y unidades de mil.

numero = int(input("Ingresa un numero: "))

umil = numero / 1000
tmp = numero % 1000

centenas = tmp / 100
tmp = tmp % 100

decenas = tmp / 10
unidades = tmp % 10

print ('Unidades de millar: %i',umil)
print ('Centenas: %i',centenas)
print ('Decenas: %i',decenas)
print ('Unidades: %i',unidades)
