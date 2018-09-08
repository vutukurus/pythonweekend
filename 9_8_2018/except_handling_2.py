print "connectint to db"


a = (10,20,30)
print "reved data",a

try:
	for i in a:
		b = i/2
		print b
except: #only when try block fail..
	print "error occured"
finally:#try block pass or fail..
	print "db connection closed"
