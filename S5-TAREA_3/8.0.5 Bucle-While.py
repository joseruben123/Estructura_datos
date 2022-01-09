pares=0
n=int(input("Numero (-1 para teminar el progrma): "))
while n!=-1:
    if n%2==0:
        pares+=1
    suma=0
    while n!=0:
        digito=n%10
        suma+=digito
        n=n//10
    print("Suma de sus digitos: ", suma)
    n=int(input("Numero (-1 para teminar el progrma): "))
print("Se ingresaron", pares, "numeros pares")
