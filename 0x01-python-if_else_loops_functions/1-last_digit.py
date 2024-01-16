#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
greater = " and is greater than 5"
zero = " and is 0"
less = " and is less than 6 and not 0"
# number = -6718
if number < 0:
    last_number = (abs(number) % 10) * -1
else:
    last_number = number % 10
if last_number > 5:
    print(f"Last digit of {number:d} is {last_number:d}" + greater)
elif last_number == 0:
    print(f"Last digit of {number:d} is {last_number:d}" + zero)
else:
    print(f"Last digit of {number:d} is {last_number:d}" + less)
