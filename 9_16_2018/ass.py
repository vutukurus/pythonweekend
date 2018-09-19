str1 = '{2}, {1} and {0}'.format('a', 'b', 'c')
str2 = '{0}{1}{0}'.format('abra', 'cad')
print(str1, str2)


a = 2
b = '3.77'
c = -8
str1 = '{0:.4f} {0:3d} {2} {1}'.format(a, b, c)
print(str1)


import string
import string 

Line1 = "And Then There Were None"
Line2 = "Famous In Love"
Line3 = "Famous Were The Kol And Klaus"
Line4 = Line1 + Line2 + Line3
print(string.find(Line1, 'Were'), string.count((Line4), 'And'))
