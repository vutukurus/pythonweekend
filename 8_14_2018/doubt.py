str1 = "I am an Indian, this an apple,how do u know that,I am an indo ,I know that , how old are you"

# condition1 start with 'I'
# condition2 ends with  'that'
str_ptr = 0
end_ptr = 0

for i in str1:
	if i == ",":
		print "found a comma"
		print str1[str_ptr:end_ptr]
		first_chr = 0
		for j in str1[str_ptr:end_ptr]:
			print "sdfsad"
			if j != "," or j != " " :
				first_chr = j
				print "tis",first_chr
				break
		if first_chr == "I":
			print "Found---->",str1[str_ptr:end_ptr]
		print "start pointer",str1[str_ptr]
		print "start pointer no",str_ptr
		print "end pointer",str1[end_ptr]
		print "end pointer no",end_ptr
		str_ptr = end_ptr+1
	end_ptr = end_ptr + 1
	