
a = ["10","20","30","asdfdsa"]

for i in a: #0 to 9
	first_char = i[0]
	print first_char
	for j in range(10):
		if str(j) == first_char:
			i = int(i)
			print "type caste applied for {}".format(i)


