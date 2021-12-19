##promedio edades

aActual= 2021
edades=[]

def leerEdad():
    while True:
        anac=int(input('Anio de nacimiento: '))
        edad= aActual-anac
        edades.append(edad)
        otra=input('Desea ingresar mas datos? s/n')
        if otra=='n' or otra =='N':
            break
def promedio():
    suma=0
    for e in edades:
        suma+=e
    p=suma/len(edades)
    return p

leerEdad()
print('Promedio de edades()',format(promedio()))
