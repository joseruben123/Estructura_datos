clase Cola:
    def __init__(self,tamanio=1):
        yo mismo. lista = []
        yo mismo. tamaño=tamanio
        yo mismo. tope=0

    def push(self,dato):
        si es uno mismo. tope < yo. tamaño:
            yo mismo. lista += [dato]  
            yo mismo. tope += 1
            volver a sí mismo. lista
        de lo contrario:
            print("La lista esta llena")
            
    def pop(self):
        si es uno mismo. vacío():
            return print("Esta lista está vacía")
        de lo contrario:
            arriba = yo. lista [0]
            yo mismo. lista = yo. lista [1:]
            yo mismo. tope -=1  
            return print("el elemento que se esta eliminado es:",top)
        
    def show(self):
        si es uno mismo. vacío():
            print("la Lista esta vacia")
        de lo contrario:
            print("Cola"",*5,"Posición")
            for pos,top in enumerate(self. lista):
                print("[{}] {:9}". format(top,pos))    
            # para la parte superior en el rango (self.tope):
            #     print("[{}]".format(self.lista[top]))
    
    def longitud(self):
        volver a sí mismo. cazón
                    
             
    def vacío(self):
        si es uno mismo. tope== 0:
            regresar Verdadero
        de lo contrario:
            regresar Falso
        
    def buscarPi(self,buscado):
        si es uno mismo. vacío():
            print("La Cola se encuentra vacía")
        de lo contrario:
            la=Falso
            for pos,ele in enumerate(self. lista):
                si ele==buscado:
                    la=Verdadero
                    quebrar
            if la==True:
                print("El número que se ingresó esta en la posición: {}". formato(pos+1))
            de lo contrario:
                print("El número que se ingresó esta en la Pila")


# cola1=Cola (3)
# cola1.push(6)
# cola1.push(2)
# cola1.push(20)

# cola1.show()
# print(cola1.longitud())