#1
lista=[1,2,3,4]
for elemento in lista:
    print(elemento)

#2
articulos={154:["jabon en polvo","limpieza",True],
           248:["talco","cosmetica",False],
           199:["cera para pisos","limpieza",True]}
for clave, valor in articulos.items():
    print("Codigo: ", clave)
    print("Descripion: ", valor[0])
    print("Rubro: ", valor[1])
    if valor[2]:
        print("Hay stock")
    else:
        print("Agotado")
    print("-----------")
    
