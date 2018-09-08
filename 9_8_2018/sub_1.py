#subprocess module..
import subprocess
import time

#simple way of using..
#a = subprocess.call("dir", shell=True)

#if u want to get ouput also to a variable..
a = subprocess.Popen("ping 192.168.0.106", shell=True,stdout=subprocess.PIPE)
print "--------"

print "="*30

print a.communicate()[0]


#100 ips//
ips = ["10.1.2", "10.3.4","10.9.4"]
for i in ips:
	st_time = time.time()
	cmd = "ping"+" "+i
	print "executing {}".format(cmd)
	a = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)
	print a.communicate()[0]
	e_time = time.time()
	print e_time-st_time
	








