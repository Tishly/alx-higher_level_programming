#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
last_digit = int(number[-1])
number = int(number)
if number < 0:
    last_digit = -last_digit
else:
    last_digit = abs(last_digit)
msg = "Last digit of {} is {} ".format(number, last_digit)
if last_digit > 5:
    print(msg + "and is greater than 5")
elif last_digit == 0:
    print(msg + "and is 0")
else:
    print(msg + "and is less than 6 and not 0")
