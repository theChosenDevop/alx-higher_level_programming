i#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 5:
    print("Last digit of {0} is {1} and is greater than 5".format(number, number[:-1]))
if number == 0:
    print("Last digit of {} is {-1} and is 0".format(number, number[:-1]))
