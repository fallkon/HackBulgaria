import unittest
from solution import is_increasing

class Testolution(unittest.TestCase):
	def test_is_increasing_0(self):
		self.assertEqual(True, is_increasing([1,2,3,4,5]))

	def test_is_increasing_1(self):
		self.assertEqual(False, is_increasing([2, 8, 4, 3, 3, 0, 9]))

	def test_is_increasing_2(self):
		self.assertEqual(True, is_increasing([12, 14, 16, 33, 56, 77]))



if __name__ == '__main__':
	unittest.main()