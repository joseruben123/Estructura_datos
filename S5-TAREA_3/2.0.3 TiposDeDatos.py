Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
"buen"+"dia"
'buendia'
a="buen"
b="dia"
a+" "+b
'buen dia'
c=a+" "+b
c
'buen dia'
len(c)
8
c[0]
'b'
c[8]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    c[8]
IndexError: string index out of range
c[1+1]
'e'
c[len(c)]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    c[len(c)]
IndexError: string index out of range
c[len(c)-1]
'a'
