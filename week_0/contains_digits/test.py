import unittest
from solution import contains_digits

class TestSolution(unittest.TestCase):
	def test_contains_digits_0(self):
		self.assertEqual(False, contains_digits(402123, [0, 3, 4]))

	def test_contains_digits_1(self):
		self.assertEqual(False, contains_digits(666, [6,4]))

	def test_contains_digits_2(self):
		self.assertEqual(True, contains_digits(456, []))

if __name__ == '__main__':
	unittest.main()