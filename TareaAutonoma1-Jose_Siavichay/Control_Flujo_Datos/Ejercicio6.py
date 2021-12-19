##dias trancurridos a partir de una fecha

from datetime import date

fecha = date(2015, 2, 1)
fecha2=date(2014, 1, 1)

delta=fecha-fecha2

print('Disas transcurridos: ', delta)
