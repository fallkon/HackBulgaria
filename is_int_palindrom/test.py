import unittest
from solution import is_int_palindrom

class TestSolution(unittest.TestCase):
	def test_is_int_palindrom_0(self):
		self.assertEqual(True, is_int_palindrom(100001))

	def test_is_int_palindrom_1(self):
		self.assertEqual(True, is_int_palindrom(1111001111))

	def test_is_int_palindrom_2(self):
		self.assertEqual(False, is_int_palindrom(874673465))



if __name__ == '__main__':
	unittest.main()