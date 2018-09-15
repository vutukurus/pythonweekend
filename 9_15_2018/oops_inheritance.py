#inherticance..
#single inheritance
#super.../method overloading..

class Bank:
	def bank_name(self):
		print "bank name"

	def dummy(self):
		print "dummy bank"

class debit:
	def __init__(self):
		print "debit card created"
		
	def withdrawl(self):
		print "amount withdranwed"
		
	def dummy(self):
		print "dummy debug card"
		
class credit(debit,Bank):
	def __init__(self):
		print "crredit card created"
	
		
a = credit()
a.withdrawl()
a.bank_name()
a.dummy()