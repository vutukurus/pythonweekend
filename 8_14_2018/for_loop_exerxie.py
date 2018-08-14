#for loop example:
#file = "test.py"

file = "test.py"

count = 0
for i in file:
	count = count + 1
	if i == ".":
		print "Dot is found at {}".format(count)
		break;

if file[count:] == "py":
	print "True"
