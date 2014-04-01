import unittest
from subprocess import check_output, call


class TestCat2(unittest.TestCase):
    def setUp(self):
        filename_0 = "file_0"
        filename_1 = "file_1"
        test_file = open(filename_0, "w")
        test_file.write("test test test")
        test_file.close()
        test_file = open(filename_1, "w")
        test_file.write("test test test")
        test_file.close()

    def testCat2(self):
        output = check_output("py solution.py file_0 file_1", shell=True)\
            .decode()
        self.assertEqual("test test test\n\ntest test test\n\n", output)

    def tearDown(self):
        call("rm file_0", shell=True)
        call("rm file_1", shell=True)


if __name__ == '__main__':
    unittest.main()
