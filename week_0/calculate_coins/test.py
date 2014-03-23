import unittest 
from solution import calculate_coins

class TestSolution(unittest.TestCase):
	def test_calcullate_coins_0(self):
		self.assertEqual({1: 1, 2: 1, 100: 0, 5: 0, 10: 0, 50: 1, 20: 0}, calculate_coins(0.53))

	def test_calcullate_coins_1(self):
		self.assertEqual({1: 0, 2: 2, 100: 8, 5: 0, 10: 0, 50: 1, 20: 2}, calculate_coins(8.94))

	def test_calcullate_coins_2(self):
		self.assertEqual({1: 0, 2: 0, 100: 2, 5: 0, 10: 0, 50: 0, 20: 0}, calculate_coins(2))		



if __name__ == '__main__':
	unittest.main()