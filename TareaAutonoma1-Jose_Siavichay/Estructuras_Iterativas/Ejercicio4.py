##factorial de un numero

num = int(input("Ingresa un numero : "))

def fact_while(n):
    factorial_total = 1
    while n > 1:
        factorial_total *= n
        n -= 1
    return factorial_total

print("Su factorial es: ".format(fact_while(num)))
