#list comprhenssions-2

a = [10,20,50,5,6,7,9,85]
#> 9 
#new list.. [10,20,50,85]
b = [ i for i in a if i > 9]
print b

'''
b=[]
for i in a:
	if i >9 :
		b.append(i)
print b
'''