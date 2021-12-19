##20% de descuento en tienda

total=float(input('Ingrese ek total de su compra: '))

if total>1000:
    descuento=total*0.20
else:
    descuento=0
print('el total a pagar es: $',total - descuento)
print('el descuento aplicado es:$ ', descuento)
