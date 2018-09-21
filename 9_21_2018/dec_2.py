def decarotor_func(some_func):
	def wrapper():
		print "Start time"
		some_func()
		print "end time"
	return wrapper
	

@decarotor_func
def add():
	print "add called"

add()