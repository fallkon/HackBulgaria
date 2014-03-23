import unittest
from solution import biggest_difference

class TestSolution(unittest.TestCase):
	def test_biggest_difference_0(self):
		self.assertEqual(-6, biggest_difference([2, 8, 4, 3]))

	def test_biggest_difference_1(self):
		self.assertEqual(-7, biggest_difference([7, 9, 3, 6, 2]))

	def test_biggest_difference_2(self):
		self.assertEqual(-3, biggest_difference([7, 10]))


if __name__ == '__main__':
	unittest.main()