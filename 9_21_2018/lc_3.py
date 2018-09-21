#list-3
x =[1,2,3,4,5]
y = "abc"

b = [ (i,j) for i in x for j in y]
print b

'''
b=[]
for i in x:
	for j in y:
		b.append((i,j))
		
print b
'''

