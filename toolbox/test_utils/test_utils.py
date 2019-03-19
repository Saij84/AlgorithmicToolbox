"""
test utils
"""
from random import randint
import time

# generate an array random or otherwise
def array_generator(start, end, isRandom=True, isRandomRange=False):
    if isRandom == True:
        if isRandomRange == True:
            end = randint(1, end)
        return [randint(start, end) for num in range(start, end+1)]
    else:
        return [num for num in range(start, end)]


# return time in milliseconds
def function_timer(function):
    def wrap(*args):
        start_time = time.time()
        func = function(*args)
        finish_time = time.time()
        print('{:s} function took {:.4f} ms'.format(function.__name__, (finish_time-start_time)*1000.0))
        return func
    return wrap
