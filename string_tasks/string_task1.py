#string task prog1
import sys
test_string = sys.argv[1]

#methode1

str_len = 0

for ch in test_string:
	str_len += 1
	if(str_len > 1):
		print("first and last two characters of string is:{} ".format(test_string[:2] + test_string[-2:]))
		break
if(str_len < 2):
	print('empty string')
	
#methode2	

if(len(test_string)>1):
	print("first and last two characters of string is:{} ".format(test_string[:2] + test_string[-2:]))	
else:
	print('empty string')
