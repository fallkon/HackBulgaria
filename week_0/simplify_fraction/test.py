import unittest
from solution import simplify_fraction

class TestSolution(unittest.TestCase):
	def test_simplify_fraction_0(self):
		self.assertEqual((1, 3), simplify_fraction((3,9)))

	def test_simplify_fraction_1(self):
		self.assertEqual((1, 7), simplify_fraction((1,7)))

	def test_simplify_fraction_2(self):
		self.assertEqual((3, 22), simplify_fraction((63,462)))


if __name__ == '__main__':
	unittest.main()