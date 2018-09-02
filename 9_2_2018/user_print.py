a = "hello world"
b = a.split(" ")
print b

c = 0
d = 0
while(1):
	print b[0][c] + "\t" + b[1][d]
	
	if c < len(b[0])-1:
		c = c+1
	else:
		break
	if d < len(b[1])-1:
		d = d+1
	else:
		break
	