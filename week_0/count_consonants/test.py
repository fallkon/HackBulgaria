import unittest
from solution import count_consonants

class TestSolution(unittest.TestCase):
	def test_count_consonants_0(self):
		self.assertEqual(4, count_consonants("Python"))

	def test_count_consonants_1(self):
		self.assertEqual(11, count_consonants("Theistareykjarbunga"))

	def test_count_consonants_2(self):
		self.assertEqual(7, count_consonants("grrrrgh!"))


if __name__ == '__main__':
	unittest.main()