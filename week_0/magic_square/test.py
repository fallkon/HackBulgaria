import unittest
from solution import magic_square

class TestSolution(unittest.TestCase):
	def test_magic_square_0(self):
		self.assertEqual(False, magic_square([[1,2,3], [4,5,6], [7,8,9]]))

	def test_magic_square_1(self):
		self.assertEqual(True, magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))

	def test_magic_square_2(self):
		self.assertEqual(False, magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))


if __name__ == '__main__':
	unittest.main()