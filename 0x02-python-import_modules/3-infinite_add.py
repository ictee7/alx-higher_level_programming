#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    n = len(argv)
    Sum = 0
    for i in range(1, n):
        Sum = Sum + int(argv[i])

    print(Sum)
