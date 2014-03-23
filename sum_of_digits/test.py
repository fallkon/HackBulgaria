import unittest
from solution import sum_of_digits

class TestSolution(unittest.TestCase):
	def test_sum_of_digits_0(self):
		self.assertEqual(43, sum_of_digits(1325132435356))

	def test_sum_of_digits_1(self):
		self.assertEqual(10, sum_of_digits(37))

	def test_sum_of_digits_2(self):
		self.assertEqual(37, sum_of_digits(203040105005050505))


if __name__ == '__main__':
	unittest.main()