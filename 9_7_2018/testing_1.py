def testing(numbers):
	b= []
	c= ""
	for i in numbers:
		if type(i) == type(c): #str, isinstance(i,str)
			return "Number are not allowed"
		b.append(i+12)
	return b
	
#print testing(["a","b","c"])
