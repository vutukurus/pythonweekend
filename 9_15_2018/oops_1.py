#oops
#constructor.. __init__
#class..
#self --> instance
#method -> function..

class car:

	def __init__(self, fuel):
		print "Fuel chekced or not {}".format(fuel)
		print " i am called by defautl"
		
	def eng_start(self):
		print "Engine started/running"

	def forward(self):
		print "Car moved forward"

#create an object to a class..
a = car("Yes")
b = car("no")
a.eng_start()
a.forward()

