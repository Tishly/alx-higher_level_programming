#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = eval(str(number)[-1])
if number < 0:
    last_digit = -(last_digit)
else:
    last_digit = abs(last_digit)
toPrint = (f"Last digit of {0:d} is {1:d} ".format(number, last_digit))
if last_digit > 5:
    print(toPrint + "and is greater than 5")
elif last_digit == 0:
    print(toPrint + "and is 0")
else:
    print(toPrint + "and is less than 6 and not 0")
