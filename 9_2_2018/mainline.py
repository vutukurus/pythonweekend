import sys

print sys.version
print sys.version_info
major = sys.version_info[0]
minor = sys.version_info[1]
micro = sys.version_info[2]

print major, minor, micro
full_ver = str(major)+"."+str(minor)
print full_ver

if (float(full_ver) > float(2.7)):
	log_print("this is python")
else:
	print "this is python < 2.7"

if (float(full_ver) > float(2.7)):
	print ("coding completed and tested > 2.7")
else:
	print "coding completed and tested < 2.7"

	

#print
#excpetional handling..
#oops..
#4-5