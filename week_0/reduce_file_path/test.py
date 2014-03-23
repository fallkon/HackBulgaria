import unittest
from solution import reduce_file_path

class TestSolution(unittest.TestCase):
	def test_reduce_file_path_0(self):
		self.assertEqual("/", reduce_file_path("/"))

	def test_reduce_file_path_1(self):
		self.assertEqual("/etc/wtf", reduce_file_path("/etc//wtf/"))

	def test_reduce_file_path_2(self):
		self.assertEqual("/", reduce_file_path("/etc/../etc/../etc/../"))


if __name__ == '__main__':
	unittest.main()