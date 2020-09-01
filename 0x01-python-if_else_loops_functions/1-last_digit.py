#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = number
if number > 0:
    x %= 10
if number < 0:
    x %= -10
print("Last digit of", number, "is", end=" ")
if x > 5:
    print(x, "and is greater than 5")
if x == 0:
    print(x, "and is 0")
if x < 6 and x != 0:
    print(x, "and is less than 6 and not 0")
