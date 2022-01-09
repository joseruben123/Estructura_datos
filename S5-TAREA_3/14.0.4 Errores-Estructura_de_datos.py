#1
a=[1,2,3,4]
for i in range(len(a)):
    if i==2:
        del a[3]
    print(a[i])


#2
b={"a":[1,2,3],"b":[],"c":[8,6],"d":[],"e":[4]}
for clave in b.keys():
    if b[clave]==[]:
        del b[clave]
