#operator overloading..
#+ --> __add__
#- --. __sub__
#* --> __mul__

class point:
	def __init__(self,x,y):
		self.x = x 
		self.y = y 
	
	def __add__(self, other):
		print self.y+other.y

p1 = point(10,20)
p2 = point(30,40)

p1+p2

