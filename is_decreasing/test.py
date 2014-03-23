import unittest
from solution import is_decreasing

class TestSolution(unittest.TestCase):
	def test_is_decreasing_0(self):
		self.assertEqual(True, is_decreasing([5,4,3,2,1]))

	def test_is_decreasing_1(self):
		self.assertEqual(False, is_decreasing([1,2,3]))

	def test_is_decreasing_2(self):
		self.assertEqual(True, is_decreasing([100, 50, 20]))


if __name__ == '__main__':
	unittest.main()