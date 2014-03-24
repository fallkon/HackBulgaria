import unittest
from solution import prime_factorization

class TestSolution(unittest.TestCase):
	def test_ (self):
		self.assertEqual([(2, 1), (5, 1)], prime_factorization(10))

	def test_ (self):
		self.assertEqual([(2, 1), (7, 1)], prime_factorization(14))

	def test_ (self):
		self.assertEqual([(2, 3), (5, 3)], prime_factorization(1000))


if __name__ == '__main__':
	unittest.main()