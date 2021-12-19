##salario

e=(input('Nombre del empleado: '))
horast=int(input('horas trabajadas: '))
horasv=int(input('valor horas: '))

if horast>=40:
    horast=horast+(horast*0.35)
else:
    print('Adios')

salario=(horast*horasv)

print('El empleado',e,'tiene un salario de: ',salario)
