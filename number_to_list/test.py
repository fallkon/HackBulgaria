import unittest
from solution import number_to_list

class TestSolution(unittest.TestCase):
	def test_number_to_list_0(self):
		self.assertEqual([1, 2, 3], number_to_list(123))

	def test_number_to_list_1(self):
		self.assertEqual([2, 3, 8, 9, 0], number_to_list(23890))

	def test_number_to_list_2(self):
		self.assertEqual([1], number_to_list(1))

if __name__ == '__main__':
	unittest.main()