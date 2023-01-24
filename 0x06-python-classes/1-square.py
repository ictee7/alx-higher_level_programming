#!/usr/bin/python3
""" Define a class Square."""


class Square:
    """Simple square class with his size as a field"""

    def __init__(self, size):
        """ Instance the class Square
            Args:
                size (int): the size of every side of the Square
                """
        self.__size = size
