#Read mode/operation..(r)
#Write Mode (w)
#append mode... (a)

#Read mode..
f = open("test_data.txt","r")
a = f.readlines()
print len(a)

#Processing..
for i in a:
	b = i.split(" ")
	print b
	for j in b:
		if j == "his":
			print i
		
