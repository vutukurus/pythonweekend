import re

msg = "this is amith"

d = re.search("^this .* (amith)$",msg)

if d:
	print d.group()
	print d.group(1)

