import re
#ameth 
#a,b,c,d,e
#amath ambth amcth amdth
msg = "amcth 78-8989"
d = re.search("am[a,b,c,d,e]th",msg)

if d:
	print d.group()

