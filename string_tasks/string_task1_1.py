#string task prog1
import sys
no_of_char = int(sys.argv[1])
test_string = sys.argv[2]

#methode1

str_len = 0

for ch in test_string:
	str_len += 1
	if(str_len >= no_of_char):
		print("first and last two characters of string is:{} ".format(test_string[:no_of_char] + test_string[-no_of_char:]))
		break
if(str_len < no_of_char):
	print('empty string')
	
#methode2	

if(len(test_string) >= no_of_char):
	print("first and last two characters of string is:{} ".format(test_string[:no_of_char] + test_string[-no_of_char:]))	
else:
	print('empty string')
		
