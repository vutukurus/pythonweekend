import unittest
import testing_1

class add_ten(unittest.TestCase):

	def test_pp(self):
		output = testing_1.testing([1,2,3,4])
		self.assertEqual(output,[11,12,13,14])
		
	def test_big(self):
		output = testing_1.testing([10,20,30,40])
		self.assertEqual(output,[20,30,40,50])

	def test_let(self):
		output = testing_1.testing(["a","b","c"])
		self.assertEqual(output,"Number are not allowed")	
	
if __name__ == "__main__":
	unittest.main()