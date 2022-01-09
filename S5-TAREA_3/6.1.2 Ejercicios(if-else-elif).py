nombre1=input("un nombre: ")
nombre2=input("otro nombre: ")
indice_final_nombre1=len(nombre1)-1
indice_final_nombre2=len(nombre2)-1
if nombre1[0]==nombre2[0] or nombre1[indice_final_nombre1]==nombre2[indice_final_nombre2]:
    print("Coincidencia")
else:
    print("No hay coincidencia")
