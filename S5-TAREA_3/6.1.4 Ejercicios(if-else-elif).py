letra=input("Letra: ")
if len(letra)!=1:
    print("Debe ser solo una letra")
else:
    if letra.lower() in "aeiou":
        print("Es vocal")
