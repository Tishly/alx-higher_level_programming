#!/usr/bin/python3
import sys


def safe_function(fct, *args):
        try:
            var = fct(*args)
            return var
        except Exception as err:
            sys.stderr.write("Exception: {}".format(err))
            return None
