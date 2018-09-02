#own print msgs.
import sys

print sys.version
print sys.version_info
#major = sys.version_info[0]
#minor = sys.version_info[1]
#micro = sys.version_info[2]

major,minor,micro,_,_ = sys.version_info

full_ver = str(major)+"."+str(minor)

def log_print(msg):
	if (float(full_ver) > float(2.7)):
		print ("{}").format(msg)
	else:
		print "{}".format(msg)

