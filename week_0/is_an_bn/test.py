import unittest
from solution import is_an_bn

class TestSolution(unittest.TestCase):
	def test_is_an_bn_0(self):
		self.assertEqual(True, is_an_bn("helgi"))

	def test_is_an_bn_1(self):
		self.assertEqual(True, is_an_bn(""))

	def test_is_an_bn_2(self):
		self.assertEqual(False, is_an_bn("aabbaabb"))


if __name__ == '__main__':
	unittest.main()