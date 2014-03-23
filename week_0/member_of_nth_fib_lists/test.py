import unittest
from solution import member_of_nth_fib_lists

class TestSolution(unittest.TestCase):
	def test_member_of_nth_fib_lists_0(self):
		self.assertEqual(False, member_of_nth_fib_lists([1, 2], [3, 4], [5, 6]))

	def test_member_of_nth_fib_lists_1(self):
		self.assertEqual(True, member_of_nth_fib_lists([1, 2], [3, 4], [1,2,3,4,3,4,1,2,3,4]))

	def test_member_of_nth_fib_lists_2(self):
		self.assertEqual(True, member_of_nth_fib_lists([7,11], [2], [7,11,2,2,7,11,2]))


if __name__ == '__main__':
	unittest.main()