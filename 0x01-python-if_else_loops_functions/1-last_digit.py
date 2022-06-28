#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number - int(number / 10) * 10
if last_digit != 0 and last_digit < 6:
    decision = "and is less than 6 and not 0"
elif last_digit > 5:
    decision = "and is greater than 5"
elif last_digit == 0:
    decision = "and is 0"
print(f"Last digit of {number:d} is {last_digit:d} {decision}")
