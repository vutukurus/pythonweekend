
C:\Users\siv\Desktop\weekend\pythonweekend\8_14_2018>python
Python 2.7.6 (default, Nov 10 2013, 19:24:18) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> a = [10,20,30,40,10]
>>> a.remove(20)
>>> print a
[10, 30, 40, 10]
>>> a.remove(10)
>>> print a
[30, 40, 10]
>>> a.pop(0)
30
>>> print a
[40, 10]
>>> a = [10,20,30,40]
>>> a.pop(1)
20
>>> print a
[10, 30, 40]
>>> a = [10,20,30,40]
>>> a.insert(1,10)
>>> print a
[10, 10, 20, 30, 40]
>>>

C:\Users\siv\Desktop\weekend\pythonweekend\8_14_2018>python
Python 2.7.6 (default, Nov 10 2013, 19:24:18) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> a = [10,20,30,40]
>>> a.insert(2,50)
>>> print a
[10, 20, 50, 30, 40]
>>> a.insert(3,"perl")
>>> print a
[10, 20, 50, 'perl', 30, 40]
>>> a.remove("perl")
>>> print a
[10, 20, 50, 30, 40]
>>> a.pop(2)
50
>>> print a
[10, 20, 30, 40]
>>>