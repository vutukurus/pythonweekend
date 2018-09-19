#Regular expressions
#\d - digits matching
#\w - words matching
#. - matches any single character
#{m,n}-min of m and  max of n occurences
#* - anything
#\s - space matching..
#+ - more than one..
#[..] - matches any characters prsent in int..
#a|b - a or b matches
#^(start) & $(end) - start & end matching..
import re
msg = "This is 9652672101 my number"
a = re.search(".* (\d{10}) .* (\d{10}) .*", msg)
b = re.search(".* (\d{10}) .*", msg)
if a:
	print a.group()
	print a.group(1)
if b:
	print b.group(1)
	