##de millas a kilometros distancia de ciudades

def menu_selection():
    print(4 * "~", "Disancia de ciudades", 4 * "~")
    print ("[ 2 ] Miles to Km")

c1=(input('Nombre de la ciudad 1: '))
c2=(input('Nombre de la ciudad 2: '))
d1=float(input('distancia en millas de la ciudad 1: '))
d2=float(input('distancia en millas de la ciudad 2: '))

main = True

while not main == False:
    menu_selection()
    user_selection = str(input("Presione 2 si desea realizar la accion: "))

    if(user_selection == "1"):
        user_in_km = int(input("Ingrese las millas de la ciudad: "))
        to_miles = round(user_in_km / 1.6093, 3)
        
        print(30 * "~%")
        print("{} Km converts to {} Miles.".format(user_in_km,to_miles))
        print(30 * "%~")
        keep_converting = input("Would you like to continue converting? [ yes  |  no ]")
        if(keep_converting == "yes"):
            continue
        elif(keep_converting == "no"):
            main_loop = False
          
        else:
            print("Wrong choice! Bye Bye!")
            break  
           
        
    elif(user_selection == "2"):
        millas1 = int(input("Ingrese las millas de la ciudad 1:  "))
        km1 = round(user_in_miles * 1.6093, 3)
        millas2 = int(input("Ingrese las millas de la ciudad 2:  "))
        km2 = round(user_in_miles * 1.6093, 3)
        
       
        print("{} Millas son {} Kilometros.".format(millas1,km1))
        print("{} Millas son {} Kilometros.".format(millas2,km2))

        distancia=km1-km2
      
        print('La distancia entre', c1, 'y la ciudad',c2,'es',distancia)
          
        else:
            print("opcion incorrecta!")
            break  
    
