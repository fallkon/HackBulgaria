import sys


def sum_numbers(filename):
    file_ = open(filename, "r")
    content = file_.read()
    file_.close()
    content = [int(x) for x in content.split()]
    count = sum(content)
    return count


def main():
    filename = sys.argv[1]
    print (sum_numbers(filename))

if __name__ == '__main__':
    main()
