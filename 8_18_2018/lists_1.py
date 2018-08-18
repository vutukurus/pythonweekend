#Lists..
'''
a = [10,20,30,40, "50"]

for  i in a:
	print int(i) + 1
'''


#f = open("test_file.txt")
#print f.readlines()
#hwi many 30 and 50..

a = ['10\n', '20\n', '30\n', '40\n', '50\n', '50\n', '30\n', '60\n', '50\n',"adfasd"] #append(90)
cleaned_list = [] #append(90)append(100)
#remove \n..
#typecast..
print a
for i in a:
	print len(i)
	i = i.strip("\n") #strip \n...
	print len(i)
	i = int(i)
	cleaned_list.append(i) #
	
print cleaned_list

#number of 50's..
count = 0

for i in cleaned_list:
	if i == 30:
		count = count+1

print "number of 50;s is {}".format(count)
	



















	
	
	
	
	
	
	
	
	
	

