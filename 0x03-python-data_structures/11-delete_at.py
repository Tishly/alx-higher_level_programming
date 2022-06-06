#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    new_list = my_list[:]
    if idx in range(len(new_list)):
        i = new_list[idx]
        new_list.remove(i)
        return new_list
    return my_list
