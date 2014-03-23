import unittest 
from solution import count_substrings

class TestSolution(unittest.TestCase):
	def test_count_substrings_0(self):
		self.assertEqual(2, count_substrings("This is a test string", "is"))
	
	def test_count_substrings_1(self):
		self.assertEqual(2, count_substrings("This is this and that is this", "this"))

	def test_count_substrings_2(self):
		self.assertEqual(7, count_substrings("alalalkalallalllla", "a"))


if __name__ == '__main__':
	unittest.main()	