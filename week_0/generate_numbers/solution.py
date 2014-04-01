import sys
from random import randint


def generate_numbers():
    filename = sys.argv[1]
    n = int(sys.argv[2])
    file_ = open(filename, "w")
    for i in range(n):
        file_.write(str(randint(1, 1000)) + " ")
    file_.close()


if __name__ == '__main__':
    generate_numbers()
