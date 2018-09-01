#args..

def test_args(*args):
	print args
	j=0
	for i in args:
		i = i+j
		j=i
	print "sum is",j

a = (10,20)
print test_args(*a)
print test_args(100,200,300)
print test_args(100,200,300,800)
print test_args(100,200,300,800,900,9,82,9)
