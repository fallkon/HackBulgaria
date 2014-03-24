import unittest
from solution import nth_fibonacci

class TestSolution(unittest.TestCase):
	def test_nth_fibonacci_0(self):
		self.assertEqual(2, nth_fibonacci(3))

	def test_nth_fibonacci_1(self):
		self.assertEqual(55, nth_fibonacci(10))

	def test_nth_fibonacci_2(self):
		self.assertEqual(1, nth_fibonacci(1))



if __name__ == '__main__':
	unittest.main()