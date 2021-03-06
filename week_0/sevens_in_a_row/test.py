import unittest
from solution import sevens_in_a_row

class TestSolution(unittest.TestCase):
	def test_sevens_in_a_row_0(self):
		self.assertEqual(True, sevens_in_a_row([10,8,7,6,7,7,7,20,-7], 3))

	def test_sevens_in_a_row_1(self):
		self.assertEqual(False, sevens_in_a_row([1,7,1,7,7], 4))

	def test_sevens_in_a_row_2(self):
		self.assertEqual(True, sevens_in_a_row([7,2,1,6,2], 1))


if __name__ == '__main__':
	unittest.main()