Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
11-(4%2+10)
1
"30"+2
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    "30"+2
TypeError: can only concatenate str (not "int") to str
"30"+"2"
'302'
"hola"[len("hola"]
       
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
len(124)
       
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    len(124)
TypeError: object of type 'int' has no len()
"hola"[len("fin")]
       
'a'
"hola"[11-(4%2+10)]
       
'o'
int["4"]
       
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    int["4"]
TypeError: 'type' object is not subscriptable
int("4")
       
4
int(4)
       
4
int("z")
       
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    int("z")
ValueError: invalid literal for int() with base 10: 'z'
4<"f"
       
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    4<"f"
TypeError: '<' not supported between instances of 'int' and 'str'
"palabra"="rama"
       
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
"palabra"=="rama"
       
False
