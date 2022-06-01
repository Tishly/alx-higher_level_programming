#!/usr/bin/python3

def rev_string(x):
    return x[::-1]
upLow = ""
for i in range(97, 123):
    if i % 2:
        upLow = upLow + upLow[i].upper()
    else:
        upLow = upLow + upLow[i].lower()
    print(f"{uplow}".format(rev_string(uplow)), end="")
