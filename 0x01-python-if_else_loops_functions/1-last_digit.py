#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = (f"{number:d}")
last_digit = eval(digit[-1])
msg = f"Last digit of {number:d} is {last_digit:d} "
if last_digit > 5:
    print(msg + "and is greater than 5")
elif last_digit < 6 and not 0:
    print(msg + "and is less than 6 and not 0")
elif last_digit == 0:
    print(msg + "and is 0")
