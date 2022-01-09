Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s=" hola, como estas?"
s[::-1]
'?satse omoc ,aloh '
s[len(s)]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    s[len(s)]
IndexError: string index out of range
s[len(s)-1]
'?'
s.count("o")
3
s.count("hola")
1
s[-4:]
'tas?'
s[15:]
'as?'
s.find("o")
2
s.strip()
'hola, como estas?'
x=s.upper()
x==s
False
x
' HOLA, COMO ESTAS?'
s
' hola, como estas?'
s[14:].upper()
'TAS?'
len(s)%2!=0
False
len(s)
18
s.replace(" ","*")
'*hola,*como*estas?'
s.replace("z","Z")
' hola, como estas?'
