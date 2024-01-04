#!/usr/bin/python3
import random
number = random.randint(-10, 10)
num = number
if num < 0:
    print(f"{num} is negative")
elif num > 0:
    print(f"{num} is positive")
else:
    print(f"{num} is zero")
