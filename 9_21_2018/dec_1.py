#decorators
import time

def calc_time(some_func):
	def wrapper(*args, **kargs):
		start_time = time.time()
		a = some_func(*args,**kargs)
		end_time = time.time()
		print "time takken",end_time - start_time
		return a
	return wrapper

	
#@calc_time
#def mult(x,y)
#  time.sleep(2)

@calc_time
def add (x,y):
	#time.sleep(5)
	return x+y

print add(100,200)
