#This is a sample billing application..
#Medical shop billing generation..
#Variables/constants
import sys


header_size = 50
print "#"*header_size
#open the file header.txt and then read the header and display
print "#"*header_size

amt = int(sys.argv[1])

tax = (amt * 10)/100

total = tax + amt

print "Total amount to be paid : {}".format(total)
