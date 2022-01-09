dia=int(input("Dia de tu nacimiento: "))
mes=int(input("Mes de tu nacimiento: "))
anio=int(input("Anio de tu nacimiento: "))
print(dia,"/",mes,"/",anio)

##parte 2
fecha=int(input("Fecha en formato DDMMAAAA: "))
anio=fecha%10000
dia=fecha//1000000
mes=(fecha//10000)%100
print(dia,"/",mes,"/",anio)
