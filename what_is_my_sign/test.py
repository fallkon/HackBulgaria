import unittest
from solution import what_is_my_sign

class TestSolution(unittest.TestCase):
	def test_what_is_my_sign_0(self):
		self.assertEqual("Aquarius", what_is_my_sign(29, 1))

	def test_what_is_my_sign_1(self):
		self.assertEqual("Taurus", what_is_my_sign(8, 5))

	def test_what_is_my_sign_2(self):
		self.assertEqual("Gemini", what_is_my_sign(31, 5))


if __name__ == '__main__':
	unittest.main()