##mes a partir del numero

import datetime

mes = int(input("Ingrese un numero del 1 al 12: "))

nommes = datetime.date(1900, mes, 1).strftime('%B')

print(nommes)
