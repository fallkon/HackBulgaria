import unittest 
from solution import is_number_balanced

class TestSolution(unittest.TestCase):
	def test_is_number_balanced_0(self):
		self.assertEqual(True, is_number_balanced(1238033))

	def test_is_number_balanced_1(self):
		self.assertEqual(True, is_number_balanced(5))


	def test_is_number_balanced_2(self):
		self.assertEqual(False, is_number_balanced(13))

if __name__ == '__main__':
	unittest.main()