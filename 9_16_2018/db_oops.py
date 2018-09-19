#oops using database..
import sqlite3

class database:
	def __init__(self, db_name):
		print "Connecting to databse"
		self.con = sqlite3.connect('test.db')
		self.cur = self.con.cursor()
	
	def execute_commands(self, command):
		try:
			self.cur.execute('''%s''' %command)
			print "Command executed sucessfully"
		except:
			self.con.close()
	
	def get_data(self):
		print self.cur.fetchone()
		
user1 = database('test.db')
user1.execute_commands("select * from test")
user1.get_data()
user1.get_data()
user1.get_data()
user1.get_data()
