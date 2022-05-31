#!/usr/bin/python3
def uppercase(str):
    for char in str:
        temp = ch
        if ord(ch) >= 97 and ord(ch) <= 122:
            temp = chr(ord(ch) - (ord('a') - ord('A')))
        print("{}".format(temp), end="")
    print()
