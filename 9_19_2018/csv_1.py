#csv file handling..
import csv

f= open("abc.csv", "r")
c = csv.reader(f)

g = open("abc_write.csv", "wb")
d = csv.writer(g) #this is the extra line..

for i in c:
	if i[1] == "DL":
		print i
		if int(i[0]) > 5:
			d.writerow(i)
		


