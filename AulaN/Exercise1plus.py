from collections.abc import Iterable
from operator import add, mul
from math import factorial

def sum_list(l, func=float, op=add, init=0):
    s = init
    if isinstance(l, Iterable) and not (isinstance(l, str) and len(l) == 1):
        for el in l:
            s = op(s, sum_list(el, func, op, init))

        return s

    else:
        return func(l)


def sum_list_str(l):
    string = str(l).replace('[','').replace(']','')
    num_list = string.split(', ')
    return sum([float(num) for num in num_list])

my_list = [[[1, 2, [[3]]], [3, 7, 2]], [[8], 2], 1]

print(sum_list(my_list))
print(sum_list(my_list, func=lambda x: [x], init=[]))
