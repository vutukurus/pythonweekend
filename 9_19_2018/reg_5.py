import re
#a = "XYZ_ABC_00189"
a = "xyx_abc_abcde"

b =  re.search("\w\w\w_\w\w\w_(\d\d\d\d\d)",a)

if b:
	print b.group(1)