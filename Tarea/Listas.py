Clase Lista:
    def __init__(self,dato=[]):
        yo mismo. lista=dato
    
    def push(self,dato):
        yo mismo. lista. append(dato)
        
    def Borrar(self):
        si es uno mismo. vacío():
            print("No existe elementos en la lista")
        de lo contrario:
            dato=yo. lista. pop()
            regresar el dato
    
    def eliminarlosElementos(self,pos):
        si es uno mismo. vacío():
            print("La lista se encuentra vacía")
        elif pos<0 o pos>=len(self. lista):
            return print("No se encuentra esa posición en la lista")
        de lo contrario:
            yo mismo. lista=self. lista[0:pos]+self. lista[pos+1:]
            return print(self. lista[pos])
    # def eliminarElementos(self,pos):
    # if pos<0 o pos>=len(self.lista):
    #         return print("No existe ese valor en la lista")
    # más:
    #         listaA=[]
    # para ind en el rango (0, pos):
    #             listaA+=[self.lista[ind]]
    # para ind ind in range(pos+1,len(self.lista)):
    #             listaA+=[self.lista[ind]]
    #         self.lista=listaA
    # devolver self.lista
        
    def Mostrar(self):
        si es uno mismo. vacío():
            print("Lista vacia")
        de lo contrario: 
            print("lista"",*5,"Posicion")                
            for pos, ele in enumerate(self. lista):
                print("[{:}] {:9}". format(ele,pos))
                
    def ingreseelElemento(self,pos,elem):
        si pos < 0 o pos > (len(self. lista)+1):
               return print("Posición incorrecta")
        de lo contrario: 
            yo mismo. lista. insertar(pos,elem)
            print("El elemento que se ingreso era: '{}' en la posición: {}". format(elem,pos))
        devolución
                
    
    def vacío(self):
        # if self.tope == 0:
        # regresar Verdadero
        # más:
        # regresar Falso
        return len(self. lista) == 0
    
    def buscarElemento(self,buscado):
        # print("Buscar un número en la lista")
        si es uno mismo. vacío():
            print("Lista vacia")
        de lo contrario:
            op=Falso
            for pos,ele in enumerate(self. lista):
                si ele==buscado:
                    op=Verdadero
                    quebrar
            if op==True:
                print("El número que ingresó se encuentra en la posición: {}". formato(pos+1))
                #print("El valor que ingreso se encuentra en la posicion: {}".format(pos+1))
            de lo contrario:
                print("El número que ingresó no se encuentra en la lista")
    
numeros=Lista()
# numeros.push("Daniel")
# numeros.push("Yadi")
#numeros.push("Ana")
#numeros. Borrar("1")
#["Daniel","Yadi","Ana"]
# print(numeros.pop())
# print(numeros.pop())
#print(numeros.lista)