capacidad=float(input("capacidad del tanque: "))
kmxl=float(input("Rendimietno (Km por litro): "))
recorrido=float(input("km totales a recorrer: "))
kmxtanque=capacidad*kmxl
print("Seran necesarios", recorrido/kmxtanque,"tanques.")
