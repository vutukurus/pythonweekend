class debit(object):
	def __init__(self):
		print "debit card created"
		
	def withdrawl(self):
		print "amount withdranwed"
		
	def dummy(self):
		print "dummy debug card"
		
class credit(debit):
	def __init__(self):
		print "crredit card created"
	
	def dummy(self):
		print "dummy credit card"
		super(credit,self).dummy()

a = credit()
a.dummy()