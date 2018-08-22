a = [10,20,30]



a = [ 10,200 , [30,40], [80,90, [900,800]] ]


print a[0]
print a[1]
print a[2]
print a[2][0]
print a[2][1]


C:\Users\siv\Desktop\weekend\pythonweekend\8_22_2018>python
Python 2.7.6 (default, Nov 10 2013, 19:24:18) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> a = [10,20, [80,90], [900, 800, [15,25]]]
>>> print a[3]
[900, 800, [15, 25]]
>>> print a[3][0]
900
>>> print a[3][1]
800
>>> print a[3][2]
[15, 25]
>>> print a[3][2][0]
15
>>> print a[3][2][1]
25
>>>