import sys


def main():
    filename = sys.argv[1]
    test_file = open(filename, "r")
    print(test_file.read())
    test_file.close()


if __name__ == '__main__':
    main()
