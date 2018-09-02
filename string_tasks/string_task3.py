#string task3
#replace next occurrences of first char with $
import sys

test_str = sys.argv[1]

replace_str = ''
str_len = 0

for ch in test_str:
	if(str_len > 0 and ch == test_str[0] ):
		replace_str += '$'
	else:
		replace_str += ch
		str_len += 1
		
print(replace_str)