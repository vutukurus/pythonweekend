#Dict/Sets
#key, value pairs..
sample_dict = {} #empty dict..

sample_dict = {"hyundai":"i20", "maruti":["swift","scross"]}

#duplicate keys should not be used
#dicts are order independent..
#keys can be used as - > strings, tuples, dicts, int
#u cannot use -> lists (mutable)
print sample_dict["hyundai"]
print sample_dict["maruti"]

for  i,j in sample_dict.iteritems():
	print i
	print j
	
sample_dict = {[10,20]:"i20", 40:["swift","scross"]}

print sample_dict[(10,20)]
#int, string, tupels.. u canto change them
#list -->mutable datatupe are not allowed as keys



