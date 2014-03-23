import unittest
from solution import nth_fib_lists

class TestSolution(unittest.TestCase):
	def test_nth_fib_lists_0(self):
		self.assertEqual([1], nth_fib_lists([1], [2], 1))

	def test_nth_fib_lists_1(self):
		self.assertEqual([2], nth_fib_lists([1], [2], 2))

	def test_nth_fib_lists_2(self):
		self.assertEqual([], nth_fib_lists([], [], 100))


if __name__ == '__main__':
	unittest.main()