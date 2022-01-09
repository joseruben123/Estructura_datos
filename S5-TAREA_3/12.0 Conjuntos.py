Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
A=set()
type(A)
<class 'set'>
A={1,2,3}
A
{1, 2, 3}
B={1,2,3,1,2,3,1,2,3}
B
{1, 2, 3}
A==B
True
numero=[1,2,3,2,1,3,2,1,3,2,1,2,3]
numeros
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    numeros
NameError: name 'numeros' is not defined. Did you mean: 'numero'?
numero
[1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 2, 3]
C=set(numero)
C
{1, 2, 3}
for n in A:
    print(n)

    
1
2
3
A[0]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    A[0]
TypeError: 'set' object is not subscriptable
len(A)
3
3 in A
True
4 in A
False
4 not in A
True
A
{1, 2, 3}
A.remove(9)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    A.remove(9)
KeyError: 9
A.discaard(9)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    A.discaard(9)
AttributeError: 'set' object has no attribute 'discaard'. Did you mean: 'discard'?
A.discard(9)
A
{1, 2, 3}
A.remove(1)
A
{2, 3}
B
{1, 2, 3}
B.clear()
B
set()
B.add(8)
B.add(9)
A==B
False
A
{2, 3}
A|B
{8, 9, 2, 3}
A&B
set()
A
{2, 3}
B
{8, 9}
A<B
False
B<A
False
A==B
False
B>A
False
B<set([7,8,9])
True
A-B
{2, 3}
B-A
{8, 9}
