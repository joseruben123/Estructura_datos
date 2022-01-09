Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
A=dict()
A
{}
b={}
B
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    B
NameError: name 'B' is not defined. Did you mean: 'b'?
b
{}
Traducciones={"hola":"hello","adios":"bye"}
Traducciones
{'hola': 'hello', 'adios': 'bye'}
for clave in traducciones/keys():
    print(clave)

    
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    for clave in traducciones/keys():
NameError: name 'traducciones' is not defined. Did you mean: 'Traducciones'?
for clave in traducciones.keys():
    print(clave)

    
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    for clave in traducciones.keys():
NameError: name 'traducciones' is not defined. Did you mean: 'Traducciones'?
for clave in Traducciones.keys():
    print(clave)

    
hola
adios
equipo[5]="maria"
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    equipo[5]="maria"
NameError: name 'equipo' is not defined
del equipo[5]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    del equipo[5]
NameError: name 'equipo' is not defined
equipo
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    equipo
NameError: name 'equipo' is not defined
