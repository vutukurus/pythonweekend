#oops_2

class Bank(object):
	
	def __init__(self, name, amt):
		print "New user {} and amount is {}".format(name,amt)
		self.name = name
		self.amount = amt
		
		
	def balance(self):
		print "Balance is {}".format(self.amount)
		
	def deposit(self, amt):
		self.amount = self.amount + amt
		print "amount deposited {}".format(self.amount)
		
	def withdrawl(self):
		print "amount withdrawn"

user1 = Bank("ramesh", 500)
user2 = Bank("ramesh", 300)
user1.deposit(100)
user2.deposit(100)

