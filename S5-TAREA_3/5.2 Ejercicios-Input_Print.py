CAPACIDADM2=4
PORCENTAJEGRADAS=0.2
PORCENTAJEESPECIAL=0.3
PORCENTAJECOMUNES=0.7

dimensiones=float(input("Dimensiones del estadio (en m2): "))
personasengradas=int(input("Capacidad de personas que caben en las gradas: "))
porcentajeescenario=int(input("Porcentaje que ocupa el escenario: "))
m2gradas=dimensiones*PORCENTAJEGRADAS
m2escenario=dimensiones*(porcentajeescenario/100)
m2disponibles=dimensiones-m2gradas-m2escenario
personastotales=(m2disponibles*4)+personasengradas
print("caben", personastotales, "personas")
precioenntradaespecial=float(input("precio entrada especial: $"))
precioentradacomun=float(input("Precio entrada comun: $"))
print("Ingreso total de venta: $",(personastotales*PORCENTAJEESPECIALES)*precioentradaespecial+(personastotales*PORCENTAJECOMUNES)*precioentradacomun)
