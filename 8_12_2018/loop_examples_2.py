#loop_examples.py
#find username (test)
#find his domain(gmail/yahoo/live)


mail_id = "test@gmail.com"

a = ""
b= ""
user_name_found = False
for i in mail_id:
	if user_name_found == False:
		if i == "@":
			#break
			user_name_found =  True
			continue; #you can use continue or else case as well..
		a = a + i
		print a
	else:#i will write logic for finding domain name..
		if i == ".":
			break;
		b = b+i

print "username = {}".format(a)
print "Domain = {}".format(b)
	
