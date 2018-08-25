f = open("task.txt")
c=0
for i in f:
	print i
	if c == 2:
		break
	c = c+1