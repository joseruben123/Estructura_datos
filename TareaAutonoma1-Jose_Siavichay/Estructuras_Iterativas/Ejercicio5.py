##intentos contrasenas

i=0
while i<10:
    clave=input("ingrese su clave")
    i=i +1
    if str(clave)=="1234567891":
        print("Bienvenido")
        break
    else:
        print("CLAVE INCORRECTA")
        if    i==10:
            print("INTENTOS AGOTADOS")
            break
     
