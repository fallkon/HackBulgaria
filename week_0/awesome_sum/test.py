import unittest
from solution import awesome_sum


class TestSolution(unittest.TestCase):
	def test_awesome_sum_0(self):
		self.assertEqual(11, awesome_sum(5, 6))

	def test_awesome_sum_1(self):
		self.assertEqual(24, awesome_sum(12, 12))

	def test_awesome_sum_2(self):
		self.assertEqual(37, awesome_sum(25, 12))

	

if __name__ == '__main__':
	unittest.main()