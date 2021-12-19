##numero capicula

n=int(input('Ingrese un numero de 5 digitos'))
if n>99 and n<100000:
    a=n//100
    b=n%10
    if a == b:
        print('El numero es capicula')
    else:
        print('El numero no capicula')
else:
    print('Ingrese numero de 5 digitos')
