a = [1234] #1
b = a[0]
b = str(b)
print type(b)

d=""
for i in b:
	c = i+"," #c= i,
	d = d + c
	
print d.strip(",")


