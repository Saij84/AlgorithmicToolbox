#Uses python3

import sys
from operator import itemgetter
import time
import random

def sort_values(a):
    if len(a) == 1:
        return a

    return_list = sorted(a, key=itemgetter(0), reverse=True)  # sort according to first digit, reverse order

    # check if number in index zero, second number is smaller than index one, zero
    if len(return_list[0]) > 1 and return_list[0][0] == return_list[1][0]:
        if return_list[0][1] < return_list[1][0]:
            cache = return_list[0]  # store index 0
            return_list[0] = return_list[1]  # assign index one to zero
            return_list[1] = cache  # assign cache to index one

    return return_list

def largest_number(a):

    sorted_values = sort_values(a)
    res = ""
    for x in sorted_values:
        res += x
    return res

def test_generator():
    rand_int = []
    n = random.randint(1, 101)

    if n == 1:
        return str(n) + " " + str(random.randint(1, 10**3+1))

    for i in range(n-1):
        rand_int.append(str(random.randint(1, 10**3+1)))

    return_data = " ".join(rand_int)
    return str(n) + " " + return_data


if __name__ == '__main__':
    input = test_generator() #sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(a)
    print(largest_number(a))
