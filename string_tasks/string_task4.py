# string task4

#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string is already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.

import sys

test_str = sys.argv[1]
str_len = 0

for char in test_str:
	str_len += 1
	
	if(str_len >= 3):
		if(str_len >= 3):
			if(test_str[-3:] == 'ing'):
				test_str += 'ly'
			else:
				test_str += 'ing'
		break


print ( test_str )		
	