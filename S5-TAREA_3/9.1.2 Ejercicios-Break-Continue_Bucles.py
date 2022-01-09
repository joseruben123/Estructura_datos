anioInicio=int(input("Anio inicial: "))
anioFin=int(input("Anio final"))
for anio in range(anioInicio,anioFin+1):
    if not anio%10==0:
        continue
    if not anio%4==0:
        continue
    if anio%100!=0 or anio%400==0:
        print(anio)
