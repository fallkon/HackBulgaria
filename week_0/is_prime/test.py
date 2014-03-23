import unittest
from solution import is_prime

class TestSolution(unittest.TestCase):
	def test_ist_prime_0(self):
		self.assertEqual(False, is_prime(1))

	def test_ist_prime_1(self):
		self.assertEqual(True, is_prime(11))

	def test_ist_prime_2(self):
		self.assertEqual(False, is_prime(8))


if __name__ == '__main__':
	unittest.main()