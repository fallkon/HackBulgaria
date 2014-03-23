import unittest
from solution import list_to_number

class TestSolution(unittest.TestCase):
	def test_list_to_number_0(self):
		self.assertEqual(123, list_to_number([1,2,3]))

	def test_list_to_number_1(self):
		self.assertEqual(237148, list_to_number([2, 3, 7, 1, 4, 8]))

	def test_list_to_number_2(self):
		self.assertEqual(1, list_to_number([1]))


if __name__ == '__main__':
	unittest.main()