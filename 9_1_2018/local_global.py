#local and globals in python

def test():
	global a
	a = 10
	print a
	
	
a = 100
test()
print a