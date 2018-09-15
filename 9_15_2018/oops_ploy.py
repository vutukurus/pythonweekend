#polymorphism...duck typing..
#operator overloading..

class Bear:
	def sound(self):
		print "bear talking"
		
class Dog:
	def sound(self):
		print "Dog talking"

def makesound(animaltype):
	animaltype.sound()
	
	
a = Bear()
b = Dog()

makesound(b)