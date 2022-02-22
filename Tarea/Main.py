NEGRO = '\033[30m'
ROJO = '\033[31m'
VERDE = '\033[32m'
AMARILLO = '\033[33m'
AZUL = '\033[34m'
MAGENTA = '\033[35m'
CIAN = '\033[36m'
BLANCO = '\033[37m'
RESET = '\033[39m'
de ast import While
de colas importar Cola
de listas import Lista
de ayudantes importar Ayudante
de pilas import Pila
tiempo de importación
importar os

def gotoxy(x,y):
    print("%c[%d;%df"% (0x1B,y,x),end=" ")
    
ayudante = Ayudante()
lista=[GREEN+"1) Lista","2) Pila","3) Cola","4) Salir"]
opcion=""
mientras que opcion != "4":
    os. system("claro")
    opcion = ayudante. menu(lista,YELLOW+"Menu Principal")
    si opcion == "1":
        opc1=""
        mientras que opc1 != "7":
            os. system("claro")
            ele=Lista()
            print(AMARILLO+"*"*20,"Mantenimento De Lista","*"*20)
            opc1 = ayudante. menu([GREEN+"1) Push","2) Pop","3) Show","4) Eliminar","5) Insertar","6) Buscar","7) Salir"],"")
            os. system("claro")
            si opc1=="1":
                print(AMARILLO+"*"*20,"Push","*"*20)
                gotoxy(0,2); dato1=int(input(GREEN+"Registre los elementos que desee que la lista tenga:"))
                # num=0
                # mientras que num < dato1:
                #     elementos = input("Ingrese el elemento a la lista:")
                #     ele.push(elementos)
                #     num =+1
                # input("El Elemento ingresado satisfactoriamente")
                para un rango de entrada (dato1):
                    valor=input("Ingresar el elemento:")
                    ele. push(valor)
                input("Se guardó todo bien")
            
            si opc1=="2":
                print(AMARILLO+"*"*20,"Pop","*"*20)
                dato=ele. Borrar()
                if dato:print(input("El elemento eliminado fue:{}". format(dato)))
                else:input("La lista se ecuentra vacía")
            
            si opc1=="3":
                print(AMARILLO+"*"*20,"Mostrar","*"*20)
                ele. Mostrar()
                input("Seleccione enter para salir")
                
                
            if opc1=="4":
                print(AMARILLO+"*"*20,"Eliminar por posicion","*"*20)
                eli=int(input("Ingresa la posicion que desea eliminar:"))
                ele. eliminarElementos(eli)
                input("Seleccione la tecla enter para salir")
            
                
            si opc1=="5":
                print(AMARILLO+"*"*20,"Ingrese por posición","*"*20)  
                dato=int(input("Registre el dato"))
                po=int(input("Ingresa la posición que desea tener el dato")) 
                ele. ingresarElemento(po,dato)
                input("El Dato que se ingreso esta correctamente")
                
            si opc1=="6":
                print(YELLOW+"*"*20,"Buscar","*"*20)
                dati=input("Registre el dato que desea buscar:")
                ele.buscarElemento(dati)  
                input("Seleccione la tecla enter para continuar")     
    
    
    elif opcion=="2":
        os.system("clear")
        gotoxy(0,2);can=input("Registre la cantidad de la pila :")
        while can.isnumeric()== False:
            time.sleep(1);gotoxy(32,2);print(" "*59)
            gotoxy(0,2);can=input(GREEN+"Registre la cantidad de la pila :")   
        ele1=Pila(can)
        opc1=""  
        while opc1 != "6":
            os.system("clear")
            print(YELLOW+"*"*20,"Mantenimento De Pila","*"*20)
            opc1 = helper.menu([GREEN+"1) Push","2) Pop","3) Show","4) Buscar","5) Longitud","6) Salir"],"")
            os.system("clear")
            if opc1=="1":   
                print(YELLOW+"*"*20,"Push","*"*20) 
                dato=str(input("Registre el elemento:"))
                ele1.push(dato)
                input("El dato que se ingreso esta correctamente")
             
            if opc1=="2":
                print(YELLOW+"*"*20,"Pop","*"*20) 
                ele1.Bo()
                input(RED+"Seleccione la tecla enter para seguir")
                
            if opc1=="3":
                print(YELLOW+"*"*20,"Show","*"*20)
                ele1.show()
                input(RED+"Seleccione la tecla enter para salir")
                
            if opc1=="4":
                print(YELLOW+"*"*20,"Buscar","*"*20)
                
            if opc1=="5":
                print(YELLOW+"*"*20,"Longitud","*"*20)
                num=ele1.longitud()
                print(input(GREEN+"La longitud de la pila es: {} de {}".format(num,can)))
                
    elif opcion=="3":
        os.system("clear")
        dad=int(input("Registre la cantidad de la cola: "))
        ele=Cola(papá)
        opc1="" 
        mientras que opc1!="6": 
            os. system("claro")
            print(AMARILLO+"*"*20,"Mantenimento De Cola","*"*20)
            opc1 = ayudante. menu([GREEN+"1) Push","2) Pop","3) Show","4) Buscar","5) Longitud","6) Salir"],"")
            os. system("claro")
            si opc1=="1":
                print(AMARILLO+"*"*20,"Push","*"*20)
                valor=str(input("Registra el elemento:"))
                ele. push(valor)
                input("Seleccione la tecla enter para salir")
            
            si opc1=="2":
                print(AMARILLO+"*"*20,"Pop","*"*20)
                ele. pop()
                input(RED+"Seleccione la tecla enter para salir")
                
            si opc1=="3":
                print(AMARILLO+"*"*20,"Mostrar","*"*20)
                ele. mostrar()
                input(RED+"Seleccione la tecla enter para salir")
                
            si opc1=="4":
                print(AMARILLO+"*"*20,"Buscar","*"*20)
                dati=input("Registra el dato que deseas buscar:")
                ele. buscarPi(dati)  
                input("Seleccione la tecla enter para continuar")
                
            si opc1=="5":
                print(AMARILLO+"*"*20,"Longitud","*"*20)
                num=ele. longitud()
                print(input(GREEN+"La longitud de la pila es: {} de {}". format(num,papá)))