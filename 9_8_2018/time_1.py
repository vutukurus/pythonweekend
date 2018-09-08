import time

#todays time..
print time.ctime()

#sleep()
print "I am going to sleep"
s=time.time()
time.sleep(7)
e=time.time()
print "I woke up..."
print e-s
