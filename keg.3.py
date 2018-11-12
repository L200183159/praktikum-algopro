Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Naura Salsabila'
>>> Nim = 'L200183159'
>>> X = '1' + Nim[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type (a)
<class 'int'>
>>> #because a is integers
>>> type (b)
<class 'int'>
>>> #because b is integers
>>> a/b
77.26666666666667
>>> type (a/b)
<class 'float'>
>>> #because results of a/b is float. Float is the numbers has a number behind the comma
>>> a//b
77
>>> type(a//b)
<class 'int'>
>>> #because a//b is integers.Integers is the number dont have number behind the comma
>>> 10*(a-999)
1600
>>> type (10*(a-999))
<class 'int'>
>>> #because 10*(a-999) is integers (The number dont have number behind the comma)
>>> b**2
225
>>> type (b**2)
<class 'int'>
>>> #because b**2 is integers who the number dont have the comma)
>>> a%b
4
>>> type (a%b)
<class 'int'>
>>> #because a%b is integers.
>>> 
>>> 
>>> c = 12.5
>>> type (c)
<class 'float'>
>>> #because c is float who the number has a number behind the comma
>>> a/c
92.72
>>> type (a/c)
<class 'float'>
>>> #because results a/c is float (number has a number behind comma)
>>> a//c
92.0
>>> type (a//c)
<class 'float'>
>>> #because results of a//c is float. but these numbers can also be called integers, because usually if behind a comma is 0, the number can be rounded
>>> a%c
9.0
>>> type (a%c)
<class 'float'>
>>> #because results of a//c is float. but these numbers can also be called integers, because usually if behind a comma is 0, the number can be rounded
>>> c>b
False
>>> #because number of c is smaller than b
>>> type (c>b)
<class 'bool'>
>>> #
