import sys


def main():
    for fl in sys.argv[1:]:
        test_file = open(fl, "r")
        print(test_file.read() + "\n")
        test_file.close()


if __name__ == '__main__':
    main()
