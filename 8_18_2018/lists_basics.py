#split and join..
a = "cat-dog-elephant"
print a.split("-")

b = ["1","dog","fox"]
print "-".join(b)

a = "I am indian,that is false,this is that"
d = a.split(",")
for i in d:
	print i
	if i[0] == "I":
		print "starting with I for {}".format(i)
	b = i.split(' ')
	print b
	if b[-1] == "that":
		print "ending with that for {}".format(i)