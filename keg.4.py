Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> name = 'naura salsabila'
>>> nim = 159
>>> tall = 1.48
>>> weight = 52
>>> yearofbirth = 2000
>>> me = ( yearofbirth, weight , tall ,nim , name)
>>> data = [ yearofbirth, weight, tall, nim, name]
>>> type (me)
<class 'tuple'>
>>> #because (me) used the usual open and close brackets '()'
>>> me[0]
2000
>>> a = nim%4; me[a]
159
>>> type (me[a])
<class 'int'>
>>> #because results of 'me[a]' is integers(bilangan bulat). Integers is the number dont have comma in behind number
>>> me[a:4]
(159,)
>>> type (me[4])
<class 'str'>
>>> #because inside me[4] there is string. That is 'naura salsabila'
>>> me[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    me[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> type (data)
<class 'list'>
>>> #because (data) used the square brackets open and close brackets '[]'
>>> type (data[4])
<class 'str'>
>>> #because inside data[4] have string.
>>> data [4] [5]
' '
>>> data [4][5]
' '
>>> data[4][a:6]
'ra '
>>> da' '
SyntaxError: invalid syntax
>>> 
>>> type (data[4][5])
<class 'str'>
>>> #because they is string.
>>> type (data[4][a:6])
<class 'str'>
>>> #because they is a string
>>> data[0] = 'oke' ; data
['oke', 52, 1.48, 159, 'naura salsabila']
>>> type (data[0] = 'oke' ; data)
SyntaxError: invalid syntax
>>> data [-a]
1.48
>>> type (data[-a])
<class 'float'>
>>> #because results of that is float. the number who have number behind the comma
>>> range (a)
range(0, 3)
>>> type (range
      9a
      
SyntaxError: invalid syntax
>>> type (range (a))
<class 'range'>
>>> <class 'range'>
SyntaxError: invalid syntax
>>> #because range (a) results "list"
