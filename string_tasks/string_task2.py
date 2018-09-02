# my doubt

str1 = "I am an indian , this an apple ,how do u know that, I am an indo , I know that, how old are you"

# condition1 start with 'I'
# condition2 ends with  'that'

temp_str = ''
str_len=0
temp_index=0

for ch in str1:
	if(ch == ',' or ch == str1[-1]):
		if(temp_str[0] == 'I'):
			print( 'start with \'I\' is:' + temp_str )
		if(temp_str[-4:] == 'that'):
			print( 'End with \'that\' is:' +temp_str )
		temp_str = ''
		
	else:
		temp_str += ch
		
print('Thank you')				