import unittest
from subprocess import check_output, call


class TestCat(unittest.TestCase):
    def setUp(self):
        filename = "file"
        test_file = open(filename, "w")
        test_file.write("test test test")
        test_file.close()

    def test_cat(self):
        output = check_output("py solution.py file", shell=True).decode()
        self.assertEqual("test test test\n", output)

    def tearDown(self):
        call("rm file", shell=True)


if __name__ == '__main__':
    unittest.main()
