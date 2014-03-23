import unittest
from solution import contains_digit

class TestSolution(unittest.TestCase):
	def test_contains_digit_0(self):
		self.assertEqual(False, contains_digit(123, 4))

	def test_contains_digit_1(self):
		self.assertEqual(True, contains_digit(42, 2))

	def test_contains_digit_2(self):
		self.assertEqual(True, contains_digit(1000, 0))


if __name__ == '__main__':
	unittest.main()