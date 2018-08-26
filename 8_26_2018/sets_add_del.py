
#normal sets are mutable..
a = set()
a.add(90) #adding elements to set..
a.add(100) #adding elements to set..
a.add(120) #adding elements to set..
print a

#remove element from set..
a.remove(90)
print a

#clear and copy in sets..
a.clear()
print a

#deepcopy/shallow copy
a =set([10,20,30])
b = set([40,50])

a = b.copy()
b.add(90)

print a
print b














