#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        print(f"{(len(argv[1:])):d} arguments.")
    elif len(argv) == 2:
        print(f"{(len(argv[1:])):d} argument:")
    else:
        print(f"{(len(argv[1:])):d} arguments:")

    for i, arg in enumerate(argv):
        if i == 0:
            continue
        print(f"{i}: {arg}")
