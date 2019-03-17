"""
test utils
"""
from random import randint
import time

# generate an array random or otherwise
def array_generator(start, end, isRandom=True, isRandomRange=False):
    """

    :rtype: list
    """
    if isRandom == True:
        if isRandomRange == True:
            end = randint(1, end)
        return [randint(start, end) for num in range(start, end+1)]
    else:
        return [num for num in range(start, end)]

def function_time(f):
    def wrap(*args):
        time1 = time.time()
        func = f(*args)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2-time1)*1000.0))
        return func
    return wrap
