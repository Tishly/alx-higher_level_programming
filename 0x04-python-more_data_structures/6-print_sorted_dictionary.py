#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary):
        print("{:s} : {}".format(key, a_dictionary[key]))
    # a_dict = sorted(a_dictionary.items())
    # return {k:v for k,v in a_dict}
