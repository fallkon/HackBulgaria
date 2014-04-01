import unittest
from subprocess import call, check_output


class TestSumNumbers(unittest.TestCase):
    def setUp(self):
        filename = "numbers"
        test_file = open(filename, "w")
        test_file.write("10 10 15 15")
        test_file.close()

    def testSumNumbers(self):
        output = check_output("py solution.py numbers", shell=True).decode()
        self.assertEqual(50, int(output))

    def eraseFile():
        call("rm numbers", shel=True)


if __name__ == '__main__':
    unittest.main()
