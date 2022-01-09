Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
numeros=[]
numeros
[]
type(numeros)
<class 'list'>
numeros=[1,2,3]
numeros
[1, 2, 3]
letras=list()
letras
[]
letras=list("ABC")
letras
['A', 'B', 'C']
print(list("ZXU"))
['Z', 'X', 'U']
for i in range(len(letras)):
    print(letras[i])

    
A
B
C
i=0
while i<len(letras):
    print(letras[i])
    i+=1

    
A
B
C
for elemento in letras:
    print(elemento)

    
A
B
C
dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
numeros+letras
[1, 2, 3, 'A', 'B', 'C']
numeros
[1, 2, 3]
letras
['A', 'B', 'C']
numeros+list(range(4,10))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
C=numeros+[letras]
C
[1, 2, 3, ['A', 'B', 'C']]
len(C)
4
len(numeros+letras)
6
C[1]
2
type(C[1])
<class 'int'>
C[3]
['A', 'B', 'C']
type(C[3])
<class 'list'>
C[3:]
[['A', 'B', 'C']]
C[::-1]
[['A', 'B', 'C'], 3, 2, 1]
C
[1, 2, 3, ['A', 'B', 'C']]
C[3][1]
'B'
C[len(C)-1]
['A', 'B', 'C']
"A" in C
False
2 in C
True
C.count(2)
1
.count(["A","B","C"])
SyntaxError: invalid syntax
C.count(["A","B","C"])
1
numeros.insert(4,C)
NUMEROS
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    NUMEROS
NameError: name 'NUMEROS' is not defined
numeros
[1, 2, 3, [1, 2, 3, ['A', 'B', 'C']]]
numeros.remove(3)
numeros
[1, 2, [1, 2, 3, ['A', 'B', 'C']]]
numeros.clear()
numeros
[]
dir(tuple)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
tupla1=()
tupla1
()
tupla2=("ema")
tupla2
'ema'
tuple3=tuple("ema")
tuple3
('e', 'm', 'a')
nueva[0]="A"
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    nueva[0]="A"
NameError: name 'nueva' is not defined
del nueva[2]
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    del nueva[2]
NameError: name 'nueva' is not defined
nueva
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    nueva
NameError: name 'nueva' is not defined
A=[1,2,3]
B(A,)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    B(A,)
NameError: name 'B' is not defined
A=[1,2,3]
b
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    b
NameError: name 'b' is not defined
B
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    B
NameError: name 'B' is not defined
