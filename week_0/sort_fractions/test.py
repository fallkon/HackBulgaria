import unittest
from solution import sort_fractions

class TestSolution(unittest.TestCase):
	def test_sort_fractions_0(self):
		self.assertEqual([(1, 2), (2, 3)], sort_fractions([(2, 3), (1, 2)]))

	def test_sort_fractions_1(self):
		self.assertEqual([(1, 3), (1, 2), (2, 3)], sort_fractions([(2, 3), (1, 2), (1, 3)]))

	def test_sort_fractions_2(self):
		self.assertEqual([(2, 3), (3, 4), (4, 5)], sort_fractions([(2, 3), (3, 4), (4, 5)]))


if __name__ == '__main__':
	unittest.main()