import unittest
from solution import sum_of_min_and_max

class TestSolution(unittest.TestCase):
	def test_sum_of_min_and_max_0(self):
		self.assertEqual(10,  sum_of_min_and_max([1,2,3,4,5,6,8,9]))

	def test_sum_of_min_and_max_1(self):
		self.assertEqual(90, sum_of_min_and_max([-10,5,10,100]))

	def test_sum_of_min_and_max_2(self):
		self.assertEqual(2, sum_of_min_and_max([1]))


if __name__ == '__main__':
	unittest.main()