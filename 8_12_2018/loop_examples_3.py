#loop example..
#finding index without inbuilt methods..

my_string = "pythonh"

count = 0
for i in my_string:
	if i == "h":
		print count
	count = count+1

print count

'''
#inbuilt index method..
print my_string.index("h")
'''