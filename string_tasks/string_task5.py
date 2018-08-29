# string task 5
# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'bad' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. 
# Sample String : 'The lyrics is not that poor!'
# Expected Result : 'The lyrics is good!

test_str = 'The lyrics is not that poor!'

str_len = 0

start_char_no = 0
#end_char_length = 0
check_ch = 0

for ch in test_str:
	if ch == 'n':
		if test_str[str_len:str_len+3] == 'not' :
			start_char_no =str_len
			check_ch = 1
	if ch == 'p':
		if check_ch == 1:
			if test_str[str_len:str_len+4] == 'poor' :
				#end_char_length = str_len+ 4
				
				print ( test_str[:start_char_no] + 'good' + test_str[str_len+4:])  # test_str[end_char_length:]
				break
	str_len += 1

