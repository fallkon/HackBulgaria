import unittest
from solution import count_words

class TestSolution(unittest.TestCase):
	def test_count_words_0(self):
		self.assertEqual({'apple': 2, 'pie': 1, 'banana': 1}, count_words(["apple", "banana", "apple", "pie"]))

	def test_count_words_1(self):
		self.assertEqual({'ruby': 1, 'python': 3}, count_words(["python", "python", "python", "ruby"]))

	def test_count_words_2(self):
		self.assertEqual({'helgi': 1, 'murarius': 1}, count_words(["helgi", "murarius"]))


if __name__ == '__main__':
	unittest.main()