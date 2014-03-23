import unittest
from solution import goldbach

class TestSolution(unittest.TestCase):
	def test_goldbach_0(self):
		self.assertEqual([(2, 2)], goldbach(4))

	def test_goldbach_1(self):
		self.assertEqual([(3,7), (5,5)], goldbach(10))

	def test_goldbach_2(self):
		self.assertEqual([(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)], goldbach(100))


if __name__ == '__main__':
	unittest.main()

	