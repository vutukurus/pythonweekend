#catching specific errors
#IndexError

a = (10,20,"a")
print "reved data",a

try:
	for i in a:
		print i/10
except (IndexError): #only when try block fail..
	print "error occured"
finally:#try block pass or fail..
	print "db connection closed"
