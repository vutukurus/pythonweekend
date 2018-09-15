#access speicifiers/modifires..
#private(__), protected(_), public..

class debit:
	def __init__(self):
		print "debit card created"
		
	def deposit(self,amount):
		self.__amount = amount
		print "my amount is {}".format(self.__amount)

	def balance(self):
		print "availabel balnace is {}".format(self.__amount)
	
a = debit()
a.deposit(100)
a.balance()
a.amount= 900
print a.amount
#a._debit__amount = 900
a.balance()
