from collections import Iterable
from operator import add
from math import factorial

def sum_list(l, func, op):
    s = 0
    if isinstance(l, Iterable):
        for el in l:
            op(sum_list(el, func, op), s)

        return s

    else:
        return func(float(l))


def sum_list_str(l):
    string = str(l).replace('[','').replace(']','')
    print(string)
    num_list = string.split(', ')
    return sum([float(num) for num in num_list])

my_list = [[[1, 2, [[3]]], [3, 7, 2]], [[8], 0], 1]

print(sum_list(my_list, factorial, add))
