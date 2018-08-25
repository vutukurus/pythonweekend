#pdb..

f = open("duplicate.txt") #read mode..
a = f.readlines()
cleaned = a[0].strip("\n").strip("[").strip("]")
cl_list = cleaned.split(",")
print cl_list
	


'''
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after

       removing all duplicate values with original order reserved.

	output : [12,24,35,88,120,155]

'''