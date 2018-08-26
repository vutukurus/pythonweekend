a = "this is pyyython"

b = {}
'''
#t =2
#h =4
b["t"] = 2
b["h"] = 4
b["t"]=9
print b
'''
for i in a:
	b[i] = a.count(i)

print b
for i,j in b.iteritems():
	print "count of {} is {}".format(i,j)