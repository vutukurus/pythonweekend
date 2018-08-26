#sets_2
a = set() #empty set..
print a
print type(a)

x = [10, 20, 50]
y = [90,10,50]

x=set(x)
y=set(y)
#difference..
print x.difference(y)
print y.difference(x)

#intersection,,
print x.intersection(y)