#Exception Handling
#exit gracefull..

a = [1,2,3]

try:
	a =(10,90,100)
	for i in a:
		print i

except:
	print "Index is out of range, see index length"
	print "mail sent"

print "clean up and exit"