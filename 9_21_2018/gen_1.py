#Generators

def range_a(n):
	i = 0
	while (i < n):
		yield i
		i = i+1
a = range_a(10)
print a.next()
print a.next()
print "hello workd"

print a.next()


'''
def range_a(n):
	b=[]
	i=0
	while( i < n):
	  b.append(i)
	  i = i + 1
	return b

print range_a(10)
print range_a(10)
print range_a(10)
'''