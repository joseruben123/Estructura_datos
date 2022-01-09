Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
cadena="programa de python"
cadena[6]
'm'
len(cadena)
18
cadena[21]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    cadena[21]
IndexError: string index out of range
i=len(cadena)-1
cadena[i]
'n'
i
17
cadena[len(cadena)-1]
'n'
cadena[0:10]
'programa d'
cadena[10:]
'e python'
cadena[:10]
'programa d'
cadena[:13]
'programa de p'
cadena[:13:2]
'porm ep'
cadena[::-1]
'nohtyp ed amargorp'
cadena[-1:]
'n'
cadena.find("python")
12
cadena.find("p")
0
cadena.find("z")
-1
cadena.find("z")==-1
True
"python" in cadena
True
precio="40"
int(precio)
40
type(int(precio))
<class 'int'>
cadena.upper()
'PROGRAMA DE PYTHON'
cadena.lower()
'programa de python'
cadena
'programa de python'
"6709".upper()
'6709'
cadena.title()
'Programa De Python'
cadena.capitalize()
'Programa de python'
a="       hola"
a.strip()
'hola'
a="     hola      chau         "
a. strip()
'hola      chau'
cadena
'programa de python'
cadena.count("p")
2
cadena.count("o")
2
cadena.replace("python","***")
'programa de ***'
cadema
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    cadema
NameError: name 'cadema' is not defined. Did you mean: 'cadena'?
cadena.replace("a","-")
'progr-m- de python'
cadena.replace("z","i")
'programa de python'
cadena.replace("o","i")
'prigrama de pythin'
