#!/usr/bin/python3


# add a list of integers in a list
# only once per integer
def uniq_add(my_list=[]):
    new_list = []
    new_list = [new_list.append(x) for x in range(len(my_list) - 1) if x not in new_list]
    summ = 0
    for i in range(len(new_list) + 1):
        summ += i
    return summ
