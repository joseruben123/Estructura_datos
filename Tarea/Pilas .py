clase Pila: 
    def __init__(self,tamanio):
        yo mismo. lista=[]
        yo mismo. tope=0
        yo mismo. tamaño=tamanio
     
    def vacío(self):
        # if self.tope == 0:
        # regresar Verdadero
        # más:
        # devolver Falso
        regresar a sí mismo. tope == 0
    
    def push(self,dato):
        yo mismo. size=int(self. tamaño)
        si es uno mismo. tope < yo. tamaño:
            yo mismo. lista += [dato]
            yo mismo. tope += 1
        de lo contrario:
            print("La Pila se encuntra Llena")
   
    def Bo(self):
        si es uno mismo. vacío():
            return print("Lista Vacia")    
        de lo contrario:
            arriba = yo. lista[-1]
            yo mismo. tope -= 1
            yo mismo. lista = yo. lista[:-1]
            return print("El valor eliminado es:",top)
            
    def longitud(self):
        volver a sí mismo. cazón
        
    def show(self):
        si es uno mismo. vacío():
            print("La Lista se encuentra vacia")
        de lo contrario: 
            print("","Pila","*5,"Posición")
            for pos,top in enumerate(self. lista):
                print([top]" "*(9-len(top)),pos)
                # print("[{}] {:9}".format(top,pos))              
            # para tope en rango (self.tope-1,-1,-1):
            #     print("[{}]".format(self.lista[tope]))    
    
    def buscar(self,buscado):
        si es uno mismo. vacío():
            print("La Pila se encuentra vacía")
        de lo contrario:
            la=Falso
            for pos,ele in enumerate(self. lista):
                si ele==buscado:
                    la=Verdadero
                    quebrar
            if la==True:
                print("El número ingresado se encuentra en la posición: {}". formato(pos+1))
            de lo contrario:
                print("El número ingresado no se encuentra en la Pila")
   

# Menú
#1) Lista
# 1) empujar entrada numero(4)
#     2) pop
# 3) mostrar
#     4) eliminar ingrese la posicon a eliminar(2)
#     5) insertar
#     6) buscar
#2) pilas
# 1) empujar
#     2) pop
# 3) mostrar
#4) buscar
#     5) lingitud

# 3) colas
# 1) empujar
#     2) pop
# 3) mostrar
#4) buscar
#     5) lingitudclase Pila: 
    def __init__(self,tamanio):
        yo mismo. lista=[]
        yo mismo. tope=0
        yo mismo. tamaño=tamanio
     
    def vacío(self):
        # if self.tope == 0:
        # volver Verdadero
        # más:
        # devolver Falso
        volver a sí mismo. tope == 0
    
    def push(self,dato):
        yo mismo. size=int(self. tamaño)
        si es uno mismo. tope < yo. tamaño:
            yo mismo. lista += [dato]
            yo mismo. tope += 1
        de lo contrario:
            print("La Pila está Llena")
   
    def Bo(self):
        si es uno mismo. vacío():
            return print("Lista Vacia")    
        de lo contrario:
            arriba = yo. lista[-1]
            yo mismo. tope -= 1
            yo mismo. lista = yo. lista[:-1]
            return print("El valor eliminado es:",top)
            
    def longitud(self):
        volver a sí mismo. cazón
        
    def show(self):
        si es uno mismo. vacío():
            print("La Lista está vacia")
        de lo contrario: 
            print("","Pila","*5,"Posición")
            for pos,top in enumerate(self. lista):
                print([top]" "*(9-len(top)),pos)
                # print("[{}] {:9}".format(top,pos))              
            # para tope en rango (self.tope-1,-1,-1):
            #     print("[{}]".format(self.lista[tope]))    
    
    def buscar(self,buscado):
        si es uno mismo. vacío():
            print("La Pila está vacía")
        de lo contrario:
            la=Falso
            for pos,ele in enumerate(self. lista):
                si ele==buscado:
                    la=Verdadero
                    quebrar
            if la==True:
                print("El número ingresado se encuentra en la posición: {}". formato(pos+1))
            de lo contrario:
                print("El número ingresado no se encuentra en la Pila")
   

# Menú
#1) Lista
# 1) empujar entrada numero(4)
#     2) pop
# 3) mostrar
#     4) eliminar ingrese la posicon a eliminar(2)
#     5) insertar
#     6) buscar
#2) pilas
# 1) empujar
#     2) pop
# 3) mostrar
#4) buscar
#     5) lingitud

# 3) colas
# 1) empujar
#     2) pop
# 3) mostrar
#4) buscar
#     5) lingitud