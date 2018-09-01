def test_args(*args):
	print args
	j=0
	for i in args:
		i = i+j
		j=i
	print "sum is",j
	
