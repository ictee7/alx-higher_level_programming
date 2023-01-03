#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)

n = num % 10

if n > 5:
    print("Last digit of {} is {} and is greater than 5".format(num, n))

elif n == 0:
    print("Last digit of {} is {} and is 0".format(num, n))

else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(num, n))
