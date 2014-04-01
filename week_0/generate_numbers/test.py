import unittest
from subprocess import call


class TestGenerate_numbers(unittest.TestCase):
    def test_generate_numbers_0(self):
        call("py solution.py test.txt 10", shell=True)
        test_file = open("test.txt", "r")
        content = test_file.read()
        test_file.close()
        content = [int(x) for x in content.split()]
        self.assertEqual(10, len(content))
        call("rm test.txt", shell=True)


if __name__ == '__main__':
    unittest.main()
