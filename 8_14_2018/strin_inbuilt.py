#string in built methods..
#len
my_string = "Pythotn"

print len(my_string)

#index...
print my_string.index("t")

#capitalize
print my_string.upper()
print my_string.lower()

#count..
print my_string.count("t")
print my_string.count("t",3,6)

#find... >=0
print my_string.find("t")
print my_string.find("e")

#replace..
my_string = my_string.lower()
print my_string.replace("p","r")

#endswith and startswith..
file = "test.py"
if file.endswith(".py") == True:
	print "this is a pyton file"

print file.startswith("te")
print file.startswith("fe")













