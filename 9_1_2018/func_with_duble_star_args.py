#**args 
#*args -> tuple.. tupe/list as input to a function ->*args
#**args -> dict  ..dict then u will **args ->**kwargs

def test_args(**args):
	print args
	j=0
	for k,v in args.iteritems():
		v = v + j
		j = v
	print j	

mydata = {"a":109,"b":20}

print test_args(**mydata)
print test_args(a=100,b=200,c=900)
print test_args(1,2,3)

