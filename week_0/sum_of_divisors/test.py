import unittest
from solution import sum_of_divisors

class TestSolution(unittest.TestCase):
	def test_sum_of_divisors_0(self):
		self.assertEqual(15, sum_of_divisors(8))

	def test_sum_of_divisors_1(self):
		self.assertEqual(8, sum_of_divisors(7))

	def test_sum_of_divisors_2(self):
		self.assertEqual(2340, sum_of_divisors(1000))


if __name__ == '__main__':
	unittest.main()